# Localstack in k8s

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

Currently configured for:

	acm,
	acm-pca,
	amplify,
	apigateway,
	apigatewayv2,
	appconfig,
	appconfigdata,
	appsync,
	athena,
	autoscaling,
	backup,
	batch,
	ce,
	cloudcontrol,
	cloudformation,
	cloudfront,
	cloudtrail,
	cloudwatch,
	codecommit,
	cognito-identity,
	cognito-idp,
	dms,
	docdb,
	dynamodb,
	dynamodbstreams,
	ec2,
	ecr,
	ecs,
	efs,
	eks,
	elasticache,
	elasticbeanstalk,
	elbv2,
	emr,
	emr-serverless,
	es,
	events,
	firehose,
	fis,
	glacier,
	glue,
	iam,
	identitystore,
	iot,
	iot-data,
	iotanalytics,
	iotwireless,
	kafka,
	kinesis,
	kinesisanalytics,
	kinesisanalyticsv2,
	kms,
	lakeformation,
	lambda,
	logs,
	managedblockchain,
	mediaconvert,
	mediastore,
	mq,
	mwaa,
	neptune,
	opensearch,
	organizations,
	pi,
	qldb,
	qldb-session,
	rds,
	rds-data,
	redshift,
	redshift-data,
	resource-groups,
	resourcegroupstaggingapi,
	route53,
	route53resolver,
	s3,
	s3control,
	sagemaker,
	sagemaker-runtime,
	secretsmanager,
	serverlessrepo,
	servicediscovery,
	ses,
	sesv2,
	sns,
	sqs,
	ssm,
	stepfunctions,
	sts,
	timestream-query,
	timestream-write,
	transcribe,
	wafv2,
	xray

## acm:

	To list certificates:

		aws acm list-certificates

	Output:

		{
		    "CertificateSummaryList": []
		}

## acm-pca:

	API for service 'acm-pca' not yet implemented or pro feature

## amplify:

	API for service 'amplify' is a pro feature

## cloudformation:

	To list stacks:

		aws cloudformation list-stacks

	Output:

		{
		    "StackSummaries": []
		}

## ec2:

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

## ebs:

	Not able to test commands yet, but `aws ebs` looks to work.

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
