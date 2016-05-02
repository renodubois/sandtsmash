import argparse
import socket
import sys

from bottle import (app, Bottle, get, post, response, request, route, run, jinja2_view,
redirect, static_file)
from signup import formValidation


from authentication import requiresLogin, checkLogin
from alerts import load_alerts, save_danger, save_success
from beaker.middleware import SessionMiddleware

@route('/assets/<path:path>')
def static(path):
    return static_file(path, root='assets')

# Main page.
@get('/')
@jinja2_view("templates/index.html")
@load_alerts
def index():
	return {}

# Login page
@get('/login/')
@jinja2_view("templates/login.html")
@load_alerts
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
    # Grab their username, and sanitize it.
    username = loginForm['username']
    # Create a session variable equal to their username:
    response.set_cookie("current_user", username, path='/')
    # Let them know they've been signed in successfully:
    save_success('Successfully logged in as {}'.format(username))
    # Redirect them back to the home page:
    redirect('/')



# Signup page

@get('/signup/')
@jinja2_view("templates/signup.html")
@load_alerts
def show_signup():
    return {}

@post('/signup/')
def validate_signup():
    signupForm = request.forms
    errors = formValidation(signupForm)
    if errors:
        for i in errors:
            save_danger(i)
        redirect('/signup/')
        

# Rankings page


# Profile page


# Forum page
@get('/forum/')
@requiresLogin
@load_alerts
def show_forum():
	return {}

# Configurations for the Alerts module.
sessionOptions = {
    'session.type': 'cookie',
    'session.validate_key': 'super-secret'
}
smashServer = app()
smashServer = SessionMiddleware(smashServer, sessionOptions)


# Run the server:
run(app=smashServer, host='131.151.155.118', port=80)
