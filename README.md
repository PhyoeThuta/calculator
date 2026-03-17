# Student CI/CD Project - Simple Calculator App

A comprehensive Python web application demonstrating modern CI/CD principles, infrastructure as code, and DevOps best practices. This project serves as an educational platform for learning containerization, configuration management, and cloud deployment.

## 📚 Project Overview

This project teaches students about:
- **Python Web Development** using Flask
- **Unit Testing** with pytest and code coverage
- **CI/CD Pipelines** with automated workflows
- **Docker Containerization** for consistent deployments
- **Infrastructure as Code** using Terraform for AWS
- **Configuration Management** using Ansible
- **Best Practices** in software development and DevOps

## 🏗️ Architecture

This project demonstrates a complete deployment pipeline:
- **Application**: Flask-based calculator app with REST API
- **Containerization**: Docker for reproducible environments
- **Infrastructure**: Terraform for AWS VPC, EC2, and security groups
- **Orchestration**: Ansible for automated deployment and configuration

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker (for containerization)
- Terraform (for AWS infrastructure)
- Ansible (for deployment automation)
- AWS Account (for cloud deployment)

### Local Development

#### 1. Clone or Download the Project
```bash
cd student-ci-project
```

#### 2. Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run the Application
```bash
python app.py
```

The app will run at `http://localhost:5000`

#### 5. Run Tests
```bash
pytest tests/ -v
pytest tests/ --cov=. --cov-report=html
```

## 📡 API Endpoints

| Endpoint | Method | Parameters | Example |
|----------|--------|-----------|---------|
| `/` | GET | - | `http://localhost:5000/` |
| `/add` | GET | `a`, `b` | `http://localhost:5000/add?a=5&b=3` |
| `/subtract` | GET | `a`, `b` | `http://localhost:5000/subtract?a=5&b=3` |
| `/multiply` | GET | `a`, `b` | `http://localhost:5000/multiply?a=5&b=3` |
| `/divide` | GET | `a`, `b` | `http://localhost:5000/divide?a=6&b=3` |

## 🧪 Testing

### Run all tests
```bash
pytest tests/ -v
```

### Run tests with coverage
```bash
pytest tests/ --cov=. --cov-report=html
```

### Run specific test
```bash
pytest tests/test_app.py::TestBasicOperations::test_add -v
```

## 📦 Project Structure

```
student-ci-project/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker configuration
├── README.md                       # Project documentation
├── templates/
│   └── index.html                 # HTML frontend
├── static/
│   ├── style.css                  # CSS styling
│   └── script.js                  # JavaScript functionality
├── tests/
│   ├── __init__.py
│   └── test_app.py                # Unit tests
├── ansible/
│   ├── ansible.cfg                # Ansible configuration
│   ├── hosts.ini                  # Inventory file
│   └── playbook.yml               # Ansible deployment playbook
└── terraform/
    ├── main.tf                    # Terraform AWS infrastructure
    └── terraform.tfstate          # Terraform state file
```

## 🌥️ Cloud Deployment with AWS

### Prerequisites
- AWS Account with appropriate permissions
- AWS CLI configured (`aws configure`)
- Terraform installed
- Ansible installed
- SSH key pair for EC2 access

### Step 1: Deploy Infrastructure with Terraform

```bash
cd terraform

# Initialize Terraform
terraform init

# Preview infrastructure changes
terraform plan

# Apply infrastructure
terraform apply

# Save the output (public_ip will be needed for Ansible)
terraform output public_ip
```

This creates:
- VPC with CIDR block 10.0.0.0/16
- Internet Gateway for external access
- Subnet for EC2 instances
- Security Group with ports 22 (SSH) and 5000 (Flask)
- EC2 t2.micro instance running Amazon Linux

### Step 2: Deploy Application with Ansible

Update the `ansible/hosts.ini` with the public IP from Terraform output:

```ini
[servers]
<PUBLIC_IP> ansible_user=ec2-user ansible_ssh_private_key_file=/path/to/key.pem
```

