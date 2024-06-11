pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'mishiklakus/kursova'
        MY_TG_BOT_TOKEN =  credentials('tg_bot_token')

    }
    stages {
        stage('Start') {
            steps {
                echo 'Cursova_Bot: nginx/custom'
            }
        }

        stage('Build nginx/custom') {
            steps {
                sh 'export MY_TG_BOT_TOKEN=$MY_TG_BOT_TOKEN' 
                sh 'docker-compose build'
                sh 'docker tag $DOCKER_IMAGE:latest $DOCKER_IMAGE:$BUILD_NUMBER'
            }
            post {
                failure {
                    script {
                        telegramSend message: "Job Name: ${env.JOB_NAME}\nBranch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}\nFailure stage: '${env.STAGE_NAME}'"
                    }
                }
            }
        }

        stage('Test nginx/custom') {
            steps {
                echo 'Pass'
            }
            post {
                failure {
                    script {
                        telegramSend message: "Job Name: ${env.JOB_NAME}\nBranch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}\nFailure stage: '${env.STAGE_NAME}'"
                    }
                }
            }
        }

        stage('Deploy nginx/custom') {
            steps {
                sh "docker-compose down"
                sh "docker container prune --force"
                sh "docker image prune --force"
                sh "docker-compose up -d --build"
            }
            post {
                failure {
                    script {
                        telegramSend message: "Job Name: ${env.JOB_NAME}\nBranch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}\nFailure stage: '${env.STAGE_NAME}'"
                    }
                }
            }
        }
    }

    post {
        success {
            script {
                telegramSend message: "Job Name: ${env.JOB_NAME}\nBranch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}"
            }
        }
        failure {
            script {
                telegramSend message: "Job Name: ${env.JOB_NAME}\nBranch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}"
            }
        }
    }
}
