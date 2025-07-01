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

        stage('Set Up Python Env') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Start Flask App') {
            steps {
                sh '''
                    source ${VENV_DIR}/bin/activate
                    nohup python app.py > flask.log 2>&1 &
                    sleep 5
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    source ${VENV_DIR}/bin/activate
                    sh 'python -m unittest discover test_app'
                '''
            }
        }

        stage('Archive Results') {
            steps {
                junit 'report.xml'
                archiveArtifacts artifacts: 'flask.log', onlyIfSuccessful: false
            }
        }
    }

    post {
        success {
            mail to: 'syedbilalsherazi1004@gmail.com',
                 subject: "✅ Jenkins Build Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: """Good news! The build succeeded.

Job: ${env.JOB_NAME}
Build: ${env.BUILD_NUMBER}
URL: ${env.BUILD_URL}"""
        }
        failure {
            mail to: 'syedbilalsherazi1004@gmail.com',
                 subject: "❌ Jenkins Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: """The build failed.

Job: ${env.JOB_NAME}
Build: ${env.BUILD_NUMBER}
URL: ${env.BUILD_URL}"""
        }
    }
}
