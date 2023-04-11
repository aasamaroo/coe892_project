from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from db import db_session
from model import EmployeeTable, BankTable

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#GET request that returns list of all employees
@app.get("/employees")
async def getEmployees():
    return db_session.query(EmployeeTable).all()

#Todo: create requests to Create, Read, Update, and Delete (CRUD) employees

#GET request to get employee by ID number
@app.get("/employees/{employee_id}")
async def getEmployeeByID(employee_id: int):
    employee = db_session.query(EmployeeTable). \
        filter(EmployeeTable.employee_id == employee_id).first()
    return employee


#POST request to create a new employee
@app.post("/employees")  # create a new employee
async def createEmployee(id: int, employee_id: int):
    employee = EmployeeTable()
    employee.employee_id = id
    employee.employee_id = employee_id
    db_session.add(employee)

    #Update Branch where employee got hired
    branch = db_session.query(BankTable). \
        filter(BankTable.branch_id == employee.branch_id).first()

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    branch.num_employees = branch.num_employees +1


    db_session.commit()
    return {"Success": True}


#DELETE request to delete an employee specified by ID
@app.delete("/employees/{employee_id}")  # discharge a employee
async def deleteEmployee(employee_id: int):
    print("employee_ID RECIEVED" + str(employee_id))
    employee = db_session.query(EmployeeTable). \
        filter(EmployeeTable.id == employee_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    #Update Branch where employee worked at
    branch = db_session.query(BankTable). \
        filter(BankTable.branch_id == employee.branch_id).first()

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    branch.num_employees = branch.num_employees - 1


    db_session.delete(employee)
    db_session.commit()
    return {"Success": True}

#PUT request to update the employee ID of an employee
@app.put("/employees/{employee_id}")
async def updateemployee(employee_id: int, branch_id: int):
    employee = db_session.query(EmployeeTable). \
        filter(EmployeeTable.employee_id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    #Update Old Branch
    branchOld = db_session.query(BankTable). \
        filter(BankTable.branch_id == employee.branch_id).first()

    if not branchOld:
        raise HTTPException(status_code=404, detail="Branch not found")

    branchOld.num_employees = branchOld.num_employees -1

    #Update New Branch
    employee.branch_id = branch_id

    branchNew = db_session.query(BankTable). \
        filter(BankTable.branch_id == employee.branch_id).first()

    if not branchNew:
        raise HTTPException(status_code=404, detail="Branch not found")

    branchNew.num_employees = branchNew.num_employees + 1

    db_session.commit()

    return {"Great Success": True}