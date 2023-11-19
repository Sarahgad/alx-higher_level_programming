#!/usr/bin/python3
"""Write a script that lists
all states from the database
 hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cmd = "SELECT cities.id, cities.name, states.name FROM cities\
           INNER JOIN states ON states.id=cities.state_id;"
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)
