pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install --upgrade pip'
                    sh 'pip install --user -r requirements.txt'
                }
                echo "Hallo"
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                python3 main.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
