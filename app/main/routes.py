# main/routes.py
from . import main
from flask import render_template

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/sobre')
def sobre():
    return render_template('sobre.html')

@main.route('/servicos')
def servicos():
    return render_template('servicos.html')

@main.route('/faq')
def faq():
    return render_template('faq.html')

@main.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@main.route('/conteudo')
def conteudo():
    return render_template('conteudo.html')

@main.route('/contato')
def contato():
    return render_template('contato.html')