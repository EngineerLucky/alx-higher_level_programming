#!/usr/bin/python3

"""
Lists all `states` from the database `hbtn_0e_0_usa`.

Arguments:
    it takes in four arguments,
    the arguments are strings,
    name searched.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    first = sys.argv[1]
    second = sys.argv[2]
    third = sys.argv[3]

    name_searched = sys.argv[4]

    # By default, it will connect to localhost:3306

    db = MySQLdb.connect(user=first, passwd=second, db=third)
    cur = db.cursor()
    cur.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = '{}';".format(name_searched))
    states = cur.fetchall()

    for state in states:
        print(state)
