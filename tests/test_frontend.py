from selenium import webdriver
from selenium.webdriver.common.by import By

def test_homepage():
    driver = webdriver.Chrome()  # Ou un autre navigateur
    driver.get("http://localhost:8501")  # URL de l'application Streamlit

    # Vérifier que la page charge bien
    assert "Classification du Genre Musical" in driver.title

    # Sélectionner un modèle
    model_select = driver.find_element(By.ID, "model_choice")
    model_select.click()

    # Cliquer sur le bouton pour aller au modèle
    button = driver.find_element(By.ID, "go_button")
    button.click()

    # Vérifier que la redirection fonctionne
    assert "5000" in driver.current_url or "5001" in driver.current_url

    driver.quit()

def test_model_selection():
    driver = webdriver.Chrome()  # Ou un autre navigateur
    driver.get("http://localhost:8501")  # URL de l'application Streamlit

    # Sélectionner "SVM"
    model_select = driver.find_element(By.ID, "model_choice")
    model_select.send_keys("SVM")
    
    # Cliquer sur le bouton "Aller au modèle sélectionné"
    go_button = driver.find_element(By.ID, "go_button")
    go_button.click()

    # Vérifier que la redirection vers le service SVM se fait bien
    assert "5000" in driver.current_url

    driver.quit()

def test_background_image():
    driver = webdriver.Chrome()  # Ou un autre navigateur
    driver.get("http://localhost:8501")  # URL de l'application Streamlit

    # Vérifier si l'image de fond est présente
    background_image = driver.find_element_by_css_selector(".main")
    style = background_image.get_attribute("style")
    
    assert "background-image: url(" in style, "L'image de fond n'est pas chargée correctement"

    driver.quit()


