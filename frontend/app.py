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

model_choice = st.selectbox("Choisissez le modèle :", ["SVM", "VGG"])

if st.button("Aller au modèle sélectionné"):
    if model_choice == "SVM":
        os.system("streamlit run ./svm_service/svm_service.py")
    else:
        os.system("streamlit run ./vgg_service/vgg_service.py")
