import requests

def test_svm_valid_audio():
    url = "http://localhost:5000"  # URL du service SVM
    files = {'file': open('temps_audio_file.wav', 'rb')}  # Remplacer par un fichier audio valide
    response = requests.post(url, files=files)

    assert response.status_code == 200, "Erreur dans le service SVM"
    assert "Le genre de musique prédit est" in response.text, "Réponse incorrecte pour audio valide"

def test_svm_invalid_audio():
    url = "http://localhost:5000"
    files = {'file': open('test_frontend.py', 'rb')}  # Fichier corrompu ou non supporté
    response = requests.post(url, files=files)

    assert response.status_code != 200, "Le service SVM a accepté un fichier invalide"
    assert "Erreur" in response.text, "Le service SVM n'a pas retourné d'erreur pour fichier invalide"

def test_svm_no_audio():
    url = "http://localhost:5000"
    response = requests.post(url)

    assert response.status_code == 400, "Le service SVM n'a pas retourné une erreur pour l'absence de fichier"
    assert "Veuillez charger un fichier audio" in response.text, "Le message d'erreur n'est pas correct"
