pipeline {
    agent any

    stages {
        stage('clean ws') {
            steps {
                cleanWs()
        }
        }
        stage('Git checkout'){
            steps {
                checkout scmGit(branches: [[name: '*/main']], 
                extensions: [], 
                userRemoteConfigs: [[url: 'https://github.com/ennioandreassi/test-flask-container']])
            }
        }
        stage('Build docker image'){
            steps {
                sh ' docker build -t flask-container .'
            }
        }
        stage('Run docker container'){
            steps {
                sh ' docker run -d -p 5000:5000 flask-container'
            }
        }
        stage('test connection'){
            steps {
                sh 'curl http://localhost:5000'
            }
        }
        stage('clean ws final'){
            steps {
                cleanWs()
            }
        }
    }
}

