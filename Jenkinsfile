pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pwd'
                sh 'python3 --version'
                sh 'pip install pycodestyle'
                sh './pycheck'
            }
        }
    }
}
