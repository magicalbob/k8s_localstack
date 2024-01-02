resource "aws_s3_bucket" "example_bucket" {
  bucket = "aws"
  acl    = "private"

  timeouts {
    create = "1m"
  }
}
