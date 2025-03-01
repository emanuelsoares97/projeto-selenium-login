from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Carregar os dados
credenciais_df = pd.read_csv('credentials.csv')

# aceder ao utilizador e pass
utilizador = credenciais_df.loc[0, 'username']
password = credenciais_df.loc[0, 'password']


# Abre o navegador
navegador = webdriver.Chrome()

# Entra no link
navegador.get("https://usarositedaempresa.pt") #nao existe apenas para nao colocar o site da empresa

# Tela cheia
navegador.maximize_window()

# Encontrar o campo de utilizador e preencher
WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, "Username"))).send_keys(utilizador)
WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, "Password"))).send_keys(password)

# Clicar no login
clicar_login = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.primary")))
clicar_login.click()

# Encontrar um elemento na tela e clicar
registar = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "branding-bar")))
registar.click()

# Clicar em registrar
clicar_registar = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.primary.js-dialog-close")))
clicar_registar.click()

navegador.quit()