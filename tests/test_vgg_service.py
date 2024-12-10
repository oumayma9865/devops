import requests

def test_vgg_valid_audio():
    url = "http://localhost:5001"  # URL du service VGG
    files = {'file': open('valid_audio.wav', 'rb')}  # Remplacer par un fichier audio valide
    response = requests.post(url, files=files)

    assert response.status_code == 200, "Erreur dans le service VGG"
    assert "Le genre de musique prédit est" in response.text, "Réponse incorrecte pour audio valide"

def test_vgg_invalid_audio():
    url = "http://localhost:5001"
    files = {'file': open('invalid_audio.xyz', 'rb')}  # Fichier corrompu ou non supporté
    response = requests.post(url, files=files)

    assert response.status_code != 200, "Le service VGG a accepté un fichier invalide"
    assert "Erreur" in response.text, "Le service VGG n'a pas retourné d'erreur pour fichier invalide"

def test_vgg_no_audio():
    url = "http://localhost:5001"
    response = requests.post(url)

    assert response.status_code == 400, "Le service VGG n'a pas retourné une erreur pour l'absence de fichier"
    assert "Veuillez charger un fichier audio" in response.text, "Le message d'erreur n'est pas correct"

def test_vgg_prediction_time():
    url = "http://localhost:5001"
    files = {'file': open('valid_audio.wav', 'rb')}  # Fichier audio valide
    
    import time
    start_time = time.time()
    response = requests.post(url, files=files)
    elapsed_time = time.time() - start_time

    assert elapsed_time < 2, f"Temps de prédiction trop long : {elapsed_time} secondes"
    assert response.status_code == 200, "Erreur lors de la prédiction"
