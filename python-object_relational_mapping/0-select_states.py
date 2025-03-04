#!/usr/bin/python3
"""Module for Selecting states"""

from sys import argv
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states')
    for state in cursor.fetchall():
        print(state)
    if cursor:
        cursor.close()
    if db:
        db.close()
