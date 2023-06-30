## two users in table are test : abc and sam : python


import sqlite3

globalUsername = None
signedIn = False

def Update_streak():
    #print("I was called")
    global globalUsername
    print(f' {globalUsername} your streak has increased !')
    sheesh = sqlite3.connect('words.db')
    sheeshcursor = sheesh.cursor()

    sheeshcursor.execute("""
    UPDATE users SET streak = streak + 1
    WHERE username = ?;
    """,(globalUsername,))
    sheesh.commit()
    sheeshcursor.close()
    sheesh.close()

def decrement_streak():
    #print("I was called")
    global globalUsername
    print(f'{globalUsername} your streak was broken!')
    sheesh = sqlite3.connect('words.db')
    sheeshcursor = sheesh.cursor()

    sheeshcursor.execute("""
    UPDATE users SET streak = 0
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
        global signedIn
        signedIn = True

    else:
        print("Invalid username or password.")
        


    cursor.close()
    conn.close()