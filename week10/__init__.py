while(True):
    print("1- login\n2-sign up\n3- exit\nChoose 1 or 2 or 3")
    choice = input('')
    if choice == '1':



        # read data and compare
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        file = open('test.txt', 'r')
        is_exsit = False
        for line in file:
            dataList = line.split(",")
            if username == dataList[0].strip() and password == dataList[1].strip():
                is_exsit = True
                print('login success')
                print('your username is: ' + dataList[0])
                print('your password is: ' + dataList[1])
                break
        if is_exsit == False:
            print('invalid user name or password')
        file.close()




    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        userData = username + "," + password + '\n'
        file = open('test.txt', 'a')
        file.write(f'Hi there\t{userData}\n')
        file.close()
    elif choice == '3':
        break
    else:
        print('enter 1 or 2 or 3 ')