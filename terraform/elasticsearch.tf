resource "aws_elasticsearch_domain" "example_domain" {
  domain_name           = "my-elastic-domain"
  elasticsearch_version = "7.10"
  cluster_config {
    instance_type  = "m4.large.elasticsearch"
    instance_count = 1
  }
  ebs_options {
    ebs_enabled = true
    volume_size = 10
  }
  access_policies = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "es.amazonaws.com"
        },
        Action   = "es:ESHttpPut",
        Resource = "arn:aws:es:${var.aws_region}:${var.aws_account_id}:domain/my-elastic-domain/*",
        Condition = {
          IpAddress : {
            "aws:SourceIp" : "192.168.0.10"
          }
        }
      }
    ]
  })
}

output "elasticsearch_endpoint" {
  value = aws_elasticsearch_domain.example_domain.endpoint
}

