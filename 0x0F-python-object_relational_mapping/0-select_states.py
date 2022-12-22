#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_con = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cur = db_con.cursor()

    db_cur.execute("SELECT * FROM states")

    rows_selected = db_cur.fetchall()

    for row in rows_selected:
        print(row)
