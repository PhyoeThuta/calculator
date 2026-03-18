provider "aws" {
  region = "ap-southeast-1"
}

resource "aws_vpc" "calc_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags                 = { Name = "calculator-vpc" }
}

# ၂။ Internet Gateway ဆောက်ခြင်း (Internet ထွက်ရန်)
resource "aws_internet_gateway" "calc_igw" {
  vpc_id = aws_vpc.calc_vpc.id
  tags   = { Name = "calculator-igw" }
}

# ၃။ Subnet တစ်ခု ဆောက်ခြင်း
resource "aws_subnet" "calc_subnet" {
  vpc_id                  = aws_vpc.calc_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true # IP အလိုအလျောက် ရရှိရန်
  availability_zone       = "ap-southeast-1a"
  tags                    = { Name = "calculator-subnet" }
}

# ၄။ Route Table ဆောက်ခြင်း (Traffic လမ်းညွှန်ရန်)
resource "aws_route_table" "calc_rt" {
  vpc_id = aws_vpc.calc_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.calc_igw.id
  }
}

# ၅။ Subnet နှင့် Route Table ကို ချိတ်ဆက်ခြင်း
resource "aws_route_table_association" "calc_rta" {
  subnet_id      = aws_subnet.calc_subnet.id
  route_table_id = aws_route_table.calc_rt.id
}

resource "aws_instance" "calc_server" {
  ami           = "ami-011d19742f14ff9b8"
  instance_type = "t2.micro"
  key_name      = "ec2-web"

  # 👇 ဒါက အရေးကြီးဆုံးပါ၊ ဆောက်ထားတဲ့ subnet ထဲမှာ ဆောက်ခိုင်းတာပါ
  subnet_id = aws_subnet.calc_subnet.id

  # 👇 Security Group ကို ID နဲ့ ချိတ်ရပါမယ်
  vpc_security_group_ids = [aws_security_group.calc_sg.id]

  tags = {
    Name = "Calculator-Deployment-Server"
  }
}

resource "aws_security_group" "calc_sg" {
  name   = "calculator-security-group"
  vpc_id = aws_vpc.calc_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # SSH Access
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Flask App Access
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "public_ip" {
  value = aws_instance.calc_server.public_ip
}