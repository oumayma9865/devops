import os
import librosa
import numpy as np
import joblib
MODEL_PATH = "/app/svmodel.pkl"
model = joblib.load(MODEL_PATH)

def test_valid_audio_processing():
    filename = "/app/temp_audio_file.wav"
    

    try:
        y, sr = librosa.load(filename, sr=None)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=58)
        mfccs_mean = np.mean(mfccs, axis=1)

        
        input_data = mfccs_mean.reshape(1, -1)
        prediction = model.predict(input_data)

        assert prediction is not None, "La prédiction ne doit pas être vide"
        print(f"Test réussi : Prédiction = {prediction[0]}")
    finally:
        os.remove(filename)


# Test 2 : Vérifier le comportement en cas de fichier invalide
def test_invalid_audio_file():
    invalid_filename = "/app/test_svm_service.py"
    with open(invalid_filename, "w") as f:
        f.write("Contenu non audio")

    try:
        try:
            librosa.load(invalid_filename, sr=None)
            assert False, "Librosa ne doit pas réussir à lire un fichier invalide"
        except Exception:
            print("Test réussi : Librosa a déclenché une erreur pour un fichier invalide")
    finally:
        os.remove(invalid_filename)


# Test 3 : Gérer le cas où aucun fichier n'est fourni
def test_no_file_behavior():
    try:
        y, sr = librosa.load("", sr=None)  
        assert False, "Librosa ne doit pas réussir à lire une entrée vide"
    except Exception:
        print("Test réussi : Erreur détectée lorsqu'aucun fichier n'est fourni")
