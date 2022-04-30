""""
##############################################################################
#######             PROJECT NAME : DATABASE OBJECT                     #######
##############################################################################

                             Synopsis:
Script contains example of CRUD functions for simple inventory database
"""


# imports
import mysql.connector as db
import db_variable


# Base class
class BaseDatabase:
    # Create connection with db and cursor object
    def __init__(self):
        self.conn = db.connect(user=db_variable.USER, password=db_variable.PASSWORD,
                               host=db_variable.HOST, database=db_variable.DB_NAME)
        self.cur = self.conn.cursor()
        self.table = ''

    # read function
    def view(self):
        """
        Returns:
            object { dict }: dict with key as id
        """
        # read all records from desired table
        self.cur.execute(f'SELECT * from {self.table}')
        rows = self.cur.fetchall()
        return {key: values for key, *values in rows}


    # Delete function
    def delete(self, id):
        """
        Parameters:
            id { int }: id of desired record(row)
        """
        self.cur.execute(f'DELETE FROM {self.table} WHERE "{id}"')
        self.conn.commit()
    
    # Deconstructor kill connection with database
    def __del__(self):
        self.conn.close()

# Class containing install_db function
class Database_Installer(BaseDatabase):
    def __init__(self):
        super().__init__()

    ## install database
    def install_db(self):
        # check if table exists and delete it 
        sql_1 = 'DROP TABLE IF EXISTS customers'
        self.cur.execute(sql_1)
         
        sql_2 = "CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(100), password VARCHAR(100))"
        self.cur.execute(sql_2)
        self.conn.commit()
        print('Table *customers* Completed!')

        # check if table exists and delete it 
        sql_1 = 'DROP TABLE IF EXISTS customer_order'
        self.cur.execute(sql_1)
        # create new table
        sql_2 = "CREATE TABLE customer_order(id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, total FLOAT, products_list VARCHAR(128), timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        self.cur.execute(sql_2)
        self.conn.commit()
        print('Table *customer_order* Completed!')

        # check if table exists and delete it 
        sql_1 = 'DROP TABLE IF EXISTS stock'
        self.cur.execute(sql_1)
        # create new table
        sql_2 = "CREATE TABLE stock(id INT AUTO_INCREMENT PRIMARY KEY, product VARCHAR(128), trade_price INT, retail_price INT, stock INT, datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        self.cur.execute(sql_2)
        self.conn.commit()
        print('Table *stock* Completed!')


# Class for Customers table
class Customers(BaseDatabase):
    # constructor
    def __init__(self):
        super().__init__()
        self.table = 'customers'

    # create function
    def insert(self, username, password):
        """
        Parameters:
            username { str }: username
            password { str }: password
        """
        sql = f'INSERT INTO {self.table} (username, password) VALUES ("{username}","{password}")'
        self.cur.execute(sql)
        self.conn.commit()

    # update function
    def update(self, id, username, password):
        """
        Parameters: 
            id { int }: record id
            username { str }: username
            password { str }: password
        """
        sql = f'UPDATE {self.table} SET username="{username}", password="{password}" WHERE id="{id}"'
        self.cur.execute(sql)
        self.conn.commit()

# Class for customer placed orderds table
class Customer_order(BaseDatabase):
    # constructor
    def __init__(self):
        super().__init__()
        self.table = 'customer_order'

    # create function
    def insert(self, user_id, total, products_list):
        """
        Parameters:
            user_id { int }: customer id
            total { float } : total order value
            product_list { str }: list of products id
        """
        sql = f'INSERT INTO {self.table} (user_id, total, products_list) VALUES ("{user_id}","{total}","{products_list}")'
        self.cur.execute(sql)
        self.conn.commit()
    
    # update function
    def update(self, id, user_id, total, products_list):
        """
        Parameters:
            id { int }: order id
            user_id { int }: customer id
            total { float } : total order value
            product_list { str }: list of products id
        """
        sql = f'UPDATE {self.table} SET user_id="{user_id}", total="{total}", products_list="{products_list}" WHERE id="{id}"'
        self.cur.execute(sql)
        self.conn.commit()

# class for stock table
class Stock(BaseDatabase):
    #constructor
    def __init__(self):
        super().__init__()
        self.table = 'stock'

    # create function
    def insert(self, product, trade_price, retail_price, stock):
        """
        Parameters:
            product { str }: product name
            trade_price { float }: trade prize
            retail price { float }: retail prize
            stock { int }: amount avaiable in stock
        """
        sql = f'INSERT INTO {self.table} (product, trade_price, retail_price, stock) VALUES ("{product}","{trade_price}","{retail_price}","{stock}")'
        self.cur.execute(sql)
        self.conn.commit()

    # update function
    """
        Parameters:
            id { int }: product id
            product { str }: product name
            trade_price { float }: trade prize
            retail price { float }: retail prize
            stock { int }: amount avaiable in stock
        """
    def update(self, id, product, trade_price, retail_price, stock):
        sql = f'UPDATE {self.table} SET product="{product}", trade_prize="{trade_price}", retail_prize="{retail_price}", stock="{stock}" WHERE id="{id}"'
        self.cur.execute(sql)
        self.conn.commit()
