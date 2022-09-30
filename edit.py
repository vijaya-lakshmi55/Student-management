import sqlite3
from rules import roll_no,stud_n,cour,email_id,col
import re
from termcolor import *
def update():
    con= sqlite3.connect('student')
    cursor = con.cursor()
    a= input('please enter std_roll no to edit_info: ')
    while not re.match('[0-9]', a):
        print(colored('Entered Roll no is invalid!', 'red'))
        roll1 = input("Enter valid Roll no: ")
        a = roll1

    check= {1:'student name',2:'roll no',3:'college name',4:'email_id',
            5:'course name',6:'all details'}

    while True:

        for i in check:
            print(i,'.',check[i])
        choice=input('enter (1-6) option to edit: ')
        if choice == '2':
            r = roll_no()
            roll = r['Roll']
            query = "update std_info set roll = '" + roll + "' where roll =" + a
            con.execute(query)
        elif choice == '1':
            n=stud_n()
            name = n['Name']
            query = "update std_info set std_name = '" + name + "' where roll =" + a
            con.execute(query)
        elif  choice=='5':
            c=cour()
            course = c['Course']
            query = "update std_info set course = '" + course+ "' where roll =" + a
            con.execute(query)
        elif choice == '4':
            e=email_id()
            email=e["Email"]
            query = "update std_info set email_id = '" + email + "' where roll =" + a
            con.execute(query)
        elif choice == '3':
            co=col()
            college=co["College"]
            query = "update std_info set college = '" + college + "' where roll =" + a
            con.execute(query)
        elif choice == '6':
            r = roll_no()
            roll = r['Roll']
            n = stud_n()
            name = n['Name']
            co = col()
            college = co["College"]
            e = email_id()
            email = e["Email"]
            c = cour()
            course = c['Course']
            query = "update std_info set roll='"+roll+"',std_name = '" + name + "',college = '" + college + "',email_id = '" + email + "', course = '" + course+ "' where roll =" + a
            con.execute(query)
        else:
            print("please enter (1-6)")
        con.commit()
        con.close()
        print('Data updated...')
        break