pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Cloner le code') {
            steps {
                git 'https://github.com/Herimanda/Grid.git' // ou utilise SCM config dans l'interface Jenkins
            }
        }

        stage('Installer les dépendances') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Lancer les tests') {
            steps {
                sh './venv/bin/pytest'
            }
        }

        stage('Build Docker (optionnel)') {
            steps {
                script {
                    // si Docker installé sur l’agent Jenkins
                    sh 'docker build -t flask-backend-ci .'
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline terminé"
        }
        failure {
            echo "Quelque chose a échoué !"
        }
    }
}
