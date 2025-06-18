# Django Project Setup & API Documentation

## 🛠️ Project Setup Instructions

Follow these steps to set up and run the Django project locally:

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Run the Development Server

```bash
python manage.py runserver
```

---

## 🔐 Authentication

Most API requests require a Bearer Token. Replace the token below with your valid JWT access token:

```http
Authorization: Bearer <your_token_here>
```

---

## 📬 API Endpoints

### 🔸 Register a New User

**POST** `/api/v1/auth/register/`

**Request Body:**

```json
{
  "email": "example@email.com",
  "username": "PERSON123",
  "password": "PASS@123",
  "password2": "PASS@123",
  "first_name": "ahmed",
  "last_name": "saeed"
}
```

---

### 🔸 Login

*(Note: This appears to be using the same register endpoint. You may need to update this if there's a dedicated login URL.)*

**POST** `/api/v1/auth/register/`

**Request Body:**

```json
{
  "email": "example@email.com",
  "username": "PERSON123",
  "password": "PASS@123",
  "password2": "PASS@123",
  "first_name": "ahmed",
  "last_name": "saeed"
}
```

---

## 🏢 Department Endpoints

### 🔹 Get All Departments

**GET** `/api/v1/departments/`

**Headers:**

```http
Authorization: Bearer <your_token_here>
```

---

### 🔹 Get a Single Department

**GET** `/api/v1/departments/1/`

**Headers:**

```http
Authorization: Bearer <your_token_here>
```

---

### 🔹 Create a Department

**POST** `/api/v1/departments/`

**Headers:**

```http
Authorization: Bearer <your_token_here>
```

**Request Body:**

```json
{
  "title": "Ant Man and The Wasp",
  "genre": "action",
  "year": 2018
}
```

---

## 📎 Notes

- Ensure your virtual environment is activated before installing dependencies or running the server.
- Update the port or domain in the URLs if your development server is configured differently.
- Replace the sample JWT token with your actual token.

---

## ✅ Example JWT Token (for testing)

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

> ⚠️ Use tokens securely and never expose them in production documentation or public repositories.

---

## 🧪 BDD Testing Steps

To run BDD tests using Behave:

```bash
behave
```

### 🧪 Running Selenium Tests

To run the Selenium tests for the project, use the following command:

```bash
python manage.py test tests.browser_departments
```

This will execute all browser-based integration tests located in the `tests/browser_departments.py` module.

---
---

## 🧰 Jenkinsfile (CI/CD Pipeline)

```groovy
pipeline {
  agent any

  environment {
    PYTHON_ENV = 'development'
  }

  stages {
    stage('Install Dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Run Migrations') {
      steps {
        sh 'python manage.py migrate'
      }
    }

    stage('Run Tests') {
      steps {
        sh 'pytest'
        sh 'behave'
      }
    }
  }

  post {
    always {
      junit '**/test-reports/*.xml'
    }
  }
}
```

---
