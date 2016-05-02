def formValidation(form):
    signupForm = request.form
    username = signupForm['username']
    fname = signupForm['fname']
    lname = signupForm['lname']
    location = signupForm['location']
    password = signupForm['password']
    password_confirm = signupForm['password-confirm']
    error = []
    if len(username) < 4 or len(username) > 20:
        error.append('Username must be between 4 and 20 characters!')
    if fname == '':
        error.append('First name field must be filled out!')
    if len(fname) > 30:
        error.append('Names must be less than 30 characters!')
    if lname == '':
        error.append('Last name field must be filled out!')
    if len(lname) > 30:
        error.append('Names must be less than 30 characters!')
    if location == '':
        error.append('Location field must be filled out!')
    if len(password) < 6 or len(password) > 36:
        error.append('Password must be between 6 and 36 characters!')
    if password != password_confirm:
        error.append('Password does not match confirmation password!')

    return error


def formInsertion(form):
    
