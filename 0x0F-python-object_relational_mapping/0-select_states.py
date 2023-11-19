#!/usr/bin/python3
"""Write a script that lists
all states from the database
 hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb as mysql
    import sys
    container = {'user': sys.argv[1],
                 'passwd': sys.argv[2],
                 'db': sys.argv[3],
                 'host': 'localhost',
                 'port': 3306}

    db = MySQLdb.connect(**container)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

