import argparse
import socket
import sys

from bottle import (app, Bottle, get, post, response, request, route, run, jinja2_view,
redirect, static_file)

from authentication import requiresLogin, checkLogin
from alerts import load_alerts, save_danger, save_success

@route('/assets/<path:path>')
def static(path):
    return static_file(path, root='assets')

# Main page.
@get('/')
@load_alerts
@jinja2_view("templates/index.html")
def index():
	return {}

# Login page
@get('/login/')
@load_alerts
@jinja2_view("templates/login.html")
def show_login():
	return {}

@post('/login/')
def validate_login():
    loginForm = request.forms
    errors = checkLogin(loginForm)
    if errors:
        for i in errors:
            save_danger(i)
        redirect('/login/')
    # If user signed in successfully:


# Signup page

@get('/signup/')
@load_alerts
@jinja2_view("templates/signup.html")
def show_signup():
    return {}

@post('/signup/')
def validate_signup():
    return {}

# Rankings page


# Profile page


# Forum page
@get('/forum/')
@load_alerts
@requiresLogin
def show_forum():
	return {}
# Run the server:
run(host='131.151.155.118', port=80)
