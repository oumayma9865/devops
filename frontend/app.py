import streamlit as st

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

# Bouton pour aller au modèle sélectionné
if st.button("Aller au modèle sélectionné"):
    if model_choice == "SVM":
        st.markdown('<meta http-equiv="refresh" content="0;URL=http://localhost:5000">', unsafe_allow_html=True)
    elif model_choice == "VGG":
        st.markdown('<meta http-equiv="refresh" content="0;URL=http://localhost:5001">', unsafe_allow_html=True)
