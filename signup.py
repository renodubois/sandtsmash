def validate_signup(form):
    username = form['username']
    fname = form['fname']
    lname = form['lname']
    location = form['location']
    password = form['password']
    password_confirm = form['password-confirm']

    if len(username) < 4 or len(username) > 20:
        print("Username must be between 4 and 20 characters!")
    if fname == '':
        #error field required
    if lname == '':
        #Error, field required
    if location == '':
        #error, field required
    if len(password) < 6 or len(password) > 36:
        #error
    if password != password_confirm:
        #error
