from sqlalchemy import Column, Integer, String, Boolean
from db import Base
from db import engine


#Create Bank object from data in bank table
#Todo: Add more variables to each bank such as minimum cash required, number of employees, and number of cash available
class BankTable(Base):
    __tablename__='bank'
    branch_id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    min_cash = Column(Integer)
    num_employees = Column(Integer)

#Create employee object based on data from employee table
class EmployeeTable(Base):
    __tablename__='employee'
    employee_id = Column(Integer, primary_key=True)
    branch_id = Column(Integer)


def main():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main()

