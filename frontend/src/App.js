import React, { Component } from 'react';

class App extends Component {
  state = {
    languages: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/languages/');
      const languages = await res.json();
      this.setState({
        languages
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.languages.map(item => (
          <div key={item.id}>
            <h1>{item.name}</h1>
            <h4>{item.paradigm}</h4>
            <span>{item.created_by}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
