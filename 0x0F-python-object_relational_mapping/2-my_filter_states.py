#!/usr/bin/python3
"""
a script that takes in an argument and displays
all values in the state table of hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
import sys

if __name__ =='__main__':
    args = sys.argv
    if len(args) !=5:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    state_name = args[4]
    db = MySQLdb.connect(host='localhost', user=username,
                        passwd=password, db=data, port=3306)
    cur = db.cursor()
    num_rows = cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
                            '{}' ORDER BY state.id;".format(state_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
