pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pip3 install pycodestyle'
                sh './pycheck'
            }
        }
    }
}
