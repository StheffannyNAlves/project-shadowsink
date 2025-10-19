import os
import functools
from flask import Flask, render_template, request, redirect, url_for, flash, session
import datetime
import logging
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

template_folder = os.path.join(BASE_DIR, 'app', 'templates')
static_folder = os.path.join(BASE_DIR, 'app', 'static')

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, 'app', 'templates'),
            static_folder=os.path.join(BASE_DIR, 'app', 'static'))
app.secret_key = 'chave_aleatoria'

VALID_USER = {"id_operador": "Nyx",
               "senha": "123"}

logging.basicConfig(
    filename='honeypot.log', 
    level=logging.WARNING, 
    format='%(asctime)s - %(levelname)s - IP:%(message)s'
)


# Rota principal que carrega a página HTML
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login_page(): # obtém o id, senha 
    if request.method == 'POST':
        user_id = request.form.get('id_do_operador')
        password = request.form.get('senha_de_acesso')

        ip_capturado = request.remote_addr
        logging.warning(f"{ip_capturado} | USER: {user_id} | Password: {password}")
        if user_id == VALID_USER["id_operador"] and password == VALID_USER["senha"]:
            session['logged_in'] = True
            session['user_id'] = user_id
            flash('Login realizado com sucesso', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Os dados inseridos estão incorretos', 'error')
            return render_template('login.html')
    
    return render_template('login.html')


def login_required(f): # exige que o usuário esteja logado, antes de acessar a rota
    @functools.wraps(f)
    def decorated_func(*args, **kwargs):
        if not session.get('logged_in'):
            flash('Você precisa fazer o login para acessar esta página.', 'warning')
            return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorated_func


@app.route('/dashboard')
@login_required  # apenas usuários logados podem acessar
def dashboard():
    # adicionar lógica pra buscar logs e mostrar estatísticas.
    return render_template('dashboard.html', user_id=session['user_id'])














@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('Logout realizado com sucesso', 'info')
    return redirect(url_for('login_page'))













































if __name__ == '__main__': #programa principal
    # Usa a variável de ambiente FLASK_DEBUG para controlar o modo de debug
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, 
            ssl_context=('cert.pem', 'key.pem'),
             host='0.0.0.0', 
             port=5000)