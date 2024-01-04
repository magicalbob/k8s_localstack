provider "aws" {
  region                      = "eu-west-2"
  profile                     = "default"
  access_key                  = "fake"
  secret_key                  = "fake"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  s3_use_path_style           = true

  endpoints {
    apigateway      = "http://127.0.0.1:4566"
    apigatewayv2    = "http://127.0.0.1:4566"
    cloudformation  = "http://127.0.0.1:4566"
    cloudwatch      = "http://127.0.0.1:4566"
    cognitoidp      = "http://127.0.0.1:4566"
    cognitoidentity = "http://127.0.0.1:4566"
    dynamodb        = "http://127.0.0.1:4566"
    ec2             = "http://127.0.0.1:4566"
    es              = "http://127.0.0.1:4566"
    elasticache     = "http://127.0.0.1:4566"
    firehose        = "http://127.0.0.1:4566"
    iam             = "http://127.0.0.1:4566"
    kinesis         = "http://127.0.0.1:4566"
    lambda          = "http://127.0.0.1:4566"
    rds             = "http://127.0.0.1:4566"
    redshift        = "http://127.0.0.1:4566"
    route53         = "http://127.0.0.1:4566"
    s3              = "http://127.0.0.1:4566"
    secretsmanager  = "http://127.0.0.1:4566"
    ses             = "http://127.0.0.1:4566"
    sns             = "http://127.0.0.1:4566"
    sqs             = "http://127.0.0.1:4566"
    ssm             = "http://127.0.0.1:4566"
    stepfunctions   = "http://127.0.0.1:4566"
    sts             = "http://127.0.0.1:4566"
  }
}
