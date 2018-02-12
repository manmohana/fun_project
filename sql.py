import logging

from sqlalchemy import *
from sqlalchemy.sql import select, column
from sqlalchemy_utils import database_exists, create_database

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

class User(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.metadata = MetaData()

    def __call__(self, db, table, data):
        try:
            db = self.create_database(db)
            table = self.create_table(db, table)
            conn = db.connect()
            self.insert_into_table(conn, table, data)
            self. retrive_users(conn, table)
            self.retrive_male_over_40(conn, table)
        except Exception as e:
            self.logger.warning(e)

    def create_database(self, db_name):
        '''
        Create Database with param
        '''
        engine = create_engine("mysql+mysqldb://root@localhost/{mydb}".format(mydb=db_name))
        if not database_exists(engine.url):
            create_database(engine.url)
        return engine

    def create_table(self, engine, table):
        '''
        Create a table
        '''
        user = Table(table, self.metadata,
                     Column('user_id', Integer, primary_key=True),
                     Column('name', String(40)),
                     Column('age', Integer),
                     Column('gender', String(5)),
                    )
        user.create(engine)
        return user

    def insert_into_table(self,conn, table, data):
        '''
        Insert the list of dict into table
        '''
        conn.execute(table.insert(), data)

    def retrive_users(self, conn, table):
        '''
        prints users in table
        '''
        s = select([table.c.name])
        result = conn.execute(s)
        self.logger.info('------------------------- users----------------------------')
        for row in result:
            print row
    
    def retrive_male_by_age(self, conn, table):
        '''
        prints users name where age greater than age
        '''
        s = select([table.c.name]).where(table.c.age>40)
        result = conn.execute(s)
        self.logger.info('------------------------- user greater than 40----------------------------')
        for row in result:
            print row

if __name__ == "__main__":
    data = [
        {'user_id': 1, 'name' : 'Alex', 'gender' : 'M', 'age' : 27},
        {'user_id': 2, 'name' : 'Louis', 'gender' : 'M', 'age' : 42},
        {'user_id': 3, 'name' : 'Andrew', 'gender' : 'M','age' : 31},
        {'user_id': 4, 'name' : 'Joris', 'gender' : 'M','age' : 29},
        ]
    execute_task = User()
    execute_task('user', 'users', data)