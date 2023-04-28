node("master") {
    stage("Checkout") {
        sshagent(['ssh-vm']) {
            sh 'ssh -o StrictHostKeyChecking=no hackaton_user@51.250.16.186 rm -rf /home/hackaton_user/hackaton-fsp'

            sh 'ssh -o StrictHostKeyChecking=no hackaton_user@51.250.16.186 git clone https://github.com/AurelVU/hackaton-fsp.git'

        }
    }

    stage("Compose") {
        sshagent(['ssh-vm']) {
            sh 'ssh -o StrictHostKeyChecking=no hackaton_user@51.250.16.186 docker-compose -f /home/hackaton_user/hackaton-fsp/docker-compose.yaml up --build -d'
        }
    }
}