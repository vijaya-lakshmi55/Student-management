import first
def con():
    check = {1: 'Do you want to continue  ', 2: 'Do you want to Quit'}
    while True:
        for i in check:
            print(i, '.', check[i])
        user_ch= input('Enter (1 or 2):')
        if user_ch =='1':
            first.students()
        elif user_ch=='2':
            quit()
            break