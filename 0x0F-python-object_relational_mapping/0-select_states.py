#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                             <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":

    """
    Access to the database and get the states
    from the database.
    """
    d_base = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host="localhost", port=3306,)
    d_cursor = d_base.cursor()
    d_cursor.execute("SELECT * FROM `states`")
    [print(state) for state in d_cursor.fetchall()]
