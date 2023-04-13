import React, { useState, useEffect, Component} from 'react'
import {render} from "react-dom";

export default function GetBranches() {

    const [branches, setBranches] = useState("")
    const [loading, setLoading] = useState(false)

    function getBranches() {
        setLoading(true)
        fetch("http://localhost:8000/branches",
            {
                method: 'GET',
                header: {Accept: "application/json", "Content=Type": "application/json"},
            }

        ).then((m) => m.json()).then(setBranches)
            .then(setLoading(false))
    }  

    useEffect(() => {
        setLoading(true)
        getBranches()
    }, [])

    if(loading){
        return <h1>Loading...</h1>
    }
    if(Array.isArray(branches)){
        return (
            <div>
                <table>
                    <thead>
                    <tr>
                        <th>Branch ID</th>
                        <th>Num Employee</th>
                        <th>Amount</th>
                    </tr>
                    </thead>
                    <tbody>
                        {branches.map((branch, i) =>
                                <tr key = {i}>
                                    <td>{branch.branch_id}</td>
                                    <td>{branch.num_employees}</td>
                                    <td>{branch.amount}</td>
                                </tr>
                        )}
                    </tbody>
                </table>

                <button onClick = {getBranches}>Update</button>
            </div>
        )
    }





}