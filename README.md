# Student CI/CD Project - Simple Calculator App

A simple Python web application demonstrating CI/CD concepts and best practices for your students.

## 📚 What is This Project?

This project teaches students about:
- **Python Web Development** using Flask
- **Unit Testing** with pytest
- **CI/CD Pipelines** with GitHub Actions
- **Docker Containerization**
- **Best Practices** in software development

## 🚀 Quick Start

### 1. Clone or Download the Project
```bash
cd student-ci-project
```

### 2. Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

The app will run at `http://localhost:5000`

### 5. Test the Application
```bash
pytest tests/ -v
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
├── .gitignore                      # Git ignore file
├── README.md                       # This file
├── tests/
│   └── test_app.py                # Unit tests
└── .github/
    └── workflows/
        └── ci.yml                 # GitHub Actions CI/CD pipeline
```

## 🔄 CI/CD Pipeline (GitHub Actions)

The `.github/workflows/ci.yml` file defines an automated CI/CD pipeline that:

1. **Triggers on**: Push to `main`/`develop` branches or Pull Requests
2. **Tests on**: Python 3.9, 3.10, and 3.11
3. **Steps**:
   - Checks out code
   - Sets up Python environment
   - Installs dependencies
   - Lints code for syntax errors
   - Runs unit tests with pytest
   - Generates code coverage report
   - Uploads coverage to Codecov
   - Builds Docker image

## 🐳 Docker Usage

### Build the Docker image
```bash
docker build -t student-calculator:latest .
```

### Run the container
```bash
docker run -p 5000:5000 student-calculator:latest
```

## 📝 Key Concepts for Students

### 1. **Functions** (app.py)
- Simple, testable functions
- Clear documentation with docstrings
- Error handling

### 2. **Web Framework** (Flask)
- REST API endpoints
- Request handling
- JSON responses

### 3. **Unit Testing** (tests/test_app.py)
- Test functions directly
- Test API endpoints
- Test error cases
- Using pytest fixtures

### 4. **CI/CD Pipeline** (.github/workflows/ci.yml)
- Automated testing on code push
- Multi-version testing
- Code coverage reporting
- Docker image building

### 5. **Docker** (Dockerfile)
- Containerizing Python applications
- Dependency management
- Port exposure

## ✅ Learning Outcomes

After working through this project, students will understand:

- ✓ How to structure a Python project
- ✓ Writing and running unit tests
- ✓ Setting up automated CI/CD pipelines
- ✓ Containerizing applications with Docker
- ✓ Version control best practices
- ✓ Deploying applications to the cloud

## 🤝 Contributing & Extending

Students can extend this project by:

1. Adding new mathematical operations
2. Creating a database for operation history
3. Adding authentication
4. Deploying to AWS/Azure/GCP
5. Adding more comprehensive error handling
6. Creating a frontend UI
7. Adding performance benchmarks

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Documentation](https://docs.docker.com/)

## 📪 Questions?

This project is designed as a teaching tool. Feel free to modify and extend it for your courses!

