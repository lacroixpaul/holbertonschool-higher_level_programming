#!/usr/bin/python3
"""
Script Python qui se connecte à une base MySQL,
récupère et affiche les données triées par id.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
