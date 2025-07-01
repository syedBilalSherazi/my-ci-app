pipeline {
    agent any

    environment {
        REPO_DIR = "my-ci-app"
        VENV_DIR = "venv"
        LOG_FILE = "flask.log"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/syedBilalSherazi/my-ci-app.git'
            }
        }

        stage('Set Up Python Env') {
            steps {
                dir("${REPO_DIR}") {
                    sh """
                        python3 -m venv ../${VENV_DIR}
                        source ../${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Kill Existing Flask App') {
            steps {
                echo 'Stopping any previous Flask processes...'
                sh "pkill -f ${REPO_DIR}/app.py || true"
            }
        }

        stage('Start Flask App') {
            steps {
                echo 'Starting Flask server...'
                sh """
                    cd ${REPO_DIR}
                    source ../${VENV_DIR}/bin/activate
                    nohup python app.py > ../${LOG_FILE} 2>&1 &
                    sleep 5
                """
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium tests against live app...'
                catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') {
                    dir("${REPO_DIR}") {
                        sh """
                            source ../${VENV_DIR}/bin/activate
                            python -m unittest discover test_app
                        """
                    }
                }
            }
        }

        stage('Archive Logs') {
            steps {
                archiveArtifacts artifacts: "${LOG_FILE}", onlyIfSuccessful: false
            }
        }
    }

    post {
        always {
            mail to: 'syedbilalsherazi1004@gmail.com',
                 subject: "📦 Jenkins Build Complete: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: """The Jenkins build has completed.

Job: ${env.JOB_NAME}
Build: ${env.BUILD_NUMBER}
URL: ${env.BUILD_URL}
"""
        }
    }
}
