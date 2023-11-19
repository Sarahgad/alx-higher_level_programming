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
    cmd = """SELECT cities.name FROM cities INNER JOIN states ON
           states.id=cities.state_id WHERE states.name=%s"""
    cur.execute(cmd, (argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
