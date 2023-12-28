data "aws_ami" "linux" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amazon-eks-node-linux"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["801119661308"]
}
