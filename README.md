# Localstack in k8s

## Kubernetes

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

## Dockerfile

If you don't want to bother with that k8s nonsense, there's a `docker-compose.yml` that gives you the same thing.

## Config of localstack

Currently configured for:

|Service | Enabled    |
| --- | --- |
|acm | Yes        |
| --- | --- |
|acm-pca | No         |
| --- | --- |
|amplify | No         |
| --- | --- |
|apigateway | Yes |
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
|backup | No |
| --- | --- |
|batch | No |
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
|cloudwatch | Yes |
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
|eks | No |
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
|es | Yes |
| --- | --- |
|events | Yes |
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

### acm:

	To list certificates:

		aws acm list-certificates

	Output:

		{
		    "CertificateSummaryList": []
		}

### apigateway

	To get api keysL

		aws apigateway get-api-keys

	Output:

		{
		    "items": []
		}

### cloudformation:

	To list stacks:

		aws cloudformation list-stacks

	Output:

		{
		    "StackSummaries": []
		}

### cloudwatch

	To list metrics:

		aws cloudwatch list-metrics

	Output:

		{
		    "Metrics": []
		}

### dynamodb:

	To list tables:

		aws dynamodb list-tables 

	Output:

		{
		    "TableNames": []
		}

### ec2:

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

### es:

	To create an elasticsearch domain:

		aws es create-elasticsearch-domain --domain-name elastic.example.com

	Output:

		{
		    "DomainStatus": {
		        "DomainId": "000000000000/elastic.example.com",
		        "DomainName": "elastic.example.com",
		        "ARN": "arn:aws:es:eu-west-2:000000000000:domain/elastic.example.com",
		        "Created": true,
		        "Deleted": false,
		        "Endpoint": "elastic.example.com.eu-west-2.es.localhost.localstack.cloud:4566",
		        "Processing": true,
		        "UpgradeProcessing": false,
		        "ElasticsearchVersion": "7.10",
		        "ElasticsearchClusterConfig": {
		            "InstanceType": "m3.medium.elasticsearch",
		            "InstanceCount": 1,
		            "DedicatedMasterEnabled": true,
		            "ZoneAwarenessEnabled": false,
		            "DedicatedMasterType": "m3.medium.elasticsearch",
		            "DedicatedMasterCount": 1,
		            "WarmEnabled": false,
		            "ColdStorageOptions": {
		                "Enabled": false
		            }
		        },
		        "EBSOptions": {
		            "EBSEnabled": true,
		            "VolumeType": "gp2",
		            "VolumeSize": 10,
		            "Iops": 0
		        },
		        "AccessPolicies": "",
		        "SnapshotOptions": {
		            "AutomatedSnapshotStartHour": 0
		        },
		        "CognitoOptions": {
		            "Enabled": false
		        },
		        "EncryptionAtRestOptions": {
		            "Enabled": false
		        },
		        "NodeToNodeEncryptionOptions": {
		            "Enabled": false
		        },
		        "AdvancedOptions": {
		            "override_main_response_version": "false",
		            "rest.action.multi.allow_explicit_index": "true"
		        },
		        "ServiceSoftwareOptions": {
		            "CurrentVersion": "",
		            "NewVersion": "",
		            "UpdateAvailable": false,
		            "Cancellable": false,
		            "UpdateStatus": "COMPLETED",
		            "Description": "There is no software update available for this domain.",
		            "AutomatedUpdateDate": 0.0,
		            "OptionalDeployment": true
		        },
		        "DomainEndpointOptions": {
		            "EnforceHTTPS": false,
		            "TLSSecurityPolicy": "Policy-Min-TLS-1-0-2019-07",
		            "CustomEndpointEnabled": false
		        },
		        "AdvancedSecurityOptions": {
		            "Enabled": false,
		            "InternalUserDatabaseEnabled": false
		        },
		        "AutoTuneOptions": {
		            "State": "ENABLE_IN_PROGRESS"
		        }
		    }
		}

	To list domain names:

		aws es list-domain-names

	Output:

		{
		    "DomainNames": [
		        {
		            "DomainName": "elastic.example.com",
		            "EngineType": "Elasticsearch"
		        }
		    ]
		}

	To list versions:

		aws es list-elasticsearch-versions

	Output:

		{
		    "ElasticsearchVersions": [
		        "OpenSearch_2.9",
		        "OpenSearch_2.7",
		        "OpenSearch_2.5",
		        "OpenSearch_2.3",
		        "OpenSearch_1.3",
		        "OpenSearch_1.2",
		        "OpenSearch_1.1",
		        "OpenSearch_1.0",
		        "7.10",
		        "7.9",
		        "7.8",
		        "7.7",
		        "7.4",
		        "7.1",
		        "6.8",
		        "6.7",
		        "6.5",
		        "6.4",
		        "6.3",
		        "6.2",
		        "6.0",
		        "5.6",
		        "5.5",
		        "5.3",
		        "5.1"
		    ]
		}

### events:

	To list connections:

		aws events list-connections

	Output:

		{
		    "Connections": []
		}

### lambda:

	To list functions:

		aws lambda list-functions

	Output:

		{
		    "Functions": []
		}

### kms:

	To list keys:

		aws kms list-keys

	Output:

	{
	    "Keys": []
	}

### s3:

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

# localstack_ui

This is a light weight Flask app that gives web access to aws services (either localstack or aws.com).

The `config.json` file defines the services and menus available in the app, and how it should fetch the info from aws. If you have `AWS_ENDPOINT_URL` pointing at localstack it will get the info from there, if you unset that it will get it from aws.com.

# terraform

This is terraform working with localstack.

It implements an EC2 instance, and an ElasticSearch domain.
