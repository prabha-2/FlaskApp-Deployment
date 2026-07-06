# 🚀 CI/CD Pipeline for Flask Application Deployment on AWS

## 📖 Overview

This project demonstrates an end-to-end CI/CD pipeline for deploying a Dockerized Flask application on AWS.

Whenever code is pushed to the `main` branch, GitHub Actions automatically:

- Builds the Docker image
- Pushes the image to Amazon ECR
- Connects to an Amazon EC2 instance via SSH
- Pulls the latest image
- Replaces the running container with the updated version

This project helped me gain practical experience with modern DevOps deployment workflows and cloud infrastructure automation.

---

# 🏗 Architecture

```
Developer
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Actions
     │
     ├─────────────► Build Docker Image
     │
     ├─────────────► Push Image to Amazon ECR
     │
     ▼
SSH into Amazon EC2
     │
     ▼
Pull Latest Docker Image
     │
     ▼
Stop Existing Container
     │
     ▼
Run Updated Container
     │
     ▼
Users Access Flask Application
```

---

# 🛠 Technologies Used

- Python
- Flask
- Docker
- GitHub Actions
- Amazon EC2
- Amazon ECR
- AWS CLI
- Ubuntu Linux
- SSH
- Git

---

# ☁️ AWS Services

- Amazon EC2
- Amazon ECR
- IAM
- AWS CLI

---

# ⚙ CI/CD Workflow

The GitHub Actions workflow performs the following steps automatically:

1. Checkout source code
2. Set up Python
3. Install project dependencies
4. Configure AWS credentials
5. Authenticate with Amazon ECR
6. Build Docker image
7. Tag Docker image
8. Push Docker image to Amazon ECR
9. Connect to EC2 using SSH
10. Pull latest Docker image
11. Stop existing container
12. Remove old container
13. Start updated container

---

# 🔄 Deployment Flow

```
Git Push
    │
    ▼
GitHub Actions
    │
    ▼
Docker Build
    │
    ▼
Amazon ECR
    │
    ▼
SSH Deployment
    │
    ▼
Amazon EC2
    │
    ▼
Docker Container
    │
    ▼
Flask Application
```

---

# 🔐 GitHub Secrets Used

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION
- AWS_ACCOUNT_ID
- REPO_NAME
- EC2_HOST
- EC2_SSH_KEY

---

# 📚 What I Learned

During this project I gained hands-on experience with:

- Designing CI/CD pipelines using GitHub Actions
- Containerizing Python applications with Docker
- Working with Amazon ECR
- Deploying containers on Amazon EC2
- Managing Docker containers remotely
- Configuring GitHub Secrets
- Automating deployments after every code push
- Troubleshooting deployment failures

---

# 🚧 Challenges Faced

Some issues encountered while implementing the pipeline included:

- Docker image build failures
- GitHub Actions workflow configuration
- AWS authentication
- Amazon ECR login
- SSH deployment issues
- Container startup failures
- Incorrect application paths inside the container

Resolving these issues helped me better understand CI/CD automation and Docker-based deployments.

---

# 🎯 Skills Demonstrated

- GitHub Actions
- CI/CD
- Docker
- AWS
- Amazon EC2
- Amazon ECR
- Linux
- SSH
- Python
- Flask
- DevOps

---

# 📌 Project Outcome

Successfully implemented an automated deployment pipeline where every push to the `main` branch triggers a complete build, containerization, image publishing, and deployment process on AWS without manual intervention.
