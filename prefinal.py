import mysql.connector
from getpass import getpass
import pandas as pd
import config
from datetime import datetime #import datetime for get now in transac

# TODO Restructure code
# TODO Change all input commanding body, to be in each there function
# TODO Input just string
# TODO un important code
# TODO Remove all writeing sql comamnd
# TODO Change str to tuple
# TODO Backup database


cmd01 = """INSERT INTO customer (cus_name, cus_gender, cus_birth)\
        VALUES (%s,%s,STR_TO_DATE(%s,'%d-%m-%Y'))"""
cmd02 = """INSERT INTO product (prod_name, prod_price, cat_id, prod_discount) \
        VALUES (%s,%s,%s,%s)"""
cmd03 = "INSERT INTO transactions (bsk_id, prod_id, qty, date, hour, cus_id) \
        VALUES (%s,%s,%s,STR_TO_DATE(%s,'%d-%m-%Y'),%s,%s)"

# def sql_execute(command_type, ):
#     # if command_type == 'customer':
#     # process here
#     # e
#     return


def backup():
    # customer table
    command_customer = "SELECT * FROM customer"
    df_customer = pd.read_sql(command_customer, my_db)
    df_customer.to_csv("customer.csv", index=False, header=False)

    # product table
    command_product = "SELECT * FROM product"
    df_product = pd.read_sql(command_product, my_db)
    df_product.to_csv("product.csv", index=False, header=False)

    # transactions table
    command_transactions = "SELECT * FROM transactions"
    df_transactions = pd.read_sql(command_transactions, my_db)
    df_transactions.to_csv("transactions.csv", index=False, header=False)

    # category table
    command_category = "SELECT * FROM category"
    df_category = pd.read_sql(command_category, my_db)
    df_category.to_csv("category.csv", index=False, header=False)


