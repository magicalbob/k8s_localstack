resource "aws_instance" "example_server" {
  ami           = data.aws_ami.linux.id
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleServer"
  }
}
