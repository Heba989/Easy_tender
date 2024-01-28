from os import getenv
import pymssql as sql
import logging
from dotenv import load_dotenv

# define constant
DOTENV_FILE = '.env'

# loading '.env' file
load_dotenv(verbose=True)
server = getenv("servername")
server_user = getenv('serverusername')
password = getenv('serverpassword')
database_name = "Easy_Tender"


# create database class for the project
class EasyTender():
    """
    The class initialize the connection to database
    data_base name : "Easy_Tender"
    """
    # initialize function that initiate the connection to database
    def __init__(self):
        self.connection = sql.connect(server=server,
                                      user=server_user,
                                      password=password,
                                      database='Easy_Tender',
                                      as_dict=True)
        self.cursor = self.connection.cursor()
        #self.cursor.execute("PRAGMA Journal_mode=WAL")
        self.connection.commit()

    def create_table(self, table_name, comp):
        query = f"CREATE TABLE {table_name}({comp});"
        self.cursor.execute(query)
        self.connection.commit()

    def close_conn(self):
        self.connection.close()


class client(EasyTender):
    def __init__(self):
        super().__init__()
        self.table_name = 'Client'

    def query_client(self):
        """
        :return: feature of the client
        """
        query = f'SELECT * From {self.table_name};'
        self.cursor.execute(query)
        return self.cursor.fetchall()


class user(EasyTender):
    def __init__(self):
        super().__init__()
        self.table_name = 'User'

    def list_all(self):
        """
        :return: list of all users in database
        """
        query = f'SELECT * From {self.table_name};'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def retrieve_user(self, condition, value):
        """
        this function assume and operation between conditions
        :param condition: list of string table names
        :param value: list of values
        :return: a list of users where all condition are true
        """
        # only one condition
        if len(condition) == 1:
            where_statement = f'WHERE {condition[0]}={value[0]}'
        # case of multiple condition
        elif not None:
            where_statement = ""
            for cond in condition:
                where_statement.join(cond, value[condition.index(cond)])
                if condition.index(cond) < len(condition)-1:
                    where_statement.join('AND')
        # complete the query
        query = f'SELECT * From {self.table_name};'.join(where_statement)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def edit_user(self, user_id, col, new_value):
        query = (f"UPDATE {self.table_name}"
                 f"SET {col} = {new_value}, WHERE User_ID = {user_id};")
        self.cursor.execute(query)
        self.connection.commit()
        #TODO: edit the return message
        return 'success'
