import mysql.connector

print('\t  NIIT BANK\n\t______________'.expandtabs(17))
print('\t  LOGIN\n\t______________'.expandtabs(7))

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='bankapp')
mycursor = cnx.cursor()



try:
    accountname = int(input('enter your accountname: '))
    if len(str(accountname)) < 10:
        print('account number length must be 10')

    elif len(str(accountname)) > 10:
        print('account number must be 10')


    userPin = int(input('enter your pin: '))
    if len(str(userPin)) < 4:
        print('pin length must be 4')

    elif len(str(userPin)) > 4:
        print('pin must be 4')
    mycursor.execute(f'''select * from customers_profile where accountnumber = {accountname} and user_pin = {userPin}''')
    if mycursor.fetchall():
        pass
    else:
        print('Incorrect details')
        print('''1) Forget password\n2)Try again''')
        option = int(input('enter option: '))
        if option == 1:
            print('yess')
        elif option == 2:
            print("Try Again")
            exit()
except:
    print('number only accepted >>Try again')
    exit()



def session():
    mycursor.execute(
        f'''select * from customers_profile where accountnumber = {accountname} and user_pin = {userPin}''')
    return mycursor.fetchall()


