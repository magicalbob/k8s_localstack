provider "aws" {
  region                      = "eu-west-2"
  profile                     = "default"
  access_key                  = "fake"
  secret_key                  = "fake"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    apigateway      = "http://192.168.0.10:4566"
    apigatewayv2    = "http://192.168.0.10:4566"
    cloudformation  = "http://192.168.0.10:4566"
    cloudwatch      = "http://192.168.0.10:4566"
    cognitoidp      = "http://192.168.0.10:4566"
    cognitoidentity = "http://192.168.0.10:4566"
    dynamodb        = "http://192.168.0.10:4566"
    ec2             = "http://192.168.0.10:4566"
    es              = "http://192.168.0.10:4566"
    elasticache     = "http://192.168.0.10:4566"
    firehose        = "http://192.168.0.10:4566"
    iam             = "http://192.168.0.10:4566"
    kinesis         = "http://192.168.0.10:4566"
    lambda          = "http://192.168.0.10:4566"
    rds             = "http://192.168.0.10:4566"
    redshift        = "http://192.168.0.10:4566"
    route53         = "http://192.168.0.10:4566"
    s3              = "http://192.168.0.10:4566"
    secretsmanager  = "http://192.168.0.10:4566"
    ses             = "http://192.168.0.10:4566"
    sns             = "http://192.168.0.10:4566"
    sqs             = "http://192.168.0.10:4566"
    ssm             = "http://192.168.0.10:4566"
    stepfunctions   = "http://192.168.0.10:4566"
    sts             = "http://192.168.0.10:4566"
  }
}
