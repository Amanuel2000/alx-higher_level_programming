#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb

"""
Access to the database and get the states
from the database.
"""
if __name__ == "__main__":
    db_con = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    db_cur = db_con.cursor()
    db_cur.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in db_cur.fetchall() if state[1][0] == "N"]
