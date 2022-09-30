import sqlite3
from rules import roll_no,stud_n,col,email_id,cour
import edit
import start

def register_student():
    while True:
        con= sqlite3.connect('student')
        cursor = con.cursor()
        print('-----------FILL THE BELOW DETAILS-------------')
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

        try:
            while True:
                save= input('Do you want to save this information - y/n: ')
                if save in['y','yes']:
                    cursor.execute('insert into std_info values(?,?,?,?,?);',(roll,name,course,email,college))

                    con.commit()
                    con.close()
                    print('Data saved...')
                    start.con()
                    break
                elif save in['n','no']:
                    while True:
                        check = {1: 'Do you want to edit this information  ', 2: 'Do you want to Quit'}
                        for i in check:
                            print(i, '.', check[i])
                        save_1= input('Enter (1 or 2):')
                        if save_1 =='1':
                            edit.update()
                        elif save_1 =='2':
                           quit()
                        break
                else:
                    break
        except sqlite3.IntegrityError:
            print("Information already exist.....")
            break






