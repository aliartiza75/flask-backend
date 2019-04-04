pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'lsb_release -a'
                sh 'python3 --version'
                sh 'pip install pycodestyle'
                sh './pycheck'
            }
        }
    }
}
