import pytest
import streamlit as st
from unittest.mock import patch
import os


def test_app_title():
    with patch("streamlit.title") as mock_title:
        st.title("Classification du Genre Musical")
        
        mock_title.assert_called_with("Classification du Genre Musical")


def test_model_selection():
    with patch("streamlit.selectbox") as mock_selectbox, patch("streamlit.button") as mock_button, patch("os.system") as mock_system:
        
        mock_selectbox.return_value = "SVM"
        
        mock_button.return_value = True

       
        model_choice = st.selectbox("Choisissez le modèle :", ["SVM", "VGG"])
        if st.button("Aller au modèle sélectionné"):
            if model_choice == "SVM":
                os.system("streamlit run ./svm_service/svm_service.py")
            else:
                os.system("streamlit run ./vgg_service/vgg_service.py")

       
        mock_system.assert_called_with("streamlit run ./svm_service/svm_service.py")


def test_background_image():
    with patch("streamlit.markdown") as mock_markdown:
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
      
        mock_markdown.assert_called_once_with(
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
