import os
from flask import Flask, render_template, request, redirect, url_for
import datetime
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(BASE_DIR, 'app', 'templates')
static_folder = os.path.join(BASE_DIR, 'app', 'static')

app = Flask(__name__, template_folder=template_folder, 
            static_folder=static_folder, static_url_path='/static') 

# Rota principal que carrega a página HTML
@app.route('/')
def login_page():
    return render_template('login.html'), "Falha na autenticação. Por favor, verifique suas credenciais e tente novamente."

logging.basicConfig(
    filename='honeypot.log', 
    level=logging.WARNING, 
    format='%(asctime)s - %(levelname)s - IP:%(message)s'
)





@app.route('/handle_login', methods=['POST'])
def handle_login():
    username = request.form.get('username')  # pega os metadados
    password = request.form.get('password')


    ip_capturado = request.remote_addr

    timestamp = datetime.datetime.now()

    log_message = f"{ip_capturado} | USER: {username} | Password: {password}"
    return "Erro de Autenticação. Credenciais incorretas ou conta bloqueada. Tente novamente mais tarde."
if __name__ == '__main__':
    # Usa a variável de ambiente FLASK_DEBUG para controlar o modo de debug
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, ssl_context =('cert.pem', 'key.pem'))