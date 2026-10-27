# Cloud Status API

A containerized REST API built with **Python, FastAPI, Docker, and GitHub Actions**. This project demonstrates API development, automated testing, containerization, and continuous integration as part of a cloud and DevOps learning portfolio.

## Features

- REST API with FastAPI
- Health-check endpoint with a UTC timestamp
- Application information endpoint
- Interactive API documentation using Swagger UI
- Automated tests using Pytest
- Docker image for consistent, isolated deployment
- GitHub Actions CI pipeline for automated testing and Docker image builds

## Architecture

```text
Developer
   |
   v
GitHub Repository
   |
   v
GitHub Actions CI
   |-------------------|
   v                   v
Python Tests       Docker Build
   |
   v
FastAPI Application
   |
   v
Uvicorn Server
   |
   v
Docker Container
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI web server |
| Pytest | Automated testing |
| Docker | Application containerization |
| Git & GitHub | Version control and source hosting |
| GitHub Actions | Continuous integration |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns the API welcome message |
| GET | `/health` | Returns health status and UTC timestamp |
| GET | `/info` | Returns application information |
| GET | `/docs` | Opens interactive Swagger documentation |

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Salman-747/cloud-status-api.git
cd cloud-status-api
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn main:app --reload
```

Open these URLs in your browser:

- API: http://localhost:8000/
- Health check: http://localhost:8000/health
- Interactive documentation: http://localhost:8000/docs

## Run Automated Tests

With the virtual environment activated, run:

```bash
python -m pytest -v
```

The tests verify the main endpoints and the expected 404 response for an unknown endpoint.

## Run with Docker

### 1. Build the image

```bash
docker build -t cloud-status-api:1.0 .
```

### 2. Run the container

```bash
docker run --rm -d \
  --name cloud-status-container \
  -p 8001:8000 \
  cloud-status-api:1.0
```

Port `8001` is used on the host to avoid conflicts with a local development server that may already use port `8000`. The container listens on port `8000`.

### 3. Verify the application

- Health check: http://localhost:8001/health
- API documentation: http://localhost:8001/docs

### 4. View logs and stop the container

```bash
docker logs cloud-status-container
docker stop cloud-status-container
```

## Continuous Integration

The GitHub Actions workflow in `.github/workflows/ci.yml` runs when code is pushed to the `main` branch or a pull request targets `main`.

It performs two jobs:

1. Installs Python dependencies and runs automated tests.
2. Builds the Docker image to verify that the application can be packaged.

## Learning Objectives

This project provides hands-on experience with REST APIs, HTTP status codes, automated testing, Git workflows, CI pipelines, Docker images, containers, port mapping, and application logs.

## Future Improvements

- Deploy the container to Microsoft Azure.
- Add application configuration using environment variables.
- Introduce structured logging and monitoring.
- Add a deployment pipeline and production health checks.

## Author

Built as a cloud and DevOps portfolio project.
