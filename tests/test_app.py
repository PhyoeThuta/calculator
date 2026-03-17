"""
Unit tests for the Calculator Application
Demonstrates how to test Python applications using pytest
"""

import pytest
from app import app, add, subtract, multiply, divide


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestBasicOperations:
    """Test basic arithmetic operations"""

    def test_add(self):
        """Test addition function"""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0.5, 0.5) == 1.0

    def test_subtract(self):
        """Test subtraction function"""
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
        assert subtract(1.5, 0.5) == 1.0

    def test_multiply(self):
        """Test multiplication function"""
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10
        assert multiply(0.5, 2) == 1.0

    def test_divide(self):
        """Test division function"""
        assert divide(6, 2) == 3
        assert divide(5, 2) == 2.5
        assert divide(-10, 2) == -5

    def test_divide_by_zero(self):
        """Test that division by zero raises an error"""
        with pytest.raises(ValueError):
            divide(5, 0)


class TestAPIEndpoints:
    """Test Flask API endpoints"""

    def test_home_endpoint(self, client):
        """Test the home endpoint (HTML response)"""
        response = client.get('/')
        assert response.status_code == 200
        # HTML template ကို စစ်ဆေးရန် get_data(as_text=True) ကို သုံးရပါမည်
        html_content = response.get_data(as_text=True)
        # index.html ထဲတွင် 'Calculator' ဆိုသော စာသားပါဝင်ကြောင်း စစ်ဆေးခြင်း
        assert "Calculator" in html_content

    def test_add_endpoint(self, client):
        """Test the /add endpoint"""
        response = client.get('/add?a=5&b=3')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 8
        assert data['operation'] == 'add'

    def test_subtract_endpoint(self, client):
        """Test the /subtract endpoint"""
        response = client.get('/subtract?a=10&b=3')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 7
        assert data['operation'] == 'subtract'

    def test_multiply_endpoint(self, client):
        """Test the /multiply endpoint"""
        response = client.get('/multiply?a=4&b=5')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 20
        assert data['operation'] == 'multiply'

    def test_divide_endpoint(self, client):
        """Test the /divide endpoint"""
        response = client.get('/divide?a=10&b=2')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 5
        assert data['operation'] == 'divide'

    def test_divide_endpoint_by_zero(self, client):
        """Test the /divide endpoint with zero"""
        response = client.get('/divide?a=5&b=0')
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data

    def test_invalid_input(self, client):
        """Test endpoint with invalid input"""
        response = client.get('/add?a=invalid&b=3')
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data