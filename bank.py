
import time
from datetime import datetime

now = datetime.now()
date_time = now.strftime("%d/%m/%y %H:%M:%S")


acct_number = 202100100
pin = 9919
account_name = 'olamide'.capitalize()
Balance = 20000000
try:
    def login():
        print('      Login\n____________________')
        account_number = int(input('enter your account number: '))
        login_pin = int(input('enter your pin: '))
        if account_number == acct_number and login_pin == pin:
            print('\nLogged in\n')

        else:
            print('incorrect password. try again\n')
            return login()



        def option():
            print('    Profile\n_________________')
            print(f'account_name: {account_name}\naccount_number: {acct_number}\nBalance: {Balance}\n')

            def others():
                time.sleep(3)
                print('       Options\n    ________________')
                print('1) Widthraw press W\n2) Transfer press T\n3) Deposit press D\n4) Report an issue press R')
                choose = str(input('\nwhat did you want to do? '))
                if choose == 'W'.lower():
                    try:
                        def withdraw():
                            print('\n         Withdrawal Option\n    _________________________')
                            print('   How much did you want to withdraw')
                            withdaw_option = int(input('1 for 500\n2 for 1000\n3 for 5000\n4 for 10000\n5 for 20000\n6 for others\n7 Back to profile\n\nchoose:   '))
                            print('________________\n')
                            if withdaw_option == 1 and Balance > 500:
                                print('      Transaction Result\n    ________________________')
                                print('Reuslt: Withdraw sucessfull')
                                print('Amount Widthraw: 500')
                                print(f'time of withdrawal: {date_time}')
                                print(f'Remaining Balance: {Balance - 500}\n')
                                return print(
                                    f'    Profile\n_________________\naccount_name: {account_name}\naccount_number: {acct_number}\nBalance: {Balance - 500}\n'), others()

                            elif withdaw_option == 2 and Balance > 1000:
                                print('      Transaction Result\n    ________________________')
                                print('Reuslt: Withdraw sucessfull')
                                print('Amount Widthraw: 1000')
                                print(f'time of withdrawal: {date_time}')
                                print(f'Balance: {Balance - 1000}\n')
                                return print(
                                    f'    Profile\n_________________\naccount_name: {account_name}\naccount_number: {acct_number}\nBalance: {Balance - 1000}\n'), others()

                            elif withdaw_option == 3 and Balance > 5000:
                                print('      Transaction Result\n    ________________________')
                                print('Reuslt: Withdraw sucessfull')
                                print('Amount Widthraw: 5000')
                                print(f'time of withdrawal: {date_time}')
                                print(f'Balance: {Balance - 5000}\n')
                                return print(
                                    f'    Profile\n_________________\naccount_name: {account_name}\naccount_number: {acct_number}\nBalance: {Balance - 5000}\n'), others()

                            elif withdaw_option == 4 and Balance > 10000:
                                print('      Transaction Result\n    ________________________')
                                print('Reuslt: Withdraw sucessfull')
                                print('Amount Widthraw: 10000')
                                print(f'time of withdrawal: {date_time}')
                                print(f'Balance: {Balance - 10000}\n')
                                return print(
                                    f'    Profile\n_________________\naccount_name: {account_name}\naccount_number: {acct_number}\nBalance: {Balance - 10000}\n'), others()

                            elif withdaw_option == 5 and Balance > 20000:
                                print('      Transaction Result\n    ________________________')
                                print('Reuslt: Withdraw sucessfull')
                                print('Amount Widthraw: 20000')
                                print(f'time of withdrawal: {date_time}')
                                print(f'Balance: {Balance - 20000}\n')
                                return print(
                                    f'    Profile\n_________________\naccount_name: {account_name}\naccount_number: {acct_number}\nBalance: {Balance - 20000}\n'), others()
                            elif withdaw_option == 6:
                                withdrawal_amount = float(input('enter amount you want to withdraw: '))
                                if Balance > withdrawal_amount:
                                    print('      Transaction Result\n    ________________________')
                                    print('Reuslt: Withdraw sucessfull')
                                    print(f'Amount Widthraw: {withdrawal_amount}')
                                    print(f'time of withdrawal: {date_time}')
                                    print(f'Balance: {Balance - withdrawal_amount}\n')
                                    return print(f'    Profile\n_________________\naccount_name: {account_name}\naccount_number: {acct_number}\nBalance: {Balance - withdrawal_amount}\n'), others()
                                else:
                                    print('only numbers are accepted')
                            elif withdaw_option == 7:
                                return option()

                            else:
                                print('      Transaction Result\n    ________________________')
                                print('Reuslt: Insufficient Fund')
                                print(f'Balance: {Balance}')
                                print(f'time of withdrawal: {date_time}')


                        withdraw()
                    except:
                        print('Select options correctly')
                        while True:
                            return withdraw()




                elif choose == 'T'.lower():
                    try:
                        def Transfer():
                            print('\n         Transfer Option\n    _________________________')
                            print(' How much did you want to Transfer')
                            transfer_amount = float(input('\n1)enter amount to transfer: '))
                            bank_name = str(input('\n2)enter bank name: '))
                            Raccount_number = int(input('\n3)enter reciever account number'))
                            if Balance > transfer_amount:
                                print('\n      Transaction Result\n    ________________________')
                                print('Reuslt: Transfer sucessfull')
                                print(f'Amount Transfer: {transfer_amount}')
                                print(f'sender_name: {account_name}')
                                print(f'receiver bank: {bank_name} ')
                                print(f'receiver account number: {Raccount_number}')
                                print(f'Balance: {Balance - transfer_amount}')
                                print(f'time of withdrawal: {date_time}')
                                return print(f'    Profile\n_________________\naccount_name: {account_name}\naccount_number: {acct_number}\nBalance: {Balance - transfer_amount}\n'), others()

                            else:
                                print('\n      Transaction Result\n    ________________________')
                                print('Reuslt: Transfer Not sucessfull')
                                print(f'Amount Transfer: {transfer_amount}')
                                print(f'Balance: {Balance}')
                                print('Insufficient fund')
                                print(f'time of withdrawal: {date_time}')

                        Transfer()
                    except:
                        print('only numbers accepted')
                        while True:
                            return Transfer()



                elif choose == 'D'.lower():
                    try:
                        def deposit():
                            print('\n         Deposit Option\n    _________________________')
                            print(' How much did you want to Deposit')
                            deposit_amount = float(input('\n1)enter amount to deposit: '))
                            if deposit_amount == deposit_amount:
                                print('\n      Transaction Result\n    ________________________')
                                print('Result: Deposit sucessfull')
                                print(f'name: {account_name}')
                                print(f'account number: {account_number}')
                                print(f'Amount_deposited: {deposit_amount}')
                                print(f'Balance: {Balance + deposit_amount}')
                                print(f'time of withdrawal: {date_time}')
                                return print(f'    Profile\n_________________\naccount_name: {account_name}\naccount_number: {acct_number}\nBalance: {Balance + deposit_amount}\n'), others()

                            else:
                                print('\n      Transaction Result\n    ________________________')
                                print('Reuslt: Deposit Not sucessfull')
                                print(f'time of withdrawal: {date_time}')


                        deposit()
                    except:
                        print('Only numbers are allowed!!')
                        while True:
                            return deposit()
                elif choose == 'R'.lower():
                    try:
                        def report():
                            issue = input('1)submit your issues/report')
                            if issue == issue:
                                print('Report submitted\nyou will be replied shortly\nThank you ....\n')
                                return print(f'    Profile\n_________________\naccount_name: {account_name}\naccount_number: {acct_number}\nBalance: {Balance}\n'), others()

                        report()
                    except:
                        print('Only alphabet are allowed!!')
                        while True:
                            return report()
                    else:
                        print('\nchoose your option correctly!!!!\n')
                        return others()


            others()

        option()

    login()
except:
    print('\nOnly numbers are allowed!!!\n')

finally:
    print('not allowed')


