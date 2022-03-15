from login import session
import mysql.connector
from datetime import datetime
import time

cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1',
                                      database='bankapp')
mycursor = cnx.cursor()

date = datetime.now()
current_time = date.strftime("%Y:%m:%d %H:%M:%S")
info_session = session()
session = list(info_session)
SESSION = {"id":session[0][0],"firstname":session[0][1],"lastname":session[0][2],"male":session[0][3],"gender":session[0][4],"phonenumber":session[0][5],"address":session[0][6],"accounttype":session[0][7],"accountnumber":session[0][8],"bvn":session[0][9],"userpin":session[0][10],"balance":session[0][11]}




def PROFILE():

    mycursor.execute(f'''select * from customers_profile where accountnumber = {SESSION.get("accountnumber")} and user_pin = {SESSION.get("userpin")}''')
    info_session = mycursor.fetchall()
    session = list(info_session)
    customer = {"id": session[0][0], "firstname": session[0][1], "lastname": session[0][2], "male": session[0][3],
               "gender": session[0][4], "phonenumber": session[0][5], "address": session[0][6],
               "accounttype": session[0][7], "accountnumber": session[0][8], "bvn": session[0][9], "balance": session[0][11]
               }

    print('\t  NIIT BANK\n\t______________'.expandtabs(17))
    print('\t  Profile\n\t______________'.expandtabs(7))
    print(f'Account Name: {customer.get("firstname")+" "+customer.get("lastname")}\nAccount Balance: {customer.get("balance")}\nAccount Number: {customer.get("accountnumber")}\nAccount Type: {customer.get("accounttype")}\nBVN: {customer.get("bvn")}')

    def others():
        time.sleep(3)
        print('       Options\n    ________________')
        print('1) Widthraw press W\n2) Transfer press T\n3) Deposit press D\n4) View  History press H')
        choose = str(input('\nwhat did you want to do? '))




        if choose == 'W'.lower():
            def withdraw():
                try:
                    print('\n         Withdrawal Option\n    _________________________')
                    print('   How much did you want to withdraw')
                    withdaw_option = int(input(
                        '1 for 500\n2 for 1000\n3 for 5000\n4 for 10000\n5 for 20000\n6 for others\n7 Back to profile\n\nchoose:   '))
                    print('________________\n')

                    if withdaw_option == 7:
                        return PROFILE()

                    elif withdaw_option == 6:
                        withdrawal_amount = float(input('enter amount you want to withdraw: '))
                        if customer.get("balance") > withdrawal_amount and not(withdrawal_amount > customer.get("balance")):
                            print('      Transaction Result\n    ________________________')
                            print('Reuslt: Withdraw sucessfull')
                            print(f'Amount Widthraw: {withdrawal_amount}')
                            print(f'time of withdrawal: {current_time}')
                            print(f'Balance: {customer.get("balance") - withdrawal_amount}\n')

                            mycursor.execute(
                                f'''update customers_profile
                                                        set worth = {customer.get("balance") - withdrawal_amount}
                                                        where accountnumber = {SESSION.get("accountnumber")}''')
                            cnx.commit()

                            mycursor.execute(f'''Insert into withdraw(account_number,amount_withraw,withdraw_date)
                                                                     VALUES({SESSION.get("accountnumber")},{withdrawal_amount},'{current_time}')''')
                            cnx.commit()
                            return PROFILE()
                        else:
                            print("insufficent fund")
                            return PROFILE()

                    elif withdaw_option == 5 and customer.get("balance") > 20000 and not(20000 > customer.get("balance")):
                        print('      Transaction Result\n    ________________________')
                        print('Reuslt: Withdraw sucessfull')
                        print('Amount Widthraw: 20000')
                        print(f'time of withdrawal: {current_time}')
                        print(f'Balance: {customer.get("balance") - 20000}\n')

                        mycursor.execute(
                            f'''update customers_profile
                                set worth = {customer.get("balance") - 20000}
                                where accountnumber = {SESSION.get("accountnumber")}''')
                        cnx.commit()

                        mycursor.execute(f'''Insert into withdraw(account_number,amount_withraw,withdraw_date)
                                             VALUES({SESSION.get("accountnumber")},{20000},'{current_time}')''')
                        cnx.commit()
                        return PROFILE()

                    elif withdaw_option == 4 and customer.get("balance") > 10000 and not(10000 > customer.get("balance")):
                        print('      Transaction Result\n    ________________________')
                        print('Reuslt: Withdraw sucessfull')
                        print('Amount Widthraw: 10000')
                        print(f'time of withdrawal: {current_time}')
                        print(f'Balance: {customer.get("balance") - 10000}\n')

                        mycursor.execute(
                            f'''update customers_profile
                                                    set worth = {customer.get("balance") - 10000}
                                                    where accountnumber = {SESSION.get("accountnumber")}''')
                        cnx.commit()

                        mycursor.execute(f'''Insert into withdraw(account_number,amount_withraw,withdraw_date)
                                                                 VALUES({SESSION.get("accountnumber")},{10000},'{current_time}')''')
                        cnx.commit()
                        return PROFILE()

                    elif withdaw_option == 3 and customer.get("balance") > 5000 and not(5000 > customer.get("balance")):
                        print('      Transaction Result\n    ________________________')
                        print('Reuslt: Withdraw sucessfull')
                        print('Amount Widthraw: 5000')
                        print(f'time of withdrawal: {current_time}')
                        print(f'Balance: {customer.get("balance") - 5000}\n')

                        mycursor.execute(
                            f'''update customers_profile
                                set worth = {customer.get("balance") - 5000}
                                where accountnumber = {SESSION.get("accountnumber")}''')
                        cnx.commit()

                        mycursor.execute(f'''Insert into withdraw(account_number,amount_withraw,withdraw_date)
                                             VALUES({SESSION.get("accountnumber")},{5000},'{current_time}')''')
                        cnx.commit()
                        return PROFILE()

                    elif withdaw_option == 2 and customer.get("balance") > 1000 and not(1000 > customer.get("balance")):
                        print('      Transaction Result\n    ________________________')
                        print('Reuslt: Withdraw sucessfull')
                        print('Amount Widthraw: 1000')
                        print(f'time of withdrawal: {current_time}')
                        print(f'Balance: {customer.get("balance") - 1000}\n')

                        mycursor.execute(
                            f'''update customers_profile
                                set worth = {SESSION.get("balance") - 1000}
                                where accountnumber = {SESSION.get("accountnumber")}''')
                        cnx.commit()

                        mycursor.execute(f'''Insert into withdraw(account_number,amount_withraw,withdraw_date)
                                             VALUES({SESSION.get("accountnumber")},{1000},'{current_time}')''')
                        cnx.commit()
                        return PROFILE()

                    elif withdaw_option == 1 and customer.get("balance") > 500 and not(500 > customer.get("balance")):
                        print('      Transaction Result\n    ________________________')
                        print('Reuslt: Withdraw sucessfull')
                        print('Amount Widthraw: 500')
                        print(f'time of withdrawal: {current_time}')
                        print(f'Remaining Balance: {SESSION.get("balance") - 500}\n')


                        mycursor.execute(
                            f'''update customers_profile
                                set worth = {SESSION.get("balance") - 500}
                                where accountnumber = {SESSION.get("accountnumber")}''')
                        cnx.commit()

                        mycursor.execute(f'''Insert into withdraw(account_number,amount_withraw,withdraw_date)
                                                                 VALUES({SESSION.get("accountnumber")},{500},'{current_time}')''')
                        cnx.commit()


                        return PROFILE()
                    else:
                        print("insufficent fund")
                        return PROFILE()
                except:
                    print("Invalid Input")
                    return withdraw()
            withdraw()
        elif choose == 'T'.lower():

            def Transfer():
                try:
                    print('\n         Transfer Option\n    _________________________')
                    print(' How much did you want to Transfer')
                    transfer_amount = float(input('\n1)enter amount to transfer: '))
                    recieverAccount = int(input('\n3)enter reciever account number'))
                    if customer.get("balance") > transfer_amount:
                        mycursor.execute(
                            f'''select * from customers_profile where accountnumber = {recieverAccount}''')
                        if mycursor.fetchall():
                            mycursor.execute(
                                f'''update customers_profile
                                    set worth = worth + {transfer_amount}
                                    where accountnumber = {recieverAccount}''')
                            cnx.commit()

                            mycursor.execute(
                                f'''update customers_profile
                                    set worth = worth - {transfer_amount}
                                    where accountnumber = {SESSION.get("accountnumber")}''')
                            cnx.commit()

                            mycursor.execute(
                                f'''insert into transfer(account_number,amount,reciever,transfer_date)
                                    VALUES({SESSION.get("accountnumber")},{transfer_amount},{recieverAccount},'{current_time}')''')
                            cnx.commit()


                        print('\n      Transaction Result\n    ________________________')
                        print('Reuslt: Transfer sucessfull')
                        print(f'Amount Transfer: {transfer_amount}')
                        print(f'receiver account number: {recieverAccount}')
                        print(f'Balance: {customer.get("balance") - transfer_amount}')
                        print(f'time of withdrawal: {current_time} ')
                        return PROFILE()
                    else:
                        print("Insufficient Fund")
                        return PROFILE()
                except:
                    print("Invalid Input")
                    return Transfer()
            Transfer()

        elif choose == 'D'.lower():

            def Deposit():
                try:
                    print('\n         Deposit Option\n    _________________________')
                    print(' How much did you want to Deposit')
                    deposit_amount = float(input('\n1)enter amount to deposit: '))
                    if deposit_amount == deposit_amount:

                        mycursor.execute(
                            f'''update customers_profile
                                set worth = worth + {deposit_amount}
                                where accountnumber = {SESSION.get("accountnumber")}''')
                        cnx.commit()



                        mycursor.execute(
                            f'''insert into deposit(account_number,deposit_amount,deposited_date)
                                                    VALUES({SESSION.get("accountnumber")},{deposit_amount},'{current_time}')''')
                        cnx.commit()
                        print('\n      Transaction Result\n    ________________________')
                        print('Result: Deposit sucessfull')
                        print(f'account number: {SESSION.get("accountnumber")}')
                        print(f'Amount_deposited: {deposit_amount}')
                        print(f'Balance: {customer.get("balance") + deposit_amount}')
                        print(f'time of withdrawal: {current_time}')
                        return PROFILE()
                except:
                    print("invalid input")
                    return Deposit()
            Deposit()
        elif choose == 'H'.lower():
            def History():

                mycursor.execute(
                    f'''select * from transfer where account_number = {SESSION.get("accountnumber")}''')
                allTransfers = mycursor.fetchall()
                print('Transfers')
                for transfers in allTransfers:
                    print(transfers)


                mycursor.execute(
                    f'''select * from deposit where account_number = {SESSION.get("accountnumber")}''')
                allDeposit = mycursor.fetchall()
                print("dposites")
                for deposit in allDeposit:
                    print(deposit)



                mycursor.execute(
                    f'''select * from withdraw where account_number = {SESSION.get("accountnumber")}''')
                allWithdraws =mycursor.fetchall()
                print("withdraw")
                for withdraw in allWithdraws:

                    print(withdraw)

            History()
        else:
            print("Invalid Input")
            return others()
    others()
PROFILE()
"""4731815885
    enter your pin: 3424"""

"""else:
                                print('\n      Transaction Result\n    ________________________')
                                print('Reuslt: Deposit Not sucessfull')
                                print(f'time of withdrawal: {date_time}')


   +                     deposit()
"""