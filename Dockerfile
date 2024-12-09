# Étape 1 : Utiliser l'image officielle de Jenkins LTS
FROM jenkins/jenkins:lts

# Étape 2 : Installer Docker et Docker Compose
USER root  # Passer en utilisateur root pour avoir les permissions nécessaires

# Installer Docker CLI
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y docker-ce-cli

# Installer Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Vérifier les installations
RUN docker --version && docker-compose --version

# Retourner à l'utilisateur Jenkins par défaut
USER jenkins
