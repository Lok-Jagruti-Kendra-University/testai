import './App.css';
import {useState } from "react";

function App({id,pname}) {
  
  const [inputs, setInputs] = useState({});
  const [textarea, setTextarea] = useState(
    "The content of a textarea goes in the value attribute"
  );

  const handleChangeTA = (event) => {
    setTextarea(event.target.value)
  }

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    //console.log(name+" "+value);

    setInputs(abc => ({...abc, [name]: value}))
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(inputs);
    console.log(textarea)
  }
var VS "gELOFD";
var abc = (<label>Enter your name {id} {pname.name} {pname.lname}
<input 
    type="text" 
    name="username" 
    value={inputs.username || ""} 
    onChange={handleChange}
      />
</label>);
  return (
    <form onSubmit={handleSubmit}>
    {abc}
    <label>Enter your age
    <input 
        type="number" 
        name="age" 
        value={inputs.age || ""} 
        onChange={handleChange}
      />
    </label> 
    <textarea value={textarea} onChange={handleChangeTA} />
    <input type="SUBMIT" /> 
    </form>
  );

}

export default App;
