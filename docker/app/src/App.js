import logo from './logo.svg';
import './App.css';

import GetBranches from './components/GetBranches';
import CreateBranch from './components/CreateBranch';
import DeleteBranch from './components/DeleteBranch';

import GetEmployees from './components/GetEmployees';
import CreateEmployee from './components/CreateEmployee';
import DeleteEmployee from './components/DeleteEmployee';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div class="branch">
          <h2>List of all Branches</h2>
          <GetBranches />
          <hr></hr>

          <h2>Create Branch</h2>
          <CreateBranch />
          <hr></hr>

          <h2>Delete Branch</h2>
          <DeleteBranch />
          <hr></hr>
        </div>

        <div class="employees">
          <h2>List of all Employees</h2>
          <GetEmployees />
          <hr></hr>

          <h2>Create an Employee</h2>
          <CreateEmployee />
          <hr></hr>

          <h2>Delete Branch</h2>
          <DeleteEmployee />
          <hr></hr>

        </div>
      </header>
    </div>
  );
}

export default App;
