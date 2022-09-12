#!/usr/bin/python3
""" script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa
    where name matches the argument
"""

if __name__ == '__main__':
    # Standard Library imports
    import sys

    # related third party imports
    import MySQLdb as sql

    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    userinput = sys.argv[4]

    conn = sql.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=passwd,
            db=database)

    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name='{}'\
                ORDER BY states.id ASC".format(userinput))

    rows = cur.fetchall()

    for row in rows:
        if row[1] == userinput:
            print("{}".format(row))

    cur.close()
    conn.close()
