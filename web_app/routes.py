#!/usr/bin/python3
"""Defines routes pages for web-app"""
from flask import render_template
from web_app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")
