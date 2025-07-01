pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/syedBilalSherazi/my-ci-app.git'
            }
        }

        stage('Install Requirements') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source ${VENV_DIR}/bin/activate
                    pytest --junitxml=report.xml
                '''
            }
        }

        stage('Archive Results') {
            steps {
                junit 'report.xml'
            }
        }
    }

    post {
        success {
            mail to: 'syedbilalsherazi1004@gmail.com',
                 subject: "Jenkins Build Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Good news! The build succeeded.\n\nJob: ${env.JOB_NAME}\nBuild: ${env.BUILD_NUMBER}\nURL: ${env.BUILD_URL}"
        }
        failure {
            mail to: 'syedbilalsherazi1004@gmail.com',
                 subject: "Jenkins Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The build failed.\n\nJob: ${env.JOB_NAME}\nBuild: ${env.BUILD_NUMBER}\nURL: ${env.BUILD_URL}"
        }
    }
}
