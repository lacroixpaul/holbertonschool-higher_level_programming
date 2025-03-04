#!/usr/bin/python3
"""Module for Selecting states with name starting with 'N'"""

from sys import argv
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(
        username=argv[1],
        password=argv[2],
        database=argv[3]
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
