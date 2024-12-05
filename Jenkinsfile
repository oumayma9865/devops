pipeline {
    agent any
    environment {
        DOCKER_REGISTRY = "${params.DOCKER_REGISTRY}" 
        REPO = "${params.REPO}"  
    }
     
    stages {
        stage('Checkout') {
            steps {
                script {
                    sh 'git config --global http.postBuffer 524288000'
                }
                checkout scm
            }
        }
        stage('Clone Repository') {
            steps {
                git url: "${params.REPO}", branch: 'main'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker-compose up -d'
                sh 'docker exec svm_service pytest /tests/test.py'
               
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        sh "docker tag svm_service ${DOCKER_REGISTRY}/svm_service:latest"
                        sh "docker push ${DOCKER_REGISTRY}/svm_service:latest"

                        sh "docker tag vgg19_service ${DOCKER_REGISTRY}/vgg19_service:latest"
                        sh "docker push ${DOCKER_REGISTRY}/vgg19_service:latest"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying services...'
               
                sh 'docker-compose down'
                sh 'docker-compose up -d'
                
                echo 'Deployment completed!'
            }
        }
    }
}
