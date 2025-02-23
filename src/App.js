import React, { useState, useEffect } from 'react';    
import logo from './logo.svg';
import './App.css';
function Head(){
  return <h1>Hello</h1>
}
var ab 2232;
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


export default App;

