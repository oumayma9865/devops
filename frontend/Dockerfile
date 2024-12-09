# Choisir l'image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier tous les fichiers de votre projet dans le conteneur
COPY . /app/

# Installer Streamlit et d'autres dépendances nécessaires
RUN pip install --no-cache-dir streamlit

# Exposer le port 3000 pour Streamlit
EXPOSE 3000


CMD ["streamlit", "run", "app.py"]
