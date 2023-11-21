from flask import render_template, flash, request, session, url_for, redirect
from app import app
import json
from .db_manager import *

@app.route('/')
def index():
    return "Hello World!"
