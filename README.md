Projeto Selenium Login


Descrição
Este repositório contém um script de automação Selenium que faz login automaticamente numa página web simulada. O objetivo inicial era apenas testar a automação do login, mas o projeto acabou por evoluir e agora inclui:

Automação de login com Python + Selenium
Interface web com HTML, CSS e JS
Simulação de validação de login com PHP (sem base de dados)

A ideia não é criar um sistema completo, mas sim um ambiente controlado para testar automações e aprender mais sobre Selenium.

Tecnologias Utilizadas
Python 3.8+ → Automação com Selenium
Selenium WebDriver → Controle do navegador
HTML + CSS + JS → Interface gráfica da aplicação
PHP → Simulação do backend (validação de login)

Instalação e Como Usar
Clonar o repositório
git clone https://github.com/seuusuario/projeto-selenium-login.git
cd projeto-selenium-login

Criar ambiente virtual e instalar dependências
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt

Iniciar o Servidor Local
php -S localhost:8000
Depois disso, a página estará disponível em http://localhost:8000/index.html.

Executar o Script de Automação
python login_script.py

O Selenium irá abrir o navegador, preencher os campos e fazer login sozinho.~

projeto-selenium-login/
│── dados/              # (Se precisar guardar ficheiros CSV ou JSON futuramente)
│── estilos/            # Arquivos CSS para o design
│── imagens/            # Imagens usadas no site
│── util/               # Scripts JS para validações e interações
│── venv/               # Ambiente virtual do Python (não deve ser enviado para o Git)
│── index.html          # Página inicial (formulário de login)
│── pagregisto.html     # Página que aparece após login bem-sucedido
│── login_script.py     # Script Selenium para automação do login
│── submit_login.php    # Simulação de backend para validar login
│── requirements.txt    # Dependências do projeto
│── README.md           # Documentação do projeto
│── .gitignore          # Arquivos que devem ser ignorados no Git

Considerações Finais
Este projeto começou apenas como um script para login automático no Selenium, mas acabou por incluir uma simulação de uma página de login real, onde o Selenium pode interagir como se fosse um utilizador normal.

Se quiseres contribuir ou sugerir melhorias, estás à vontade!