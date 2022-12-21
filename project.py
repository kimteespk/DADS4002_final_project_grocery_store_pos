import mysql.connector
from getpass import getpass
import pandas as pd


# Access to Database
while True:
    try:
        user = input('User name : ')
        pwd = getpass('Password : ')

        my_db, my_cursor = None, None
        my_db = mysql.connector.connect(
            host='localhost',
            user=user,
            password=pwd,
            database='mystore')
        print('Successfully connected to database')

    except Exception as e:
        print('something went wrong while attempting to connect the database.')
        if my_db is not None:
            my_db.rollback()
        print(f'>>> Error {e}')

    finally:
        if my_db is not None:
            break

print('Database is now open.')

# Database_operation

my_cursor = my_db.cursor()

# function


def register_cus():
    while True:
        try:
            c_id = int(float(input('Customer ID : ')))
            c_name = input('Customer Name : ')
            c_surname = input('Customer Surname : ')
            c_gender = input('Customer Gender (male/female) : ')
            c_birth_day = int(float(input('The day of birth (Only) : ')))
            c_birth_month = int(float(input('The month of birth as number :')))
            c_birth_year = int(float(input('The year of birth : ')))
        except Exception:
            print('wrong in put, please try again.')
        else:
            break
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
    while True:
        try:
            new_discount = int(input('New discount (%) : '))
            w_prod_id = int(input('Product ID : '))
        except Exception:
            print('Wrong input, please try again.')
        else:
            break
    return f"UPDATE product SET prod_discount = {1-(new_discount)/100} WHERE prod_id = {w_prod_id}"


def sale_by_hour():
    pass

# Program Open


while True:
    print('\n---SHOP OPEN---\n\n')
    try:
        print('please select the menu : \n\n \
        0 : to start Shop Operation\n \
        OR \n \
        9 : to close the shop.\n')
        choice = int(input('your input : '))
        if choice == 0:

            # start loop

            while True:

                # Start Main Menu

                print('\n---WELCOME TO GIFT SHOP---\n\n \
                please select the option below :\n\n \
                    1 : Register new customer ID \n \
                    2 : Register new pruduct ID \n\n \
                    3 : Trading operation \n\n \
                    4 : Data analytics \n \
                    5 : Update discount \n\n \
                    6 : Exit the program.\n')
                try:
                    x = int(input('type your command here : '))
                except ValueError:
                    print('The input must be integer, please try again.')
                    continue
                except Exception:
                    print('Something is wrong, read the option and try again.')
                    continue

                # open backup log

                f = open(".\sql_backup_00.txt", mode='w', encoding='utf-8')

                # SQL_command

                cmd01 = "INSERT INTO customer (cus_id,cus_name,cus_gender,cus_birth)\
                        VALUES (%s,%s,%s,%s)"
                cmd02 = "INSERT INTO product (prod_id,prod_name,prod_price,cat_id,prod_discount) \
                        VALUES (%s,%s,%s,%s,%s)"
                cmd03 = "INSERT INTO transaction (bsk_id,prod_id,qty,date,bsk_hour,bsk_cus_id) \
                        VALUES (%s,%s,%s,%s,%s,%s)"

                # Option 01 : Register customer ID

                if x == 1:
                    while True:
                        print('input customer ID : \n')
                        command_01_0 = register_cus()
                        x1_op = input(
                            'do you want to confirm input? (y/n) : ').lower()
                        if x1_op == 'y':
                            break
                        else:
                            continue
                    my_cursor.execute(cmd01, command_01_0)
                    f.writelines(
                        ['customer registeration : ', command_01_0, '\n'])
                    continue

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
            break
        else:
            raise ValueError
    except ValueError:
        print('the input must be 1 or 9 , please try again.')
        continue
    except Exception:
        print('something is wrong about your input , please try again.')
        continue
    else:
        break


# close

my_db.close()
my_cursor.close()
print('Database is closed')
