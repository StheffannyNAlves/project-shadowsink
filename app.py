import os
from flask import Flask, render_template


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(BASE_DIR, 'app', 'templates')
static_folder = os.path.join(BASE_DIR, 'app', 'static')

app = Flask(__name__, template_folder=template_folder, 
            static_folder=static_folder, static_url_path='/static') 

# Rota principal que carrega a página HTML
@app.route('/')
def login_page():
    # Certifique-se de que seu HTML está na pasta 'templates/'
    return render_template('login.html'), "Falha na autenticação. Por favor, verifique suas credenciais e tente novamente."
@app.route('/handle_login', methods=['POST'])
def handle_login():
    # Por enquanto, apenas retorna uma mensagem. 
    # A lógica de captura virá aqui!
    return "Autenticação em processamento... Tente novamente mais tarde. (Seu IP foi registrado.)"

if __name__ == '__main__':
    # Use a variável de ambiente FLASK_DEBUG para controlar o modo de debug
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, ssl_context =('cert.pem', 'key.pem'))