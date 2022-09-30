import sqlite3
from rules import roll_no
def std_details():
    con= sqlite3.connect('student')
    cursor = con.cursor()
    r = roll_no()
    roll = r['Roll']
    cursor.execute(f"select * from std_info where roll = {roll}")
    row= cursor.fetchall()
    for row in row:
        print("Name : ", row[1])
        print("College name  : ", row[4])
        print("email_id  :", row[3])
        print("course :", row[2])
        con.close()
