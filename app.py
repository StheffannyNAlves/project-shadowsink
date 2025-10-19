import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
import logging
from app.routes import shadow_bp
import datetime, json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

template_folder = os.path.join(BASE_DIR, 'app', 'templates')
static_folder = os.path.join(BASE_DIR, 'app', 'static')

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, 'app', 'templates'),
            static_folder=os.path.join(BASE_DIR, 'app', 'static'))
app.secret_key = 'chave_aleatoria'
app.register_blueprint(shadow_bp)



logging.basicConfig(
    filename='honeypot.log', 
    level=logging.WARNING, 
    format='%(asctime)s - %(levelname)s - IP:%(message)s'
)



if __name__ == '__main__': #programa principal
    # Usa a variável de ambiente FLASK_DEBUG para controlar o modo de debug
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, 
            ssl_context=('cert.pem', 'key.pem'),
             host='0.0.0.0', 
             port=5000)