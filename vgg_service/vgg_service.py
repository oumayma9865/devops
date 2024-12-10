import streamlit as st
import librosa
import numpy as np
import joblib
import tensorflow as tf

model = tf.keras.models.load_model('/app/vgg_service/vgg_genre_model.h5')
label_encoder = joblib.load('/app/vgg_service/label_encoder.pkl')

st.title("Prédiction du genre de musique avec 'VGG'")

audio_file = st.file_uploader("Charger un fichier audio", type=["wav", "mp3"])
if audio_file is not None:
    with open("temp_audio_file.wav", "wb") as f:
        f.write(audio_file.getbuffer())

    y, sr = librosa.load("temp_audio_file.wav", sr=None)

    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
    S_db = librosa.power_to_db(S, ref=np.max)

    try:
        input_data = np.resize(S_db, (224, 224, 1))  
        input_data = np.repeat(input_data, 3, axis=-1) 
        input_data = tf.image.resize(input_data, (224, 224))  
        input_data = input_data.numpy()

        input_data = input_data.astype('float32') / 255.0


    except ValueError:
        st.write("Erreur : Les dimensions des spectrogrammes ne correspondent pas à l'entrée attendue du modèle.")
        st.stop()

    prediction = model.predict(input_data.reshape(1, 224, 224, 3))  
    predicted_label_index = np.argmax(prediction, axis=1)
    predicted_genre = label_encoder.inverse_transform(predicted_label_index)
    
    st.write(f"Le genre de musique prédit est : {predicted_genre[0]}")