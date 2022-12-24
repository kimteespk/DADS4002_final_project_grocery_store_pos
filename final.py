import mysql.connector
#from getpass import getpass
from matplotlib import pyplot as plt
import pandas as pd
import config # ไฟล์ config.py ที่จะเก็บ user, pwd, port สำหรับเชื่อมต่อ db
from datetime import datetime #import datetime for get now in transac



"""
SQL Command หลักที่จะใช้ในการ Insert ข้อมูลเข้า DB
"""
# Insert ข้อมูลเข้า Customer table ในตอนสมัครสมาชิก
cmd01 = """INSERT INTO customer (cus_name, cus_gender, cus_birth)\
        VALUES (%s,%s,STR_TO_DATE(%s,'%d-%m-%Y'))"""
# Insert ข้อมูลเข้า Product table เมื่อเพิ่มสินค้าใหม่
cmd02 = """INSERT INTO product (prod_name, prod_price, cat_id, prod_discount) \
        VALUES (%s,%s,%s,%s)"""
# Insert ข้อมูลเข้า Transactions table เมื่อมีการซื้อสินค้า
cmd03 = "INSERT INTO transactions (bsk_id, prod_id, qty, date, hour, cus_id) \
        VALUES (%s,%s,%s,STR_TO_DATE(%s,'%d-%m-%Y'),%s,%s)"



def backup():
    """Function สำหรับการ Backup ข้อมูลลงเป็นไฟล์ CSV โดยการใช้ fucntion read_sql, to_csv ของ pandas"""
    # customer table
    command_customer = "SELECT * FROM customer" # 
    df_customer = pd.read_sql(command_customer, my_db)
    df_customer.to_csv("customer.csv", index=False, header=False)

    # product table
    command_product = "SELECT * FROM product"
    df_product = pd.read_sql(command_product, my_db)
    df_product.to_csv("product.csv", index=False, header=False)

    # transaction table
    command_transactions = "SELECT * FROM transactions"
    df_transactions = pd.read_sql(command_transactions, my_db)
    df_transactions.to_csv("transaction.csv", index=False, header=False)

    # category table
    command_category = "SELECT * FROM category"
    df_category = pd.read_sql(command_category, my_db)
    df_category.to_csv("category.csv", index=False, header=False)


def db_connect():
    """Function สำหรับเชื่อต่อ DB """
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
    """Function สำหรับสมัครสมาชิกใหม่ จะถูกเรียกจาก input หลัก และมาเก็บ input รวมถึงการ insert เข้า db"""
    global cmd01
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


def register_prod():
    """Function สำหรับการลงทะเบียนสินค้าใหม่"""
    global cmd02
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


def trade_id(basket_id, member):
    """Function สำหรับซื้อสินค้า"""
    global cmd03
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

            # Get datetime automaticlly ด้วย datetime.now() จาก datetime lib
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
    """Function สำหรับการแก้ไขส่วนลดสำหรับสมาชิก ใช้สำหรับจะแก้ไขเมื่อสินค้าอยู่ใน DB อยู่แล้ว"""
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
    
    
def plot_function1(): # ฟังชันค์สำหรับพอท เริ่มตั้งแต่ sql command จนได้ข้อมูล จนถึงโชรูป plt.show()
    print('Graph 1 plotted')

    sql_commands = """SELECT
                            hour,
                            ROUND(sum(sale), 2) AS total_sale
                        FROM
                        (SELECT 
                            t.hour,
                            CASE 
                                WHEN t.cus_id IS NULL THEN ROUND(p.prod_price*t.qty, 2)
                                ELSE ROUND(p.prod_price*p.prod_discount*t.qty, 2)
                                END as sale
                        FROM product as p
                        INNER JOIN transactions as t
                        USING (prod_id)) t
                        GROUP BY hour
                        ORDER BY hour;"""

    df = pd.read_sql(sql_commands, my_db)

    plt.plot(df['hour'], df['total_sale'])
    plt.title('Total Sale by hour')
    plt.xlabel('Hour')
    plt.ylabel('Sale')
    plt.show()


