#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_0_usa """
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
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")

    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
