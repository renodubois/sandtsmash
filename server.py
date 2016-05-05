import argparse
import socket
import sys

from bottle import (app, Bottle, get, post, response, request, route, run, jinja2_view,
redirect, static_file)

from users import retrieveUserInfo, editUserProfile
from signup import formValidation, formInsertion
from authentication import requiresLogin, checkLogin
from events import getCurrentEvents
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
    print(request.get_cookie('current_user'))
    if request.get_cookie('current_user'):
        return {'currentUser':request.get_cookie('current_user')}
    return {}

# Login page
@get('/login/')
@jinja2_view("templates/login.html")
@load_alerts
def show_login():
    if request.get_cookie('current_user'):
        redirect('/')
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
    if request.get_cookie('current_user'):
        return {'currentUser':request.get_cookie('current_user')}
    return {}

@post('/signup/')
def validate_signup():
    signupForm = request.forms
    errors = formValidation(signupForm)
    if errors:
        for i in errors:
            save_danger(i)
        redirect('/signup/')
    else:
        formInsertion(signupForm)
        save_success('Account created successfully!')
        redirect('/login/')


# Logout of the website.
@get('/logout/')
@load_alerts
def log_out():
    if request.get_cookie('current_user'):
        response.set_cookie('current_user', "", path='/')
        save_success('You have been successfully logged out.')
    redirect('/')

# Events page
@get('/events/')
@jinja2_view('templates/events.html')
def view_events():
    eventData = {}
    eventData['currentEvents'] = getCurrentEvents()
    if request.get_cookie('current_user'):
        eventData['currentUser'] = request.get_cookie('current_user')
    return eventData

# View a detailed view of the event
@get('/events/event-<id>')
def view_event_details():
    pass


# Profile page

@get('/users/<username>/')
@jinja2_view("templates/profile.html")
def show_profile(username):
    userInfo = retrieveUserInfo(username)
    userInfo['username'] = username
    if request.get_cookie('current_user') == username:
        userInfo['ownsProfile'] = True
    if request.get_cookie('current_user'):
        userInfo['currentUser'] = request.get_cookie('current_user')
    return userInfo


@post('/users/<username>/')
@load_alerts
def change_profile(username):
    if request.get_cookie('current_user'):
        errors = editUserProfile(request.forms, username)
        if errors:
            for err in errors:
                save_danger(err)
                redirect('users/<username>/')
        else:
            save_success('Profile changed successfully!')
            redirect('users/<username>/')
    else:
        redirect('users/<username>/')

# Forum page
@get('/forum/')
@requiresLogin
@load_alerts
def show_forum():
    if request.get_cookie('current_user'):
        return {'currentUser':request.get_cookie('current_user')}
    return {}

# Configurations for the Alerts module.
sessionOptions = {
    'session.type': 'cookie',
    'session.validate_key': 'super-secret'
}
smashServer = app()
smashServer = SessionMiddleware(smashServer, sessionOptions)


# Run the server:
if __name__ == '__main__':
    run(app=smashServer, host='131.151.155.118', port=80)
