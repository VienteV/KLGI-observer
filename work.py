import sqlite3

conn = sqlite3.connect('BVdb.db')
cur = conn.cursor()
while True:
    conn.commit()
    request = input()
    try:
        cur.execute(f'''{request}''')
        a = cur.fetchall()
        print(*a, sep='\n')
    except Exception as e:
        print(e)
        continue
