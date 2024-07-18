pipeline {
    agent any


    parameters {
        string(name: 'GIT_URL', defaultValue: 'https://github.com/ennioandreassi/test-flask-container')
        string(name: 'GIT_BRANCH', defaultValue: '*/main')
        string(name: 'NAME_RELEASE', defaultValue: 'flask-project')
        string(name: 'NAME_CHART', defaultValue: 'flask')
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
        stage('Check chart exists'){
            steps {
                script {
                    if (fileExists("/root/${params.NAME_CHART}")) {
                        echo 'Chart exists'
                    } else {
                        echo 'Chart does not exist'
                        sh "cd /helm ; helm create ${params.NAME_CHART}"
                    }
                }
            }
        }
        stage('Update values.yaml'){
            steps {
                script {
                    sh "echo \"image: flask-container\" > /helm/${params.NAME_CHART}/values.yaml"
                }
            }
        }
        stage('Build docker image'){
            steps {
                sh ' docker build -t flask-container .'
            }
        }
        stage('Run chart'){
            steps {
                sh "cd /helm ; sudo helm upgrade --install ${params.NAME_RELEASE} ${params.NAME_CHART}"
            }
        }
        stage('Delay'){
            steps {
                script {
                    sleep(15)
                }
            }
        }
        stage('test pod'){
            steps {
                script {
                    list_pod = sh(script: 'kubectl get pods | grep flask-project | awk \'{print $1}\'', returnStdout: true).trim()
                    if (list_pod.contains('flask')) {
                        echo 'Pod exists'
                    } else {
                        echo 'Pod does not exist'
                    }
                }
            }
        }
        stage('clean ws final'){
            steps {
                cleanWs()
            }
        }
    }
}
