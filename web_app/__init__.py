#!/usr/bin/python3
"""Initialisation for app package"""
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from web_app import routes
