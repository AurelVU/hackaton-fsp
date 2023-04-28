node("master") {
    stage("Checkout") {
        git 'https://github.com/chalex2k/hackaton.git'
        sshagent(['ssh-vm']) {
            sh 'scp -o StrictHostKeyChecking=no docker-compose.yaml hackaton_user@51.250.16.186:/home/hackaton_user/hackaton/docker-compose.yaml'
        }
    }

    stage("Compose") {
        sshagent(['ssh-vm']) {
            sh 'ssh -o StrictHostKeyChecking=no hackaton_user@51.250.16.186 docker-compose -f /home/hackaton_user/hackaton/docker-compose.yaml up --build -d'
        }
    }
}