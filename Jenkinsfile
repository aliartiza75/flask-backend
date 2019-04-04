pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'sudo pip3 install pycodestyle'
                sh './pycheck'
            }
        }
    }
}
