pipeline {
    agent any

    environment {
        VENV = 'venv'
        COVERAGE_FILE = 'coverage.xml'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python manage.py migrate --noinput
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    coverage run --source='.' manage.py test
                    coverage xml -o ${COVERAGE_FILE}
                '''
            }
        }

        stage('Run BDD Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    behave features/
                '''
            }
        }

        stage('Archive & Report') {
            steps {
                junit 'reports/*.xml'
                publishCoverage adapters: [coberturaAdapter('${COVERAGE_FILE}')], sourceFileResolver: sourceFiles('NEVER_STORE')
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo '✅ Pipeline finished successfully!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}
