#!/usr/bin/python3
""" 0. Get all states module """
import MySQLdb

conn = MySQLdb.connect(user="root", db="hbtn_0e_0_usa")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
