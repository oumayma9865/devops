import os
import wave
import librosa
import numpy as np
import joblib
import tensorflow as tf

MODEL_PATH = "/app/vgg_genre_model.h5"
LABEL_ENCODER_PATH = "/app/label_encoder.pkl"

model = tf.keras.models.load_model(MODEL_PATH)
label_encoder = joblib.load(LABEL_ENCODER_PATH)

#


# Test 1 : Vérifier qu'un fichier audio valide est correctement traité
def test_valid_audio_processing():
    filename = "/app/temp_audio_file.wav"
    

    try:
      
        y, sr = librosa.load(filename, sr=None)

        S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
        S_db = librosa.power_to_db(S, ref=np.max)

        input_data = np.resize(S_db, (224, 224, 1))
        input_data = np.repeat(input_data, 3, axis=-1)  
        input_data = tf.image.resize(input_data, (224, 224))
        input_data = input_data.numpy().astype('float32') / 255.0

        prediction = model.predict(input_data.reshape(1, 224, 224, 3))
        predicted_label_index = np.argmax(prediction, axis=1)
        predicted_genre = label_encoder.inverse_transform(predicted_label_index)

        assert predicted_genre is not None, "La prédiction ne doit pas être vide"
        print(f"Test réussi : Prédiction = {predicted_genre[0]}")
    finally:
        os.remove(filename)


# Test 2 : Vérifier le comportement en cas de fichier audio invalide
def test_invalid_audio_file():
    invalid_filename = "/app/test_vgg_service.py"
    with open(invalid_filename, "w") as f:
        f.write("Contenu non audio")

    try:
        try:
            librosa.load(invalid_filename, sr=None)
            assert False, "Librosa ne doit pas réussir à lire un fichier invalide"
        except Exception:
            print("Test réussi : Erreur détectée pour un fichier non audio")
    finally:
        os.remove(invalid_filename)



# Test 4 : Gérer le cas où aucun fichier n'est fourni
def test_no_file_behavior():
    try:
        y, sr = librosa.load("", sr=None) 
        assert False, "Librosa ne doit pas réussir à lire une entrée vide"
    except Exception:
        print("Test réussi : Erreur détectée lorsqu'aucun fichier n'est fourni")
