## two users in table are test : abc and sam : python


import sqlite3

globalUsername = None
signedIn = False

def update_streak():
    global globalUsername
    print(f'this is global username {globalUsername}')
    sheesh = sqlite3.connect('words.db')
    sheeshcursor = sheesh.cursor()

    sheeshcursor.execute("""
    UPDATE users SET streak = streak + 1
    WHERE username = ?;
    """,(globalUsername,))
    sheesh.commit()
    sheeshcursor.close()
    sheesh.close()


def Sign_In():
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()
    inputUser = input("Enter your username: ")
    global globalUsername # have to give it access
    globalUsername = inputUser
    inputPassword = input("Enter password: ")

    cursor.execute("""
    SELECT * FROM users
    WHERE username = ?
    AND password = ?;
    """, (inputUser, inputPassword))

    passResult = cursor.fetchone()

    if passResult:
        print("Login successful!")
        signedIn = True

    else:
        print("Invalid username or password.")
        


    cursor.close()
    conn.close()