unset USE_KIND
# Check if kubectl is available in the system
if kubectl 2>/dev/null >/dev/null; then
  # Check if kubectl can communicate with a Kubernetes cluster
  if kubectl get nodes 2>/dev/null >/dev/null; then
    echo "Kubernetes cluster is available. Using existing cluster."
    export USE_KIND=0
  else
    echo "Kubernetes cluster is not available. Creating a Kind cluster..."
    export USE_KIND=X
  fi
else
  echo "kubectl is not installed. Please install kubectl to interact with Kubernetes."
  export USE_KIND=X
fi

if [ "X${USE_KIND}" == "XX" ]; then
    # Make sure cluster exists if using Kind
    kind  get clusters 2>&1 | grep "kind-localstack"
    if [ $? -gt 0 ]
    then
        envsubst < kind-config.yaml.template > kind-config.yaml
        kind create cluster --config kind-config.yaml --name kind-localstack
    fi

    # Make sure create cluster succeeded
    kind  get clusters 2>&1 | grep "kind-localstack"
    if [ $? -gt 0 ]
    then
        echo "Creation of cluster failed. Aborting."
        exit 666
    fi
fi

echo add metrics
kubectl apply -f https://dev.ellisbs.co.uk/files/components.yaml

echo install local storage
kubectl apply -f  local-storage-class.yaml

echo create localstack namespace, if it does not exist
kubectl get ns localstack 2> /dev/null
if [ $? -eq 1 ]
then
    kubectl create namespace localstack
fi

echo create deployment
kubectl apply -f localstack.deployment.yaml

echo create service
kubectl apply -f localstack.service.yaml

echo wait for deployment to be running
until kubectl get all -n localstack|grep ^pod/|grep 1/1; do
  sleep 5
done

echo create port-forward to access localstack on port 4566
if ! nc -z -w1 192.168.0.10 4566; then
  # Port 4566 is not already forwarded, so execute the port-forwarding command
  kubectl port-forward service/localstack-gateway-service -n localstack --address 192.168.0.14 4566:4566 &
else
  echo "Port 4566 is already forwarded."
fi
