import React, { useState, useEffect, Component} from 'react'

export default function DeleteBranch() {

    const [branchID, setBranchID] = useState("")

    function deleteBranch() {
        fetch("http://localhost:8000/branches/" + branchID,
            {
                method: 'DELETE',
                header: {Accept: "application/json", "Content=Type": "application/json"},
            }

        ).then((m) => console.log(m))
    }


  return (
    <div>
        <p>Branch ID:</p>
        <input type="number" name = "branchID" value = {branchID} onChange = {x => setBranchID(x.target.value)}/>
        <br></br>
        <button onClick = {deleteBranch}>Delete Branch</button>
    </div>
  )
}