def plot_function2():
    print('Graph 2 plotted')

    sql_commands1 = """SELECT
                            prod_name,
                            ROUND(SUM(sale), 2) as total_sale
                        FROM
                        (SELECT 
                            p.prod_name,
                            CASE 
                                WHEN t.cus_id IS NULL THEN ROUND(p.prod_price*t.qty, 2)
                                ELSE ROUND(p.prod_price*p.prod_discount*t.qty, 2)
                                END as sale
                        FROM product as p
                        INNER JOIN transactions as t
                        USING (prod_id)
                        WHERE t.cus_id IS NOT NULL) t
                        GROUP BY prod_name
                        ORDER BY total_sale DESC
                        LIMIT 10;"""

    df_member = pd.read_sql(sql_commands1, my_db) # raed_sq(command, db_object)

    sql_commands2 = """SELECT
                            prod_name,
                            ROUND(SUM(sale), 2) as total_sale
                        FROM
                        (SELECT 
                            p.prod_name,
                            CASE 
                                WHEN t.cus_id IS NULL THEN ROUND(p.prod_price*t.qty, 2)
                                ELSE ROUND(p.prod_price*p.prod_discount*t.qty, 2)
                                END as sale
                        FROM product as p
                        INNER JOIN transactions as t
                        USING (prod_id)
                        WHERE t.cus_id IS NULL) t
                        GROUP BY prod_name
                        ORDER BY total_sale DESC
                        LIMIT 10;"""

    df_nonmember = pd.read_sql(sql_commands2, my_db)

    fig = plt.figure(figsize = (10, 5))

    plt.subplot(1, 2, 1)
    plt.bar(df_member['prod_name'], df_member['total_sale'])
    plt.xticks(rotation=90)
    plt.title('Most Spending Product by Member')
    plt.xlabel('Product')
    plt.ylabel('Sale')


    plt.subplot(1, 2, 2)
    plt.bar(df_nonmember['prod_name'], df_nonmember['total_sale'])
    plt.xticks(rotation=90)
    plt.title('Most Spending Product by Non-Member')
    plt.xlabel('Product')
    plt.ylabel('Sale')

    plt.show()

def plot_function3():
    print('Graph 3 plotted')
    sql_commands = """SELECT
                        prod_name,
                        ROUND(SUM(sale), 2) as total_sale
                    FROM
                    (SELECT 
                        t.prod_id,
                        CASE 
                            WHEN t.cus_id IS NULL THEN ROUND(p.prod_price*t.qty, 2)
                            ELSE ROUND(p.prod_price*p.prod_discount*t.qty, 2)
                            END as sale
                    FROM product as p
                    INNER JOIN transactions as t
                    USING (prod_id)) t
                    INNER JOIN product USING (prod_id)
                    GROUP BY prod_id
                    ORDER BY total_sale DESC
                    LIMIT 10;"""

    df = pd.read_sql(sql_commands, my_db)
    df['prod_name'] = df['prod_name'].astype(str)

    plt.bar(df['prod_name'], df['total_sale'])
    plt.title('Best Sales Product')
    plt.xticks(rotation=90)
    plt.xlabel('Product name')
    plt.ylabel('Sale')
    plt.show()

def plot_function4():
    print('Graph 4 plotted')

    sql_commands = """SELECT
                        cus_id,
                        ROUND(SUM(sale), 2) as total_sale
                    FROM
                    (SELECT 
                        t.cus_id,
                        CASE 
                            WHEN t.cus_id IS NULL THEN ROUND(p.prod_price*t.qty, 2)
                            ELSE ROUND(p.prod_price*p.prod_discount*t.qty, 2)
                            END as sale
                    FROM product as p
                    INNER JOIN transactions as t
                    USING (prod_id)) t
                    GROUP BY cus_id
                    ORDER BY total_sale DESC
                    LIMIT 10;"""

    df = pd.read_sql(sql_commands, my_db)
    df['cus_id'] = df['cus_id'].astype(str)

    plt.bar(df['cus_id'], df['total_sale'])
    plt.title('Most Spending Customer')
    plt.xlabel('Customer ID')
    plt.ylabel('Sale')
    plt.show()

def analytics():

    ##### Input Zone ####
    command = input('Enter (1/2/3/4) to plot, (q) to exit:') # รับ input ใน function เลยจะได้เรียกซ้ำง่ายๆ
    if command == 'q': # เคลียเคสออกก่อน จะได้จบเร็วๆ
        return
    try: # ใช้ try เผื่อใส่ผิด จะได้ raise ให้มันเรียกฟังชั่นซ้ำ
        command = int(command) 
        if command > 4 or command < 1: # มากกว่า 3 ก็คือ invalid, raise ให้ไปหา ส่วนที่เรียกฟังชันซ้ำ
            raise Exception
    except Exception : # ส่วนที่เรียกฟังชั้นซ้ำ เวลาใสผิด จะได้มารวามอันเดียว
        print('Invalid command, Enter again')
        analytics()
    
    # เอาฟังค์ชันสำหรับ plot แต่ละกราฟ มาใส่เป็น value ของ dict ไม่ต้องใส่() เพราะแค่เซ็ตตัวแปร
    command_dict = {
        1: plot_function1,
        2: plot_function2,
        3: plot_function3,
        4: plot_function4
    }
    command_dict[command]() # เรียกใช้ function ใน dict

    #### Plot more graph ####
    plot_more = input('Plot more graph (y) otherwise exit:').lower()
    if plot_more == 'y':
        analytics()


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
    """Function สำหรับดึง basket id ล่าสุดมาสำหรับการซื้อสินค้าใหม่ในแต่ละ transaction"""
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

            # Option 02 : Register new product ID
            elif x == 2:
                register_prod()

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
                    
                sum_sale(basket_id) # calculate total amount


            # Option 04 : Data Analytics

            elif x == 4:
                analytics()

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

backup() # backup ไป csv ก่อนจบการทำงานโปรแกรม

my_cursor.close()
my_db.close()
