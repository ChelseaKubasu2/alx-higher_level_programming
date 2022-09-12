
#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""

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
        if row[1].startswith("N"):
            print(row)

    cur.close()
    conn.close()
