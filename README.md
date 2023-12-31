# Localstack in k8s

A simple deployment of AWS LocalStack in Kubernetes.

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

Currently configured for:

|Service | Enabled    |
| --- | --- |
|acm | Yes        |
| --- | --- |
|acm-pca | No         |
| --- | --- |
|amplify | No         |
| --- | --- |
|apigateway | Don't know |
| --- | --- |
|apigatewayv2 | Don't know |
| --- | --- |
|appconfig | Don't know |
| --- | --- |
|appconfigdata | Don't know |
| --- | --- |
|appsync | Don't know |
| --- | --- |
|athena | Don't know |
| --- | --- |
|autoscaling | Don't know |
| --- | --- |
|backup | Don't know |
| --- | --- |
|batch | Don't know |
| --- | --- |
|ce | Don't know |
| --- | --- |
|cloudcontrol | Don't know |
| --- | --- |
|cloudformation | Yes        |
| --- | --- |
|cloudfront | Don't know |
| --- | --- |
|cloudtrail | Don't know |
| --- | --- |
|cloudwatch | Don't know |
| --- | --- |
|codecommit | Don't know |
| --- | --- |
|cognito-identity | Don't know |
| --- | --- |
|cognito-idp | Don't know |
| --- | --- |
|dms | Don't know |
| --- | --- |
|docdb | Don't know |
| --- | --- |
|dynamodb | Yes |
| --- | --- |
|dynamodbstreams | Don't know |
| --- | --- |
|ebs | No |
| --- | --- |
|ec2 | Yes |
| --- | --- |
|ecr | Don't know |
| --- | --- |
|ecs | Don't know |
| --- | --- |
|efs | Don't know |
| --- | --- |
|eks | Don't know |
| --- | --- |
|elasticache | Don't know |
| --- | --- |
|elasticbeanstalk | Don't know |
| --- | --- |
|elbv2 | Don't know |
| --- | --- |
|emr | Don't know |
| --- | --- |
|emr-serverless | Don't know |
| --- | --- |
|es | Don't know |
| --- | --- |
|events | Don't know |
| --- | --- |
|firehose | Don't know |
| --- | --- |
|fis | Don't know |
| --- | --- |
|glacier | Don't know |
| --- | --- |
|glue | Don't know |
| --- | --- |
|iam | Don't know |
| --- | --- |
|identitystore | Don't know |
| --- | --- |
|iot | Don't know |
| --- | --- |
|iot-data | Don't know |
| --- | --- |
|iotanalytics | Don't know |
| --- | --- |
|iotwireless | Don't know |
| --- | --- |
|kafka | Don't know |
| --- | --- |
|kinesis | Don't know |
| --- | --- |
|kinesisanalytics | Don't know |
| --- | --- |
|kinesisanalyticsv2 | Don't know |
| --- | --- |
|kms | Yes        |
| --- | --- |
|lakeformation | Don't know |
| --- | --- |
|lambda | Yes |
| --- | --- |
|logs | Don't know |
| --- | --- |
|managedblockchain | Don't know |
| --- | --- |
|mediaconvert | Don't know |
| --- | --- |
|mediastore | Don't know |
| --- | --- |
|mq | Don't know |
| --- | --- |
|mwaa | Don't know |
| --- | --- |
|neptune | Don't know |
| --- | --- |
|opensearch | Don't know |
| --- | --- |
|organizations | Don't know |
| --- | --- |
|pi | Don't know |
| --- | --- |
|qldb | Don't know |
| --- | --- |
|qldb-session | Don't know |
| --- | --- |
|rds | Don't know |
| --- | --- |
|rds-data | Don't know |
| --- | --- |
|redshift | Don't know |
| --- | --- |
|redshift-data | Don't know |
| --- | --- |
|resource-groups | Don't know |
| --- | --- |
|resourcegroupstaggingapi | Don't know |
| --- | --- |
|route53 | Don't know |
| --- | --- |
|route53resolver | Don't know |
| --- | --- |
|s3 | Yes        |
| --- | --- |
|s3control | Don't know |
| --- | --- |
|sagemaker | Don't know |
| --- | --- |
|sagemaker-runtime | Don't know |
| --- | --- |
|secretsmanager | Don't know |
| --- | --- |
|serverlessrepo | Don't know |
| --- | --- |
|servicediscovery | Don't know |
| --- | --- |
|ses | Don't know |
| --- | --- |
|sesv2 | Don't know |
| --- | --- |
|sns | Don't know |
| --- | --- |
|sqs | Don't know |
| --- | --- |
|ssm | Don't know |
| --- | --- |
|stepfunctions | Don't know |
| --- | --- |
|sts | Don't know |
| --- | --- |
|timestream-query | Don't know |
| --- | --- |
|timestream-write | Don't know |
| --- | --- |
|transcribe | Don't know |
| --- | --- |
|wafv2 | Don't know |
| --- | --- |
|xray | Don't know |

## acm:

	To list certificates:

		aws acm list-certificates

	Output:

		{
		    "CertificateSummaryList": []
		}

## cloudformation:

	To list stacks:

		aws cloudformation list-stacks

	Output:

		{
		    "StackSummaries": []
		}

## dynamodb:

	To list tables:

		aws dynamodb list-tables 

	Output:

		{
		    "TableNames": []
		}

## ec2:

	To decribe hosts:

		aws ec2 describe-hosts

	Output:

		---------------
		|DescribeHosts|
		+-------------+

	To Describe VPCs:

		aws ec2 describe-vpcs

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

## lambda:

	To list functions:

		aws lambda list-functions

	Output:

		{
		    "Functions": []
		}

## kms:

	To list keys:

		aws kms list-keys

	Output:

	{
	    "Keys": []
	}

## s3:

	To create bucket:

		aws s3 mb s3://aws

	Output:
	
		make_bucket: aws

	To copy a file to that bucket:

		aws s3 cp aws/credentials s3://aws

	Output:

		upload: aws/credentials to s3://aws/credentials                 

	To list the buckets content:

		aws s3 ls s3://aws

	Output:

		2023-12-25 10:04:19         62 credentials

requirements.txt includes all the python dependencies for awscli.

./aws contains example ~/.aws/ config and crededentials files with bogus keys.

### localstack_ui

This is a light weight Flask app that gives web access to aws services (either localstack or aws.com).
