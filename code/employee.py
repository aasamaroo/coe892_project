from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from db import db_session
from model import EmployeeTable

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
@app.get("/patients")
def getEmployees():
    return db_session.query(EmployeeTable).all()

#Todo: create requests to Create, Read, Update, and Delete (CRUD) employees