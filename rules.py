import re
from termcolor import *

def roll_no():
    roll = input("Enter your Roll no:")
    while not re.match("[0-9]", roll):
        print(colored('Entered Roll no is invalid!', 'red'))
        roll1 = input("Enter valid Roll no: ")
        roll = roll1
    return {"Roll":roll}
def stud_n():
    name = input("Enter your Name:")
    while not name.replace(' ', '').isalpha():
        print(colored('Entered name is invalid!', 'red'))
        name1 = input("Enter your Name:")
        name = name1
    return {"Name": name}
def cour():
    course = input("Enter your course name:").replace(' ', '')
    return {"Course":course}
def email_id():
    email = input('Email ID: ')
    while not re.fullmatch("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+.[a-z]{1,3}$", email):
        print(colored('Entered Email ID is invalid!', 'red'))
        mail = input("Enter valid email: ")
        email = mail
    return {"Email":email}
def col():
    college = input("Enter your college name:").replace(' ', '')
    return {"College":college}
