import sqlite3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


db = sqlite3.connect('banks.db')
cursor = db.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS bank(
        branch_id INTEGER PRIMARY KEY,
        amount INTEGER NOT NULL,
        min_cash INTEGER NOT NULL,
        num_employees INTEGER
        )
        ''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee(
        employee_id INTEGER PRIMARY KEY,
        branch_id INTEGER NOT NULL UNIQUE
        )
        ''')

db.commit()
cursor.close()
# cursor.execute("INSERT INTO employee VALUES(1, 2) ")
# cursor.execute("SELECT * FROM employee")
# result = cursor.fetchall()
# print(result)


engine = create_engine('sqlite:///banks.db', echo=True)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = session.query_property()

db_session = session()

# try:
#     # Try to create an engine to connect to the database
#     engine = create_engine('sqlite:///banks.db')
#     # If no exceptions are raised, the database was successfully created
#     print("Database was successfully created.")
# except sqlalchemy.exc.SQLAlchemyError as e:
#     # If an exception is raised, print the error message
#     print("Failed to create the database:", e)