import React, { useState, useEffect } from 'react';    
import logo from './logo.svg';
import './App.css';
function Head(){
  return <h1>Hello</h1>
}
function App() {
  const [textBoxValue, setTextBoxValue] = useState('');
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted!');
    console.log('Text Box Value:', textBoxValue);
  }

  return (
        <div>
      <form onSubmit={handleSubmit}>
        {/* Text Box */}
        <label>
          Text Box:
          <input
            type="text"
            value={textBoxValue}
            onChange={(e) => setTextBoxValue(e.target.value)}/>
        </label>
        <button type="submit">Submut</button>
        </form>
        </div>
  );
}

function CounterExample() {  
  const [count, setCount] = useState(0);
  
  useEffect(() => {  
    document.title = `You clicked ${count} times`;  
  });  
  
  return (  
    <div>  
      <p>You clicked {count} times</p>  
      <button onClick={() => setCount(count + 1)}>  Click me  </button>  
    </div>  
  );  
}
const SimpleForm = () => {
  // State variables to store form input values
  const [textBoxValue, setTextBoxValue] = useState('');
  
  // Function to handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted!');
    console.log('Text Box Value:', textBoxValue);
    
  };
  return (
    <div>
      <form onSubmit={handleSubmit}>
        {/* Text Box */}
        <label>
          Text Box:
          <input type="text" value={textBoxValue}
            onChange={(e) => setTextBoxValue(e.target.value)}/>
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  )
}
export {App, Head, CounterExample, SimpleForm};