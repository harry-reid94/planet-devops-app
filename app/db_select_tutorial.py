import sqlite3
conn = sqlite3.connect('testDB.db')


c = conn.cursor()
c.execute('''
		
SELECT *
FROM tutorial_model
;

''')

conn.commit()