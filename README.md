Localstack in k8s
=================

A simple deployment of AWS LocalStack.

Run `./install-localstack.sh` to deploy it.

The install script runs `kubectl port-forward service/localstack-gateway-service -n localstack --address 127.0.0.1 4566:4566 &` at the end so that you can then do things like:

	aws --endpoint-url=http://localhost:4566 dynamodb list-tables 

Currently configured for s3, sts and dynamodb aws services.

s3:
###

	To create bucket:

		aws --endpoint-url=http://localhost:4566 s3 mb s3://aws

	Output:
	
		make_bucket: aws

	To copy a file to that bucket:

		aws --endpoint-url=http://localhost:4566 s3 cp aws/credentials s3://aws

	Output:

		upload: aws/credentials to s3://aws/credentials                 

	To list the buckets content:

		aws --endpoint-url=http://localhost:4566 s3 ls s3://aws

	Output:

		2023-12-25 10:04:19         62 credentials

requirements.txt includes all the python dependencies for awscli.

./aws contains example ~/.aws/ config and crededentials files with bogus keys.
