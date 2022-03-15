import random
from datetime import datetime
import mysql.connector

print('\t  NIIT BANK\n\t______________'.expandtabs(17))
print('\t  SIGN UP\n\t______________'.expandtabs(7))


def sign_up():
    firstname = []
    lastname = []
    email = []
    sex = []
    phonenumber =[]
    accounttype = []
    accountnumber = []
    address = []
    bvn = []
    userpin = []

    def FirstName():
        firstName = input('enter your firstName: ').lstrip()
        for numeric in firstName:
            if numeric.isdigit():
                print('Firstname must contain only alphabet')
                return FirstName()
            elif len(firstName) <3:
                print('firstname minimum length must be 3 letters')
                return FirstName()
            elif len(firstName) > 30:
                print('firstname maximum length is 30')
                return FirstName()
        firstname.append(firstName)
    FirstName()


    def LastName():
        lastName = input('enter your lastName: ').lstrip()

        for numeric in lastName:
            if numeric.isdigit():
                print('Lastname must contain only alphabet')
            elif len(lastName) <3:
                print('lastname minimum length must be 3 letters')
                return LastName()
            elif len(lastName) >30:
                print('lastname maximum length is 30')
                return LastName()
        lastname.append(lastName)
    LastName()



    def EMAIL():
        Email = input('enter your Email: ').lstrip()

        for i in Email:
            if not (Email.count('@') == 1):
                print('invalid Email: include "@" once')
                return EMAIL()
            elif Email.endswith('@.com'):
                print('Invalid Email: expecting e.g "@gmail.com"')
                return EMAIL()
            elif not (Email.endswith('.com')):
                print('invalid Email: expecting ".com"')
                return EMAIL()
            elif Email.startswith('@'):
                print('Invalid Email: no email name ')
                return EMAIL()
        email.append(Email)
    EMAIL()


    def SEX():
        print('''Gender\n  _____________
        M for male
        F for female
        ''')
        SexOption = input('enter Gender: ').lstrip()
        if SexOption == 'M'.lower():
            Sex = 'Male'
        elif SexOption == 'F'.lower():
            Sex = 'Female'
        else:
            print('invalid character e.g M for male ,F for female')
            return SEX()
        sex.append(Sex)
    SEX()


    def PhoneNumber():
        try:
            phoneNumber = int(input('enter your phone number: '))
            if len(str(phoneNumber)) < 11:
                print('phone number length must be 11')
            elif len(str(phoneNumber)) >11:
                print('phone number length must be 11')
        except:
            print('only numbers accepted')
            return PhoneNumber()
        phonenumber.append(phoneNumber)
    PhoneNumber()


    def ADDRESS():
        Address = input('enter Address: ').lstrip()
        address.append(Address)
    ADDRESS()


    def AccountType():
        print('\t  Account Type\n\t___________________'.expandtabs(1))
        print("""
        1) Current account
        2) Savings account
        """)

        accountTypeOption = int(input('enter option: '))
        if accountTypeOption == 1:
            accountType = 'Current Account'
        elif accountTypeOption == 2:
            accountType = 'Savings Account'
        else:
            print('invalid option')
            return AccountType()
        accounttype.append(accountType)
    AccountType()

    def AccountNumber():
        for number in range(10):
            accountNumberGenerator = random.randint(0, 9)
            accountnumber.append(accountNumberGenerator)
        '''accountNumber_x = ""
        for i in accountNumber:
            accountNumber_x+=str(i)+""'''

    AccountNumber()

    def bankVerificationNumber():
        for number in range(10):
            bankVerificationNumberGenerator = random.randint(0, 9)
            bvn.append(bankVerificationNumberGenerator)
        '''accountNumber_x = ""
        for i in accountNumber:
            accountNumber_x+=str(i)+""'''

    bankVerificationNumber()

    def UserPin():
        try:
            userPin = int(input('create your pin: '))
            if len(str(userPin)) < 4:
                print('pin length must be 4')
            elif len(str(userPin)) >10:
                print('pin length must be 4')

        except:
            print('only numbers accepted')
            return UserPin()
        userpin.append(userPin)
    UserPin()

    def submit():
        firstname_x = ""
        for i in firstname:
            firstname_x += str(i) + ""

        lastname_x = ""
        for i in lastname:
            lastname_x += str(i) + ""

        email_x = ""
        for i in email:
            email_x += str(i) + ""

        sex_x = ""
        for i in sex:
            sex_x += str(i) + ""

        phonenumber_x = ""
        for i in phonenumber:
            phonenumber_x += str(i) + ""

        address_x = ""
        for i in address:
            address_x += str(i) + ""


        accounttype_x = ""
        for i in accounttype:
            accounttype_x += str(i) + ""

        accountnumber_x = ""
        for i in accountnumber:
            accountnumber_x += str(i) + ""

        bvn_x = ""
        for i in bvn:
            bvn_x += str(i) + ""

        userpin_x = ""
        for i in userpin:
            userpin_x += str(i) + ""






        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1',
                                      database='bankapp')
        mycursor = cnx.cursor()


        mycursor.execute(f'''select * from customers_profile where mail = '{email_x}' ''')


        if mycursor.fetchall():
            print("Mail already used..try another mail")
            return sign_up()

        else:
            date = datetime.now()
            current_time = date.strftime("%Y:%m:%d %H:%M:%S")

            message = open(f'bank/{firstname_x + accountnumber_x[7:]}.txt','x')
            mesage = open(f'bank/{firstname_x + accountnumber_x[7:]}.txt', 'w')
            msg = mesage.write(f'''{current_time}\n{firstname_x +' '+ lastname_x} Your Account_number: {accountnumber_x}\nyour BVN: {bvn_x}\nFrom:NIIT BANK\n\n
            ''')

            mycursor.execute(f'''Insert into  customers_profile(firstname,lastname,mail,gender,phonenumber,address,accounttype,accountnumber,bvn,user_pin,create_date)
                                VALUES('{firstname_x}','{lastname_x}','{email_x}','{sex_x}',{int(phonenumber_x)},'{address_x}','{accounttype_x}',{int(accountnumber_x)},{int(bvn_x)},{int(userpin_x)},'{current_time}')''')
            cnx.commit()
        import profile

    submit()

sign_up()
