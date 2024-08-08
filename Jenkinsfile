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
                    def chartExists = sh(script: "helm list -q | grep -w ${params.NAME_CHART}", returnStatus: true) == 0
                    if (chartExists) {
                        echo 'Chart exists'
                    } else {
                        echo 'Chart does not exist'
                        sh "cd /helm ; helm create ${params.NAME_CHART}"
                    }
                }
            }

        }
        stage('Update values.yaml') {
            steps {
                script {
                    writeFile file: "/helm/${params.NAME_CHART}/values.yaml", text: """
                    replicaCount: 3
                    image:
                      repository: ennioandreassi88/flask-container
                      tag: latest
                    service:
                      type: NodePort
                      nodePort: 30007
                    """
                }
            }
        }
        stage('Build docker image'){
            steps {
                sh ' docker build -t flask-container .'
            }
        }
        stage('Push docker image'){
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login --username $DOCKER_USERNAME --password-stdin'
                        sh 'docker tag flask-container ennioandreassi88/flask-container'
                        sh 'docker push ennioandreassi88/flask-container'
                    }
                }
            }
        }
        stage('Run chart'){
            steps {
                sh "cd /helm ; sudo /usr/local/bin/helm upgrade --install ${params.NAME_RELEASE} ${params.NAME_CHART} --kubeconfig /home/helm/.kube/config"
            }
        }
        stage('Delay'){
            steps {
                script {
                    sleep(7)
                }
            }
        }
        stage('test pod'){
            steps {
                script {
                    list_pod = sh(script: 'sudo kubectl get pods --kubeconfig /home/helm/.kube/config| grep flask-project | awk \'{print $1}\'', returnStdout: true).trim()
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
