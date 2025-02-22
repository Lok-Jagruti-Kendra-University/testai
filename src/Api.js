import './App.css';
import React from 'react';
class Api extends React.Component {

  constructor(props) {
    super(props);
    this.state = { items: [], DataisLoaded: false };
  }
  // ComponentDidMount is used to execute the code
  componentDidMount() {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((res) => res.json())
      .then((json) => {this.setState({ items: json, DataisLoaded: true });});
  }

  render() {
    const { DataisLoaded, items } = this.state;
    if (!DataisLoaded) 
      return (
        <div>
          <h1> Pleses wait some time.... </h1>
        </div>
      );

    return (
      <div className="App">
        <h1> Fetch data from an api in react </h1>
        <ol>
          {items.map((item) => (
            <li key={item.id}>
              User_Name: {item.username}, Full_Name: {item.name}, User_Email: {item.address.street}
            </li>
          ))}
        </ol>
      </div>
    );
  }
}

export default Api;
