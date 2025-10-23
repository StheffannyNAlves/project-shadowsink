import functools
from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint
import datetime
import logging

shadow_bp = Blueprint('shadow_core',__name__)

# Rota principal que carrega a página HTML
@shadow_bp.route('/', methods=['GET', 'POST'])
@shadow_bp.route('/login', methods=['GET', 'POST'])
def login_page(): # obtém o id, senha 
    if request.method == 'POST':
        user_id = request.form.get('id_do_operador')
        password = request.form.get('senha_de_acesso')

        ip_capturado = request.remote_addr
        logging.warning(f"{ip_capturado} | USER: {user_id} | Password: {password}") # temporario, dps muda pra o db
        flash('Os dados inseridos estão incorretos', 'error')
        return render_template('login.html')
    return render_template('login.html')


def login_required(f): # exige que o usuário esteja logado, antes de acessar a rota
    @functools.wraps(f)
    def decorated_func(*args, **kwargs):
        if not session.get('logged_in'):
            flash('Você precisa fazer o login para acessar esta página.', 'warning')
            return redirect(url_for('shadow_core.login_page'))
        return f(*args, **kwargs)
    return decorated_func


@shadow_bp.route('/dashboard')
@login_required  # apenas usuários logados podem acessar
def dashboard():
    # adicionar lógica pra buscar logs e mostrar estatísticas.
    return render_template('dashboard.html', user_id=session['user_id'])



@shadow_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('Logout realizado com sucesso', 'info')
    return redirect(url_for('login_page'))
