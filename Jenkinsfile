pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pwd'
                sh 'pip install pycodestyle'
                sh './pycheck'
            }
        }
    }
}
