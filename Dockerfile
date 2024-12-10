FROM jenkins/jenkins:lts

# Passer en utilisateur root
USER root

# Installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common \
    lsb-release

# Ajouter le dépôt Docker pour Debian Bullseye
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update

# Installer Docker CLI avec une version spécifique
RUN apt-get install -y docker-ce-cli=5:20.10.12~3-0~debian-bullseye

# Installer Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" \
    -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose

# Ajouter l'utilisateur Jenkins au groupe Docker
RUN groupadd docker && usermod -aG docker jenkins

# Créer un lien symbolique pour le socket Docker si nécessaire
RUN ln -s /var/run/docker.sock /tmp/docker.sock

# Revenir à l'utilisateur Jenkins
USER jenkins
