pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                pwd()
                bash 'apt update'
                sh 'python3 --version'
                sh 'pip install pycodestyle'
                sh './pycheck'
            }
        }
    }
}
