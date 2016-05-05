# User, password, host, database
MY_SQL_CONNECTION = ('root', 'dankmemes', '127.0.0.1', 'RollaSmash')

with open("MeleeCharacters.txt") as meleeFile:
    meleeCharacters = meleeFile.read()
    meleeCharacters = meleeCharacters.splitlines()

with open("Admins.txt") as adminFile:
    admins = adminFile.read()
    admins = admins.splitlines()
