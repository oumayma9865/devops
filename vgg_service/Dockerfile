# Utiliser l'image de base Python 3.9
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier de service dans le conteneur
COPY vgg_service.py /app/

# Mettre à jour pip et installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    libhdf5-dev \
    libatlas-base-dev \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    libcurl4-openssl-dev \
    libssl-dev

# Mettre à jour pip et installer les dépendances Python nécessaires
RUN pip install --upgrade pip
RUN pip install --no-cache-dir streamlit librosa numpy tensorflow-cpu==2.9.1 scikit-learn==1.4.2 joblib

# Définir la variable d'environnement pour désactiver CUDA (utilisation CPU uniquement)
ENV CUDA_VISIBLE_DEVICES="-1"

# Exposer le port pour le serveur Streamlit
EXPOSE 5001

# Lancer l'application Streamlit
CMD ["streamlit", "run", "vgg_service.py", "--server.address=0.0.0.0", "--server.port=5001", "--server.enableCORS=false"]
