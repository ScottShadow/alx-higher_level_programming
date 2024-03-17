#!/usr/bin/python3
"""  lists all cities by state from the database hbtn_0e_0_usa """
import sys
import MySQLdb
if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("""
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state,))

    results = cursor.fetchall()
    tmp = list(row[0] for row in results)
    print(*tmp, sep=", ")
    cursor.close()
    db.close()
