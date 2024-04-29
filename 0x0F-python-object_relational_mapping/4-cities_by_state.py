#!/usr/bin/python3
"""
Lists all `cities` from the database `hbtn_0e_4_usa`.

Arguments:
    it takes three arguments
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    # By default, it will connect to localhost:3306

    db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name)
    curs = db.cursor()

    curs.execute("SELECT c.id, c.name, s.name \
                 FROM cities c INNER JOIN states s \
                 ON c.state_id = s.id \
                 ORDER BY c.id")
    rows = curs.fetchall()

    for row in rows:
        print(row)
