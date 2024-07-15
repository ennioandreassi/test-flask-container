pipeline {
    agent any


    parameters {
        string(name: 'GIT_URL', defaultValue: 'https://github.com/ennioandreassi/test-flask-container')
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
        stage('Check container running'){
            steps {
                script {
                def container = sh(script: 'docker ps | grep flask-container', returnStdout: true).trim()
                if(container.contains('flask-container')){
                    sh 'docker stop flask-container'
                }
                def container_stop = sh(script: 'docker ps -a | grep flask-container', returnStdout: true).trim()
                if(container_stop != ''){
                    sh 'docker rm flask-container'
                }
            }
        }
    }
        stage('Build docker image'){
            steps {
                sh ' docker build -t flask-container .'
            }
        }
        stage('Run docker container'){
            steps {
                sh ' docker run -d -p 5000:5000 --name flask-container flask-container'
            }
        }
        stage('Delay'){
            steps {
                script {
                    sleep(7)
                }
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
