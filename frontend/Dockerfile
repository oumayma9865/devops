# Choisir l'image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier tous les fichiers de votre projet dans le conteneur
COPY . /app/
COPY ./tests/test_frontend.py /app/test_frontend.py
RUN pip install -r /app/requirements.txt

# Exposer le port 3000 pour Streamlit
EXPOSE 3000


CMD ["streamlit", "run", "/app/app.py"]
