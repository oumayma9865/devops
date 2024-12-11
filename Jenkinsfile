pipeline {
    agent any
    environment {
        DOCKER_REGISTRY = 'benhleloumayma/devops-project'
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
            post {
                always {
                    echo 'Build stage completed.'
                }
                failure {
                    echo 'Error during Build stage. Check the logs for details.'
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker-compose down --remove-orphans'
                sh 'docker-compose up -d'
              //  sh 'docker exec devops-project_vgg19_service_1 pytest /app/test_vgg_service.py --junitxml=/app/results/vgg_results.xml'
                sh 'docker exec devops-project_svm_service_1 pytest /app/test_svm_service.py --junitxml=/app/results/svm_results.xml' 
                  
            }
            post {
                always {
                    echo 'Test stage completed.'
                }
                success {
                    echo 'Tests passed successfully.'
                }
                failure {
                    echo 'Tests failed. Check the test logs and results.'
                }
            }
        }

        stage('Archive Test Results') {
            steps {
                archiveArtifacts artifacts: '**/results/*.xml', allowEmptyArchive: true
                junit '**/results/*.xml'
            }
            post {
                always {
                    echo 'Test results archived.'
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        sh "docker tag devops-project_svm_service:latest ${DOCKER_REGISTRY}/svm_service:latest"
                        sh "docker push ${DOCKER_REGISTRY}/svm_service:latest"

                        sh "docker tag devops-project_vgg19_service:latest ${DOCKER_REGISTRY}/vgg19_service:latest"
                        sh "docker push ${DOCKER_REGISTRY}/vgg19_service:latest"

                        sh "docker tag devops-project_frontend:latest ${DOCKER_REGISTRY}/frontend:latest"
                        sh "docker push ${DOCKER_REGISTRY}/frontend:latest"
                    }
                }
            }
            post {
                always {
                    echo 'Push Docker Images stage completed.'
                }
                success {
                    echo 'Docker images pushed successfully.'
                }
                failure {
                    echo 'Failed to push Docker images. Verify Docker registry credentials and image tagging.'
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
            post {
                always {
                    echo 'Deploy stage completed.'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        failure {
            echo 'Pipeline failed. Check the logs for issues.'
        }
        success {
            echo 'Pipeline executed successfully!'
        }
    }
}
