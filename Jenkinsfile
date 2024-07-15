pipeline {
    agent any


    parameters {
        string(name: 'GIT_URL', defaultValue: 'https://github.com/ennioandreassi/test-flask-container'),
        string(name: 'GIT_BRANCH', defaultValue: '*/main')
    }
    
    stages {
        stage('clean ws') {
            steps {
                cleanWs()
        }
        }
        stage('Git checkout'){
            steps {
                checkout scmGit(branches: [[name: params.GIT_BRANCH]], 
                extensions: [], 
                userRemoteConfigs: [[url: params.GIT_URL]])
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
