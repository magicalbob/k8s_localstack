Localstack in k8s
=================

A simple deployment of AWS LocalStack.

Run `./install-localstack.sh` to deploy it.

The install script runs `kubectl port-forward service/localstack-gateway-service -n localstack --address 127.0.0.1 4566:4566 &` at the end so that you can then do things like:

	aws --endpoint-url=http://localhost:4566 dynamodb list-tables 

but you could do:

	alias aws="$(which aws) --endpoint-url=http://192.168.0.10:4566"

and you'll be able to just do:

	aws sts get-caller-identity

But that's still over complicated.

Just do:

	export AWS_ENDPOINT_URL=http://192.168.0.10:4566

in your ~/.bashrc or similar.

Currently configured for cloudwatch, dynamodb, ebs, ec2, iam, lambda, s3, and sts aws services.

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

ec2:
####

	To decribe hosts:

		aws --endpoint-url=http://localhost:4566 ec2 describe-hosts

	Output:

		---------------
		|DescribeHosts|
		+-------------+

	To Describe VPCs:

		aws --endpoint-url=http://localhost:4566 ec2 describe-vpcs

	Output:

		--------------------------------------------------
		|                  DescribeVpcs                  |
		+------------------------------------------------+
		||                     Vpcs                     ||
		|+-----------------------+----------------------+|
		||  CidrBlock            |  172.31.0.0/16       ||
		||  DhcpOptionsId        |  default             ||
		||  InstanceTenancy      |  default             ||
		||  IsDefault            |  True                ||
		||  OwnerId              |  000000000000        ||
		||  State                |  available           ||
		||  VpcId                |  vpc-f1269111        ||
		|+-----------------------+----------------------+|
		|||           CidrBlockAssociationSet          |||
		||+----------------+---------------------------+||
		|||  AssociationId |  vpc-cidr-assoc-173ebc71  |||
		|||  CidrBlock     |  172.31.0.0/16            |||
		||+----------------+---------------------------+||
		||||              CidrBlockState              ||||
		|||+---------------+--------------------------+|||
		||||  State        |  associated              ||||
		|||+---------------+--------------------------+|||

ebs:
####

	No command's added yet.

requirements.txt includes all the python dependencies for awscli.

./aws contains example ~/.aws/ config and crededentials files with bogus keys.
