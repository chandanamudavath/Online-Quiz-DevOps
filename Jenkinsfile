pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Chandana\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pip install -r requirements-dev.txt'
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat '"C:\\Users\\Chandana\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pytest tests -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t online-quiz:latest .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl get services'
            }
        }
    }
}