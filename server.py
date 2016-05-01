import argparse
import socket
import sys

from bottle import (app, Bottle, get, post, response, request, route, run, jinja2_view,
redirect, static_file)

from authentication import requiresLogin

@route('/assets/<path:path>')
def static(path):
    return static_file(path, root='assets')

# Main page.
@get('/')
@jinja2_view("templates/index.html")
def index():
	return {}

# Login page
@get('/login/')
@jinja2_view("templates/login.html")
def show_login():
	return {}

@post('/login/')
def validate_login():
	return {}

# Signup page


# Rankings page


# Profile page


# Forum page
@get('/forum/')
@requiresLogin
def show_forum():
	return {}
# Run the server:
run(host='131.151.155.118', port=80)
