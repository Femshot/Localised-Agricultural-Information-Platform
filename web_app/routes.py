#!/usr/bin/python3
"""Defines routes pages for web-app"""
from flask import render_template, flash, redirect, url_for
from web_app import app
from web_app.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    title = "Agroboard | Smart Decisions"
    return render_template("home.html", title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    title = "Log In"
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login Successful for {form.email.data}", 'success')
        return redirect('/home')
    return render_template('login.html', title=title, form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/weather')
def weather():
    return render_template('weather.html', title="Agroboard | Weather Forcast")

@app.route('/article')
def article():
    return render_template('article.html')
