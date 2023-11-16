#!/usr/bin/python3
"""Defines routes pages for web-app"""
from flask import render_template, flash, redirect, url_for
from web_app import app, db
from web_app.forms import LoginForm, RegisterForm
from web_app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user

@app.route('/')
@app.route('/home')
def home():
    title = "Agroboard | Smart Decisions"
    return render_template("home.html", title=title)


@app.route('/register', methods=['GET', 'POST'])
def register():
    title = "Register"
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashd_pswd = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data,
                password_hash=hashd_pswd)
        db.session.add(user)
        db.session.commit()
        flash(f"Account registration successful for {form.email.data}")
        return redirect(url_for('login'))
    return render_template('register.html', title=title, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = "Log In"
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(f"Login Successful for {form.email.data}")
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', title=title, form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

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
