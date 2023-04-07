from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from db import db_session
from model import BankTable

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