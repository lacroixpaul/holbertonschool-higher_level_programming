#!/usr/bin/python3
"""Module for Selecting states"""

from sys import argv
import MySQLdb


if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        username=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()
    try:
        cursor.execute('SELECT * FROM states ORDER BY states.id ASC')
        for state in cursor.fetchall():
            print(state)
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
