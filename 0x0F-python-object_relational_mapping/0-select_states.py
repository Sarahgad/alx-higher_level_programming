#!/usr/bin/python3
"""Write a script that lists 
all states from the database
 hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    container = { 'username': sys.argv[1],
                'password': sys.argv[2],
                'database': sys.argv[3],
                'host': 'localhost',
                'port': 3306}
                

    db = MySQLdb.connect(**container)
    cur = db.cursor()
    cur.excute("SELECT * FROM states ORDER BY states.id ASC;")
    for table in cur:
        print(table)
        