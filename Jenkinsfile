pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
        stage('Build') {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
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
