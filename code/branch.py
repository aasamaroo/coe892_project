from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from db import db_session
from model import BankTable, EmployeeTable

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#GET request to get the data for all of the branches
@app.get("/branches")
async def getBranches():
    return db_session.query(BankTable).all()

#Todo: add more requests for branches such as a GET request to get a particular branch
#      perhaps a POST request to create a new branch, a DELETE request to remove a branch
#      and a PUT request to update a branch (maybe something like update the cash available)

#GET request to get a particular branch specified by Branch ID
@app.get("/branches/{branch_id}")
async def getBranchByID(branch_id: int):
    branch = db_session.query(BankTable). \
        filter(BankTable.branch_id == branch_id).first()

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    return branch

#POST request to create a branch with a new Branch ID
@app.post("/branches")
async def createBranch(id: int):
    bank = BankTable()
    bank.branch_id = id
    bank.amount = 1000
    bank.num_employees = 0
    calculateMinCash(id)
    db_session.add(bank)
    db_session.commit()
    return {"Great Success!": True}


#DELETE request to delete a branch
@app.delete("/branches/{branch_id}")
async def deleteBranch(branch_id: int):
    branch = db_session.query(BankTable). \
        filter(BankTable.id == branch_id).first()

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    #Lay off everyone working at the bank to be deleted
    db_session.query(EmployeeTable).filter(EmployeeTable.branch_id == branch_id).delete()

    #Delete the branch itself
    db_session.delete(branch)
    db_session.commit()
    return {"Great Success!": True}

#PUT request to update the amount of cash avaiable at a branch
@app.put("/branches/{branch_id}")
async def updateBranch(branch_id: int, amount: int):
    branch = db_session.query(BankTable). \
        filter(BankTable.branch_id == branch_id).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    calculateMinCash(branch.branch_id)

    if amount < branch.min_cash:
        raise HTTPException(status_code=400, detail="Amount must meet min cash requirement")
    else:
        branch.amount = amount

    db_session.commit()

    return {"Great Success": True}

def calculateMinCash(id: int):
    branch = db_session.query(BankTable). \
        filter(BankTable.branch_id == id).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    branch.min_cash = branch.num_employees * 1000
    db_session.commit()
    return {"Min Cash Calculated": True}
