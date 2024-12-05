import streamlit as st
import os


st.markdown(
    """
    <style>
    .main {
        background-image: url("R.jpg");
        background-size: cover;
        background-position: center;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Classification du Genre Musical")

# Sélection du modèle
model_choice = st.selectbox("Choisissez le modèle :", ["SVM", "VGG"])

# Lancer le modèle choisi
if st.button("Aller au modèle sélectionné"):
    if model_choice == "SVM":
        os.system(f"streamlit run /app/svm_service/svm_service.py")
        
    elif model_choice == "VGG":
        os.system(f"streamlit run /app/vgg_service/vgg_service.py")
        