from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep
import random

def espera_aleatoria():
    """Criei esta função apenas para ser possivel ver o que o bot está a fazer"""
    sleep(random.uniform(1.5, 3.5))

# Carregar os dados
credenciais_df = pd.read_csv('dados/credenciais.csv')

# aceder ao utilizador e pass
utilizador = credenciais_df.loc[0, 'username']
password = credenciais_df.loc[0, 'password']


# Abre o navegador
navegador = webdriver.Chrome()

# Entra no link
navegador.get("http://localhost:8000/index.html") 

# Tela cheia
navegador.maximize_window()

espera_aleatoria()

# Encontrar o campo de utilizador e preencher
WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(utilizador)
WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(password)

# Clicar no login
clicar_login = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))
clicar_login.click()

espera_aleatoria()

# Encontrar um elemento na tela e clicar
registar = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, "btnRegistrar")))
registar.click()

espera_aleatoria()

# Clicar em registrar
clicar_registar = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, "btnConfirmar")))
clicar_registar.click()

espera_aleatoria()

navegador.quit()
