import streamlit as st
import librosa
import numpy as np
import joblib
model = joblib.load('/app/svmodel.pkl')
st.title("Prédiction du genre de musique avec 'SVM'")

audio_file = st.file_uploader("Charger un fichier audio", type=["wav", "mp3"])

if audio_file is not None:
    with open("temp_audio_file", "wb") as f:
        f.write(audio_file.getbuffer())
    y, sr = librosa.load("temp_audio_file", sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=58)
    mfccs_mean = np.mean(mfccs, axis=1)
    input_data = mfccs_mean.reshape(1, -1)
    prediction = model.predict(input_data)
    st.write(f"Le genre de musique prédite est : {prediction[0]}")
else:
    st.write("Veuillez charger un fichier audio.")