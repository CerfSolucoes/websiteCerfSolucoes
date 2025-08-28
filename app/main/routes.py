# main/routes.py
from flask import render_template, current_app
from . import main

@main.route('/')
def index():
    services = current_app.services  # pega da instância do Flask
    return render_template('home.html', services=services)

@main.route('/sobre')
def sobre():
    return render_template('sobre.html')

@main.route('/servicos')
def servicos():
    return render_template('home.html')

@main.route('/faq')
def faq():
    return render_template('faq.html')

@main.route('/portfolio')
def portfolio():
    return render_template('home.html')

@main.route('/conteudo')
def conteudo():
    return render_template('home.html')

@main.route('/contato')
def contato():
    return render_template('contato.html')