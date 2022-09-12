#!/usr/bin/python3
""" module that lists all states in hbtn_0e_0_usa databse """

if __name__ == '__main__':
    # Standard Library imports
    import sys

    # related third party imports
    import MySQLdb as sql

    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    conn = sql.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=passwd,
            db=database)

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
