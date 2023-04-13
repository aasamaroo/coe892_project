import React, { useState, useEffect, Component} from 'react'
import {render} from "react-dom";

export default function GetEmployees() {

    const [employees, setEmployees] = useState("")
    const [loading, setLoading] = useState(false)

    function getEmployees() {
        setLoading(true)
        fetch("http://localhost:8001/employees/",
            {
                method: 'GET',
                header: {Accept: "application/json", "Content=Type": "application/json"},
            }

        ).then((m) => m.json()).then(setEmployees)
            .then(setLoading(false))
    }  

    useEffect(() => {
        setLoading(true)
        getEmployees()
    }, [])

    if(loading){
        return <h1>Loading...</h1>
    }
    if(Array.isArray(employees)){
        return (
            <div>
                <table>
                    <thead>
                    <tr>
                        <th>Employee ID</th>
                        <th>Branch ID</th>
                    </tr>
                    </thead>
                    <tbody>
                        {employees.map((employee, i) =>
                                <tr key = {i}>
                                    <td>{employee.employee_id}</td>
                                    <td>{employee.branch_id}</td>
                                </tr>
                        )}
                    </tbody>
                </table>

                <button onClick = {getEmployees}>Update</button>
            </div>
        )
    }





}