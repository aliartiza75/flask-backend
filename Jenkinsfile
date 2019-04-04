pipeline {
    agent {
        docker { image 'python:3.6-jessie' }
    }
    stages {
        stage('build') {
            steps {
                sh 'sudo pip3 install pycodestyle'
                sh './pycheck'
            }
        }
    }
}
