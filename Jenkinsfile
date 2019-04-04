pipeline {
    agent {
        docker { image 'python:3.6-jessie' }
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
