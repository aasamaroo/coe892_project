import React, { useState, useEffect, Component} from 'react'

export default function DeleteEmployee() {

    const [employeeID, setEmployeeID] = useState("")

    function deleteEmployee() {
        fetch("http://localhost:8001/employees/" + employeeID,
            {
                method: 'DELETE',
                header: {Accept: "application/json", "Content=Type": "application/json"},
            }

        ).then((m) => console.log(m))
    }


  return (
    <div>
        <p>Employee ID:</p>
        <input type="number" name = "employeeID" value = {employeeID} onChange = {x => setEmployeeID(x.target.value)}/>
        <br></br>
        <button onClick = {deleteEmployee}>Delete Employee</button>
    </div>
  )
}