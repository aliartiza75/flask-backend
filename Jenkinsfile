pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'apt update'
                sh 'python3 --version'
                sh 'pip install pycodestyle'
                sh './pycheck'
            }
        }
    }
}
