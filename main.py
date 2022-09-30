import data
import details
from termcolor import colored
from linked_list import LinkedList
print(colored('---------------STUDENT MANAGEMENT SYSTEM------------------','green'))
check={1:'Do you want to register student ',2:'Do you want to see the details of student'}

while True:
        for i in check:
                print(i, '.', check[i])
        ask = input('ENTER (1 or 2) : ')
        if ask>'2':
                ask = input('choose any one(1 or 2) : ')
        elif ask =='1':
                list = LinkedList()
                list.push(data.register_student())
        elif ask =='2':
                details.std_details()
        break




