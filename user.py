import sqlite3
import hashlib

globalUsername = None
signedIn = False
globalStreak = 0

def Update_streak():
    global globalUsername
    conn = sqlite3.connect('words_1.db')
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users SET streak = streak + 1
    WHERE username = ?;
    """,(globalUsername,))
    conn.commit()
    cursor.close()
    conn.close()

def call_streak():
    global globalUsername
    global globalStreak
    
    conn = sqlite3.connect('words_1.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT streak FROM users WHERE username = ?;
    """, (globalUsername,))

    globalStreak = cursor.fetchone()
    globalStreak = globalStreak[0] if globalStreak else None

    print(f'                   {globalUsername} your streak is now {globalStreak}!')
  
    cursor.close()
    conn.close()

def decrement_streak():
    global globalUsername
    print(f'                   {globalUsername} your streak was broken!')
    conn = sqlite3.connect('words_1.db')
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users SET streak = 0
    WHERE username = ?;
    """,(globalUsername,))
    conn.commit()
    cursor.close()
    conn.close()

def Sign_In():
    conn = sqlite3.connect('words_1.db')
    cursor = conn.cursor()
    inputUser = input("                        Enter your username: ")
    global globalUsername
    globalUsername = inputUser
    inputPassword = input("                        Enter password: ")

    hashed_password = hashlib.sha256(inputPassword.encode()).hexdigest()

    cursor.execute("""
    SELECT * FROM users
    WHERE username = ?
    AND password = ?;
    """, (inputUser, hashed_password))

    passResult = cursor.fetchone()

    if passResult:
        print("                        Login successful!")
        global signedIn
        signedIn = True

    else:
        print("                     Invalid username or password.")
        input_sign_up = input("                        Sign up instead?: y/n ")
        if input_sign_up == "y":
            Sign_up()
        else:
            Sign_In()
    cursor.close()
    conn.close()

def Sign_up():
    conn = sqlite3.connect("words_1.db")
    cursor = conn.cursor()
    input_create_user = input("                        Create your username: ")
    global globalUsername
    globalUsername = input_create_user
    input_create_password = input("                        Create your password: ")
    hashed_password = hashlib.sha256(input_create_password.encode()).hexdigest()
    
    try:
        cursor.execute("""
        INSERT INTO users (username, password)
        VALUES
        (?, ?)
        """, (input_create_user, hashed_password))
        conn.commit()
        global signedIn
        signedIn = True
        print("                        Signup successful!")
    except sqlite3.IntegrityError:
        print("          Username already exists. Please choose another one.")
        Sign_up()    
    
    cursor.close()
    conn.close()
