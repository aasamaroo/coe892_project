import React, { useState, useEffect } from 'react'

export default function CreateEmployee() {

    const [id, setID] = useState("")
    const [employee_id, setEmployeeID] = useState("")

    function CreateEmployee() {

        fetch("http://localhost:8001/employee/" + id +"/"+ employee_id,
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

        <p>Employee ID:</p>
        <input type = "number" name = "employee_id" value = {employee_id} onChange ={a=> setEmployeeID(a.target.value)} />
        <br></br>

        <button onClick={CreateEmployee}>Add</button>

    </div>
  )
}