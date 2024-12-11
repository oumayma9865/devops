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
         stage('Remove .dockerignore') {
            steps {
                echo '### Vérification et suppression de .dockerignore ###'
                sh '''
                if [ -f .dockerignore ]; then
                    echo "Suppression du fichier .dockerignore..."
                    rm -f .dockerignore
                fi
                '''
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

      //  stage('Run Tests') {
       //     steps {
       //          sh 'docker-compose down --remove-orphans'
        //         sh 'docker-compose up -d'
        //         sh 'docker exec devops-project_frontend_1  pytest /app/test_frontend.py'
       //          sh 'docker exec devops-project_vgg19_service_1   pytest /app/test_vgg_service.py'
       //          sh 'docker exec devops-project_svm_service_1   pytest /app/test_svm_service.py'
               
        //     }
       //  } 

        stage('Push Docker Images') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        sh "docker tag svm_service ${DOCKER_REGISTRY}/svm_service:latest"
                        sh "docker push ${DOCKER_REGISTRY}/svm_service:latest"

                        sh "docker tag vgg19_service ${DOCKER_REGISTRY}/vgg19_service:latest"
                        sh "docker push ${DOCKER_REGISTRY}/vgg19_service:latest"

                        sh "docker tag frontend ${DOCKER_REGISTRY}/frontend:latest"
                        sh "docker push ${DOCKER_REGISTRY}/frontend:latest"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying services...'
               
                sh 'docker-compose down'
                sh 'docker-compose up '
                
                echo 'Deployment completed!'
            }
        }
    }
}
