provider "aws" {
  region                      = "eu-west-2"
  profile                     = "default"
  access_key                  = "fake"
  secret_key                  = "fake"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    apigateway      = "http://nexus.ellisbs.co.uk:4566"
    apigatewayv2    = "http://nexus.ellisbs.co.uk:4566"
    cloudformation  = "http://nexus.ellisbs.co.uk:4566"
    cloudwatch      = "http://nexus.ellisbs.co.uk:4566"
    cognitoidp      = "http://nexus.ellisbs.co.uk:4566"
    cognitoidentity = "http://nexus.ellisbs.co.uk:4566"
    dynamodb        = "http://nexus.ellisbs.co.uk:4566"
    ec2             = "http://nexus.ellisbs.co.uk:4566"
    es              = "http://nexus.ellisbs.co.uk:4566"
    elasticache     = "http://nexus.ellisbs.co.uk:4566"
    firehose        = "http://nexus.ellisbs.co.uk:4566"
    iam             = "http://nexus.ellisbs.co.uk:4566"
    kinesis         = "http://nexus.ellisbs.co.uk:4566"
    lambda          = "http://nexus.ellisbs.co.uk:4566"
    rds             = "http://nexus.ellisbs.co.uk:4566"
    redshift        = "http://nexus.ellisbs.co.uk:4566"
    route53         = "http://nexus.ellisbs.co.uk:4566"
    s3              = "http://nexus.ellisbs.co.uk:4566"
    secretsmanager  = "http://nexus.ellisbs.co.uk:4566"
    ses             = "http://nexus.ellisbs.co.uk:4566"
    sns             = "http://nexus.ellisbs.co.uk:4566"
    sqs             = "http://nexus.ellisbs.co.uk:4566"
    ssm             = "http://nexus.ellisbs.co.uk:4566"
    stepfunctions   = "http://nexus.ellisbs.co.uk:4566"
    sts             = "http://nexus.ellisbs.co.uk:4566"
  }
}
