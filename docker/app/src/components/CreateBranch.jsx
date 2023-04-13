import React, { useState, useEffect } from 'react'

export default function CreateBranch() {

    const [id, setID] = useState("")
    const [amount, setAmount] = useState("")
    const [num_employees, setNumEmployees] = useState("")

    function createBranch() {

        fetch("http://localhost:8000/branches/" + id + "/" + amount + "/" + num_employees,
            {
                method: 'POST',
                header: {Accept: "application/json", "Content=Type": "application/json"},
            }
        ).then((m) => console.log(m))
    }

  return (
    <div>
        <p>Branch ID:</p>
        <input type = "number" name = "id" value = {id} onChange ={a=> setID(a.target.value)} />
        <br></br>

        <p>Amount:</p>
        <input type = "number" name = "amount" value = {amount} onChange ={a=> setAmount(a.target.value)} />
        <br></br>

        <p>Number of Employees:</p>
        <input type = "number" name = "num_employees" value = {num_employees} onChange ={a=> setNumEmployees(a.target.value)} />
        <br></br>

        <button onClick={createBranch}>Add</button>

    </div>
  )
}