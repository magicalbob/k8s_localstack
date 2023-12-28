resource "aws_instance" "example_server" {
  ami           = data.aws_ami.linux.id
  instance_type = "t2.micro"

  user_data = <<-EOF
              #!/bin/bash
              echo "Hello" > /tmp/world.txt
              EOF

  tags = {
    Name = "ExampleServer"
  }
}