def db_connect():
    global my_db
    global my_cursor
    while True:

        # user = input('User name : ')
        # pwd = getpass('Password : ')
        user = config.user
        pwd = config.pwd
        port = config.port

        my_db, my_cursor = None, None
        try:
            my_db = mysql.connector.connect(
                host='localhost',
                user=user,
                password=pwd,
                port=port,
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
            c_name = input('Customer Name : ')
            c_surname = input('Customer Surname : ')
            c_gender = input('Customer Gender (male/female) : ')
            c_birth_day = int(float(input('The day of birth (Only) : ')))
            c_birth_month = int(float(input('The month of birth as number :')))
            c_birth_year = int(float(input('The year of birth : ')))

            command = (f'{c_name} {c_surname}', c_gender,
                       f'{c_birth_day}-{c_birth_month}-{c_birth_year}')

            while True:
                confirm = input(
                    'do you want to confirm input? (y/n) : ').lower()
                if confirm == 'y':
                    my_cursor.execute(cmd01, command)
                    my_db.commit()
                    break
                if confirm == 'n':
                    break
                else:
                    print('please input (y/n) to confirm')
            if confirm == 'n':
                continue

        except Exception as e:
            print(e)
            print('wrong in put, please try again.')
        else:
            print('Successfully registered.')
            break

    # return f"({c_name} {c_surname},{c_gender},{c_birth_day}-{c_birth_month}-{c_birth_year});"


def register_prod():
    while True:
        try:
            p_name = input('Product Name : ')
            p_price = int(float(input('Product Price : ')))
            p_cat = int(input('Category ID : '))
            p_discount = 1-((float(input('Discount rate(%) : ')))/100)

            command = (p_name, p_price, p_cat, p_discount)

            while True:
                confirm = input(
                    'do you want to confirm input? (y/n) : ').lower()
                if confirm == 'y':
                    my_cursor.execute(cmd02, command)
                    my_db.commit()
                    break
                if confirm == 'n':
                    break
                else:
                    print('please input (y/n) to confirm')
            if confirm == 'n':
                continue

        except Exception as e:
            print(e)
            # print(e)
            print('wrong in put, please try again.')
        else:
            print('Successfully registered.')
            break
    # return f'({p_name},{p_price},{p_cat},{p_discount});'


def trade_id(basket_id):
    while True:
        try:
            bsk_id = basket_id
            bsk_prod_id = int(float(input('Product ID : ')))
            bsk_qnt = (int(input('Quantity : ')))
            # bsk_day = int(float(input('The day of Transaction (Only) : ')))
            # bsk_month = int(float(input('The month of Transaction :')))
            # bsk_year = int(float(input('The year of Transaction : ')))
            # bsk_hour = int(
            #     (input('The hour of Transaction (between : 0-23) : ')))

            # Get datetime automaticlly
            bsk_day = datetime.now().date().day
            bsk_month = datetime.now().date().month
            bsk_year = datetime.now().date().year
            bsk_hour = datetime.now().hour
            if (bsk_hour < 0) or (bsk_hour > 23):
                raise ValueError
            bsk_cus_id = int(float(input('Customer ID : ')))

            command = (bsk_id, bsk_prod_id, bsk_qnt,
                       f'{bsk_day}-{bsk_month}-{bsk_year}', bsk_hour, bsk_cus_id)

            while True:
                confirm = input(
                    'do you want to confirm input? (y/n) : ').lower()
                if confirm == 'y':
                    my_cursor.execute(cmd03, command)
                    my_db.commit()
                    break
                if confirm == 'n':
                    break
                else:
                    print('please input (y/n) to confirm')
            if confirm == 'n':
                continue

        except Exception as e:
            print(e)
            print('wrong input, please try again.')

        else:
            break

def trade_id(basket_id, member):
    while True:
        try:
            bsk_id = basket_id
            bsk_prod_id = int(float(input('Product ID : ')))
            bsk_qnt = (int(input('Quantity : ')))
            # bsk_day = int(float(input('The day of Transaction (Only) : ')))
            # bsk_month = int(float(input('The month of Transaction :')))
            # bsk_year = int(float(input('The year of Transaction : ')))
            # bsk_hour = int(
            #     (input('The hour of Transaction (between : 0-23) : ')))

            # Get datetime automaticlly
            bsk_day = datetime.now().date().day
            bsk_month = datetime.now().date().month
            bsk_year = datetime.now().date().year
            bsk_hour = datetime.now().hour

            if member == 'y':
                bsk_cus_id = int(float(input('Customer ID : ')))
                command = (bsk_id, bsk_prod_id, bsk_qnt,
                        f'{bsk_day}-{bsk_month}-{bsk_year}', bsk_hour, bsk_cus_id)
            elif member == 'n':
                cmd03 = "INSERT INTO transactions (bsk_id, prod_id, qty, date, hour) \
                        VALUES (%s,%s,%s,STR_TO_DATE(%s,'%d-%m-%Y'),%s)"
                command = (bsk_id, bsk_prod_id, bsk_qnt,
                        f'{bsk_day}-{bsk_month}-{bsk_year}', bsk_hour)

            while True:
                confirm = input(
                    'do you want to confirm input? (y/n) : ').lower()
                if confirm == 'y':
                    my_cursor.execute(cmd03, command)
                    my_db.commit()
                    break
                if confirm == 'n':
                    break
                else:
                    print('please input (y/n) to confirm')
            if confirm == 'n':
                continue

        except Exception as e:
            print(e)
            print('wrong input, please try again.')

        else:
            break


def discount_ud():
    while True:
        try:
            new_discount = 1 - float(input('New discount (%) : '))/100
            prod_id = int(input('Product ID : '))

            command = f"UPDATE product SET prod_discount = {new_discount} WHERE prod_id = {prod_id}"

            while True:
                confirm = input(
                    'do you want to confirm input? (y/n) : ').lower()
                if confirm == 'y':
                    my_cursor.execute(command)
                    my_db.commit()
                    break
                if confirm == 'n':
                    break
                else:
                    print('please input (y/n) to confirm')
            if confirm == 'n':
                continue

        except Exception as e:
            print(e)
            print('Wrong input, please try again.')
            discount_ud()
        else:
            print('Successfully updated.')
            break

    # TODO execute sql command
    # return f"UPDATE product SET prod_discount = {1-(new_discount)/100} WHERE prod_id = {w_prod_id}"
    
    
def plot_function1(): # ฟังชันค์สำหรับพอท เริ่มตั้งแต่ sql command จนได้ข้อมูล จนถึงโชรูป plt.show()
    print('Graph 1 plotted')
    # เขียน sql command
    # execute
    # commit
    # เซ็ตกราฟสำหรับพอท 
    # plot.show()
    return
def plot_function2():
    print('Graph 2 plotted')
    return
def plot_function3():
    print('Graph 3 plotted')
    return

def analytics():
    """ใช้เป็น Function ที่ไม่รับ param มา แล้วใช้การเก็บ input จากใน function ว่าจะ plot กราฟไหน
    เพื่อที่เมื่อที่ต้องการ plot เพิ่ม จะได้ทำ Recursive เรียกซ้ำอีกครั้ง มาถามหาว่าจะplot อะไรต่อ
    
    - โดยเริ่มแรกด้วยรับ input ละเคลียเคสทีจะออกจาก function หรือ เคสที่ใส่ input ผิด
    - เรียกใช้ dictโดยมี command เป็น key และมันจะเรียกฟังชันค์สำหรับ plot กรฟานั้นๆ
    - สุดท้าย ถ้าจะ plot ต่อ (y) ก็เรียกฟังค์ชันซ้ำอีกครั้ง
    """
    ##### Input Zone ####
    command = input('Enter (1/2/3) to plot, (q) to quit:') # รับ input ใน function เลยจะได้เรียกซ้ำง่ายๆ
    if command == 'q': # เคลียเคสออกก่อน จะได้จบเร็วๆ
        return
    try: # ใช้ try เผื่อใส่ผิด จะได้ raise ให้มันเรียกฟังชั่นซ้ำ
        command = int(command) 
        if command > 3: # มากกว่า 3 ก็คือ invalid, raise ให้ไปหา ส่วนที่เรียกฟังชันซ้ำ
            raise Exception
    except Exception: # ส่วนที่เรียกฟังชั้นซ้ำ เวลาใสผิด จะได้มารวามอันเดียว
        print('Invalid command, Enter again')
        analytics()
    
    # เอาฟังค์ชันสำหรับ plot แต่ละกราฟ มาใส่เป็น value ของ dict ไม่ต้องใส่() เพราะแค่เซ็ตตัวแปร
    command_dict = {
        1: plot_function1,
        2: plot_function2,
        3: plot_function3
    }
    command_dict[command]() # เรียกใช้ function ใน dict

    #### Plot more graph ####
    plot_more = input('Plot more graph (y) otherwise exit:').lower()
    if plot_more == 'y':
        analytics()
    
    return

def sum_sale(basket_id):

    print('Calculating total payment...')
    bsk_id = basket_id


    command = f"""SELECT SUM(sale) FROM
                (SELECT 
                    p.prod_price,
                    p.prod_discount,
                    t.qty,
                    t.cus_id,
                    CASE 
                        WHEN t.cus_id IS NULL THEN ROUND(p.prod_price*t.qty, 2)
                        ELSE ROUND(p.prod_price*p.prod_discount*t.qty, 2)
                        END as sale
                FROM product as p
                INNER JOIN transactions as t
                USING (prod_id)
                WHERE bsk_id = {bsk_id}) t"""
    
    my_cursor.execute(command)
    for x in my_cursor.fetchall():
        print(f'Total payment is {x[0]} Baht')

def last_bsk_id():
    command = """SELECT bsk_id FROM transactions ORDER BY bsk_id DESC LIMIT 1"""
    my_cursor.execute(command)
    for x in my_cursor.fetchall():
        return x[0]+1

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
                    2 : Register new product ID \n \
                    3 : Trading operation \n \
                    4 : Data analytics \n \
                    5 : Update discount \n \
                    6 : Exit the program.\n')

            x = int(input('type your command here : '))

            # Option 01 : Register customer ID
            if x == 1:
                register_cus()
                # f.writelines('customer registeration : ', command_01_0, '\n'])

            # Option 02 : Register new product ID
            elif x == 2:
                register_prod()
                # f.writelines(['product registeration : ', command_02, '\n'])

            # Option 03 : Trading Operation

            elif x == 3:
                basket_id = last_bsk_id()
                while True:
                    ans = input('Are you a member? (y/n) : ').lower()
                    if ans == 'y':
                        trade_id(basket_id, ans)
                        break
                    elif ans == 'n':
                        while True:
                            ask = input('Do you want to Register ? (y/n) : ').lower()
                            if ask == 'y':
                                register_cus()
                                trade_id(basket_id, ask)
                                break
                            elif ask == 'n':
                                trade_id(basket_id, ask)
                                break
                            else:
                                print('please input (y/n) to confirm')
                                continue
                        break
                    else:
                        print('please input (y/n) to confirm')
                        continue

                while True:
                    x = input('Do you want to buy more product ? (y/n): ')
                    if x == 'y':
                        trade_id(basket_id, ask)
                    elif x == 'n':
                        break
                    else:
                        print('please input (y/n) to confirm')
                        continue
                    
                sum_sale(basket_id)


            # Option 04 : Data Analytics

            elif x == 4:
                analytics()
                pass

            # Option 05 : Update Discount

            elif x == 5:
                discount_ud()

            # Option 06 : Quit

            elif x == 6:
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

backup()

my_cursor.close()
my_db.close()
