#!/usr/bin/python3
"""Module for Selecting states with name starting with 'N'"""

import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM states WHERE name \
                       LIKE 'N%' ORDER BY states.id ASC")
        for state in cursor.fetchall():
            print(state)
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
