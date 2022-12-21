import mysql.connector
from getpass import getpass
import pandas as pd

# TODO Restructure code
    # TODO Change all input commanding body, to be in each there function
    # TODO Input just string
# TODO un important code
    # TODO Remove all writeing sql comamnd
# TODO Change str to tuple
# TODO Backup database


cmd01 = """INSERT INTO customer (cus_name,cus_gender,cus_birth)\
        VALUES (%s,%s,STR_TO_DATE(%s,'%d-%m-%Y'))"""
cmd02 = "INSERT INTO product (prod_id,prod_name,prod_price,prod_cat,prod_discount) \
        VALUES (%s,%s,%s,%s,%s)"
cmd03 = "INSERT INTO transaction (bsk_id,bsk_prod_id,bsk_qnt,bsk_date,bsk_hour,bsk_cus_id) \
        VALUES (%s,%s,%s,%s,%s,%s)"

def sql_execute(command_type, ):
    #if command_type == 'customer':
        # process here
    #e
    return
    

def db_connect():
    global my_db
    global my_cursor
    while True:
        my_db, my_cursor = None, None
        try:
            my_db = mysql.connector.connect(
                    host='localhost',
                    user=user,
                    password=pwd,
                    port='5500',
                    database='mystore')
            my_cursor = my_db.cursor()
            print('Successfully connected to database')

        except Exception as e:
            print('something went wrong while attempting to connect the database.')
            if my_db is not None or my_cursor is not None:
                my_db.rollback()
            print(f'>>> Error {e}')
        if my_db is not None:
            break



def register_cus():
    while True:
        try:
            #print('input customer ID : \n')
            # TODO dont get, auto increasing from db function
            c_id = 100
            c_name = 'kimtee'
            c_surname = 'eiei'
            # TODO m of male
            c_gender = 'male'
            c_birth_day = 16
            c_birth_month = 5
            c_birth_year = 1996
            x1_op = input(
                            'do you want to confirm input? (y/n) : ').lower()
            # c_id = int(float(input('Customer ID : ')))
            # c_name = input('Customer Name : ')
            # c_surname = input('Customer Surname : ')
            # # TODO m of male
            # c_gender = input('Customer Gender (male/female) : ')
            # c_birth_day = int(float(input('The day of birth (Only) : ')))
            # c_birth_month = int(float(input('The month of birth as number :')))
            # c_birth_year = int(float(input('The year of birth : ')))
            # x1_op = input(
            #                 'do you want to confirm input? (y/n) : ').lower()
            command =  (f'{c_name} {c_surname}',c_gender,f'{c_birth_day}-{c_birth_month}-{c_birth_year}')
            # ! WHAT IF [NO]
            if x1_op == 'y':
                my_cursor.execute(cmd01, command)
                my_db.commit()
            else:
                break
        except Exception as e:
            print(e)
            print('wrong in put, please try again.')
    return f"({c_id},{c_name} {c_surname},{c_gender},{c_birth_day}-{c_birth_month}-{c_birth_year});"


def register_prod():
    while True:
        try:
            p_id = int(float(input('Product ID : ')))
            p_name = input('Product Name : ')
            p_price = int(float(input('Product Price : ')))
            p_cat = int(input('Category : '))
            p_discount = 1-((float(input('Discount rate(%) : ')))/100)

        except Exception:
            print('wrong in put, please try again.')
        else:
            break
    return f'({p_id},{p_name},{p_price},{p_cat},{p_discount});'


