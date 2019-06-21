import React, { Component } from 'react';
import './App.css';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/Navbar';

class App extends Component {
  state = {
    faangm: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/faangm/');
      const faangm = await res.json();
      this.setState({
        faangm
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div className="container">
      <Navbar />
      <br />
      <h1>Faangm Companies</h1>
      <p>See the list to understand what it means.</p>
      <p>People normally use the <b>FANG</b> (Facebook, Apple, Netflix and Google) definition, but I wanted to include a couple more big tech companies.</p>
        {this.state.faangm.map(item => (
          <div key={item.id}>
            <h3>{item.name}</h3>
            <span className="text-size">{item.created}</span>
            <p>{item.location}</p>
            <br />
          </div>
        ))}
      </div>
    );
  }
}

export default App;
