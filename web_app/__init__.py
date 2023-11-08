#!/usr/bin/python3
"""Initialisation for app package"""
from flask import Flask

app = Flask(__name__)

from web_app import routes
