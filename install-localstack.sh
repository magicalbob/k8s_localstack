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

# add metrics
kubectl apply -f https://dev.ellisbs.co.uk/files/components.yaml

# install local storage
kubectl apply -f  local-storage-class.yaml

# create localstack namespace, if it doesn't exist
kubectl get ns localstack 2> /dev/null
if [ $? -eq 1 ]
then
    kubectl create namespace localstack
fi

# create deployment
kubectl apply -f localstack.deployment.yaml

# create service
kubectl apply -f localstack.service.yaml
