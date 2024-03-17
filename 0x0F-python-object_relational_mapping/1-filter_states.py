#!/usr/bin/python3
"""  lists all states """
import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute(
        """SELECT *
        FROM states
        WHERE name
        LIKE BINARY'N%'
        ORDER BY states.id""")

    output = cursor.fetchall()
    for row in output:
        print(row)
    cursor.close()
    db.close()
