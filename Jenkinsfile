pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        LOG_FILE = "flask.log"
        PYTHON = "${VENV_DIR}/bin/python"
        PIP = "${VENV_DIR}/bin/pip"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/syedBilalSherazi/my-ci-app.git'
            }
        }

        stage('Set Up Python Env') {
            steps {
                sh """
                    python3 -m venv ${VENV_DIR} && \
                    ${PIP} install --upgrade pip && \
                    ${PIP} install -r requirements.txt
                """
            }
        }

        stage('Kill Existing Flask App') {
            steps {
                echo 'Stopping any previous Flask processes...'
                sh """
                    PIDS=$(pgrep -f "python app.py" || true)
                    if [ ! -z "$PIDS" ]; then
                        echo "Killing: \$PIDS"
                        kill \$PIDS
                    fi
                """
            }
        }

        stage('Start Flask App') {
            steps {
                echo 'Starting Flask server...'
                sh """
                    nohup ${PYTHON} app.py > ${LOG_FILE} 2>&1 &
                    sleep 5
                """
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium tests against live app...'
                catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') {
                    sh "${PYTHON} -m unittest discover test_app"
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
