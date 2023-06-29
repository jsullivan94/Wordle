import sqlite3
CONN = sqlite3.connect('words.db')
CURSOR = CONN.cursor()

query = '''
SELECT words
FROM word;
'''
all_words = CURSOR.execute(query).fetchall()
word_list = [word[0] for word in all_words]
CONN.close()
