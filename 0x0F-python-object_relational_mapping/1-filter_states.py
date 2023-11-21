#!/usr/bin/python3

"""
a script that lists all states with a name starting with
N (upper N)from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) !=4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                        password=password, db=data, port=3306)
    cur = db.cursor()
    num_row = cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
                            'N%' ORDER BY states.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()