Run the playbook:
```bash
cd ansible
ansible-playbook -i hosts.ini playbook.yml
```

This will:
- Install Docker on the EC2 instance
- Pull the Docker image
- Start the calculator container
- Configure auto-restart

### Accessing the Application
```
http://<PUBLIC_IP>:5000
```

## 📊 CI/CD Pipeline (GitHub Actions)

The `.github/workflows/ci.yml` file defines an automated CI/CD pipeline that:

1. **Triggers on**: Push to `main`/`develop` branches or Pull Requests
2. **Tests on**: Python 3.9, 3.10, and 3.11
3. **Automated Steps**:
   - Checks out code
   - Sets up Python environment
   - Installs dependencies
   - Lints code for syntax errors
   - Runs unit tests with pytest
   - Generates code coverage report
   - Builds Docker image

## 🧪 Testing

### Run all tests
```bash
pytest tests/ -v
```

### Run tests with coverage
```bash
pytest tests/ --cov=. --cov-report=html
```

### Run specific test
```bash
pytest tests/test_app.py::TestBasicOperations::test_add -v
```

## 🐳 Docker

### Build locally
```bash
docker build -t student-calculator:latest .
```

### Run container locally
```bash
docker run -p 5000:5000 student-calculator:latest
```

### Build and push to Docker Hub (optional)
```bash
# Tag the image
docker tag student-calculator:latest <your-dockerhub-username>/student-calculator:latest

# Push to Docker Hub
docker push <your-dockerhub-username>/student-calculator:latest
```

## 🔐 Security Considerations

- **IP Whitelisting**: Restrict SSH access to known IPs in production
- **Secrets Management**: Use AWS Secrets Manager for sensitive data
- **SSL/TLS**: Add HTTPS certificate for production
- **Database**: Use RDS instead of local persistence
- **Monitoring**: Enable CloudWatch for logs and metrics

## 📝 Key Concepts for Students

### 1. **Functions** (app.py)
- Simple, testable functions
- Documentation with docstrings
- Error handling

### 2. **Web Framework** (Flask)
- REST API endpoints
- Request handling
- JSON responses

### 3. **Unit Testing** (tests/test_app.py)
- Test functions and API endpoints
- Test edge cases and error conditions
- Using pytest fixtures

### 4. **Infrastructure as Code** (terraform/)
- Define cloud resources
- Version control infrastructure
- Reproducible deployments

### 5. **Configuration Management** (ansible/)
- Automate server setup
- Install and configure services
- Idempotent operations

### 6. **Containerization** (Dockerfile)
- Package application with dependencies
- Ensure consistency across environments
- Simplified deployment

## ✅ Learning Outcomes

After completing this project, students will understand:

- ✓ Python web application development with Flask
- ✓ Writing and running comprehensive unit tests
- ✓ Docker containerization
- ✓ Infrastructure as Code using Terraform
- ✓ Configuration management with Ansible
- ✓ CI/CD automation with GitHub Actions
- ✓ Cloud deployment to AWS
- ✓ DevOps best practices

## 🤝 Contributing & Extending

Students can enhance this project by:

1. Adding new mathematical operations (logarithm, exponentiation, etc.)
2. Implementing a database for operation history
3. Adding user authentication
4. Deploying to other cloud providers (Azure, GCP)
5. Implementing comprehensive error handling and validation
6. Creating an enhanced web UI with real-time updates
7. Adding performance monitoring and logging
8. Setting up a CI/CD pipeline with GitHub Actions
9. Implementing load balancing with multiple servers
10. Adding database backup and disaster recovery

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Docker Documentation](https://docs.docker.com/)
- [Terraform AWS Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Ansible Documentation](https://docs.ansible.com/)
- [AWS Documentation](https://docs.aws.amazon.com/)

## 📄 License

This project is provided as an educational resource.

## 📪 Support

This project is designed as a teaching tool. Feel free to modify and extend it for your courses!

