import sqlite3
CONN = sqlite3.connect('words_1.db')
CURSOR = CONN.cursor()

query = '''
SELECT all_words
FROM words;
'''
all_words = CURSOR.execute(query).fetchall()
word_list = [word[0] for word in all_words]
CONN.close()