def trade_id():
    while True:
        try:
            bsk_id = int(float(input('Transaction ID : ')))
            bsk_prod_id = int(float(input('Product ID : ')))
            bsk_qnt = (int(input('Quantity : ')))
            bsk_day = int(float(input('The day of Transaction (Only) : ')))
            bsk_month = int(float(input('The month of Transaction :')))
            bsk_year = int(float(input('The year of Transaction : ')))
            bsk_hour = int(
                float(input('The time of Transaction (between : 0-23) : ')))
            if (bsk_hour < 0) or (bsk_hour > 23):
                raise ValueError
            bsk_cus_id = int(float(input('Customer ID : ')))
        except Exception:
            print('wrong input, please try again.')
        else:
            break
    return f"({bsk_id},{bsk_prod_id},{bsk_qnt},{bsk_day}-{bsk_month}-{bsk_year},{bsk_hour},{bsk_cus_id});"


def discount_ud():
    try:
        new_discount = int(input('New discount (%) : '))
        w_prod_id = int(input('Product ID : '))
    except Exception as e:
        print(e)
        print('Wrong input, please try again.')
        discount_ud()
        
    # TODO execute sql command
    return f"UPDATE product SET prod_discount = {1-(new_discount)/100} WHERE prod_id = {w_prod_id}"




# user = input('User name : ')
# pwd = getpass('Password : ')
user = 'root'
pwd = '1249'
db_connect()

while True:
    print('\n---SHOP OPEN---\n\n')
    try:
        print('please select the menu [0] to start, [9] to close :')
        choice = int(input('your input : '))
        if choice == 0:

                # Start Main Menu
                print('\n---WELCOME TO GIFT SHOP---\n\n \
                please select the option below :\n\n \
                    1 : Register new customer ID \n \
                    2 : Register new pruduct ID \n\n \
                    3 : Trading operation \n\n \
                    4 : Data analytics \n \
                    5 : Update discount \n\n \
                    6 : Exit the program.\n')

                x = input('type your command here : ')


                f = open(".\sql_backup_00.txt", mode='w', encoding='utf-8')


                # Option 01 : Register customer ID
                if x == '1':                
                    command_01_0 = register_cus()
                    #f.writelines('customer registeration : ', command_01_0, '\n'])

                # Option 02 : Register new product ID
                elif x == 2:
                    while True:
                        print('input product ID : \n')
                        command_02 = register_prod()
                        x2_op = input(
                            'do you want to confirm input? (y/n) : ').lower()
                        if x2_op == 'y':
                            break
                        else:
                            continue
                    my_cursor.execute(cmd02, command_02)
                    f.writelines(
                        ['product registeration : ', command_02, '\n'])
                    continue

                # Option 03 : Trading Operation

                elif x == 3:
                    while True:
                        ans = input('Are you a member? (y/n) : ').lower()
                        if ans == 'y':
                            command_03 = trade_id()
                        elif ans == 'n':
                            ask = input(
                                'Do you want to Register ? (y/n) : ').lower()
                            if ask == 'y':
                                command_01_1 = register_cus()
                                print('Successfully registered.')
                                command_03 = trade_id()
                            elif ask != 'n':
                                break
                            elif ask == 'n':
                                command_03 = trade_id()
                        else:
                            break
                        print('input Transaction ID : \n')
                        command_03 = trade_id()

                        x3_op = input(
                            'do you want to confirm input? (y/n) : ').lower()
                        if x3_op == 'y':
                            break
                        else:
                            continue
                    my_cursor.execute(cmd01, command_01_1)
                    f.writelines(
                        ['customer registeration : ', command_01_1, '\n'])
                    my_cursor.execute(cmd03, command_03)
                    f.writelines(['Transaction records : ', command_03, '\n'])
                    continue

                # Option 04 : Data Analytics

                elif x == 4:
                    pass

                # Option 05 : Update Discount

                elif x == 5:
                    cmd05 = discount_ud()
                    my_cursor.execute(cmd05)

                # Option 06 : Quit

                elif (x == 6):
                    f.close()
                    print('you are now move back to menu')
                    break
                else:
                    print('wrong input, please try again')
                    continue

        elif choice == 9:
            print("\n---SHOP CLOSED---\n")
            # backup data function call
            break
    except Exception as e:
        print(e)
        print('Enter command again')


my_cursor.close()
my_db.close()