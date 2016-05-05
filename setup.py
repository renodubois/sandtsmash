# User, password, host, database
MY_SQL_CONNECTION = ('root', 'dankmemes', '127.0.0.1', 'RollaSmash')

with open("MeleeCharacters.txt") as meleeFile:
    meleeCharacters = meleeFile.read()
    meleeCharacters = meleeCharacters.splitlines()

for character in meleeCharacters:
    print(character)
