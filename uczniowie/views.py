# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import Flask
from flask import render_template, request, redirect, url_for, abort, flash
from modele import *
from forms import *

app = Flask(__name__)

@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')


@app.route('/lista_ucz')
def lista_ucz():
    uczniowie = Uczen.select()
    return render_template('lista_ucz.html', query=uczniowie)

@app.route('/lista_kl')
def lista_kl():
    klasy = Klasa.select()
    return render_template('lista_kl.html', query=klasy)

@app.route('/dodaj_kl', methods=['GET', 'POST'])
def dodaj_kl():
    form = DodajForm()
    form.klasa.choices = [(k.id, k.klasa) for k in Klasa.select()]
    
    if form.validate_on_submit():
        print(form.data)
        k = Klasa(klasa=form.klasa.data)
        k.save()

        flash("Dodano klasę!", "sukces")
        return redirect(url_for('index'))
    elif request.method == 'POST':
        flash_errors(form)
    return render_template('dodaj_kl.html', form=form)
    
    @app.route('/dodaj_kl', methods=['GET', 'POST'])

