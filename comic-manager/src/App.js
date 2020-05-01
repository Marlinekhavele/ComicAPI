import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";

import axios from "axios";

import ComicList from "./components/ComicList";

class App extends Component {
  // default state object
  state = {
    comics: []
  };

  componentDidMount() {
    axios
      .get("")
      .then(response => {
        // create an array of contacts only with relevant data
        const newComics = response.data.map(c => {
          return {
            id: c.id,
            title: c.title

          };
        });

        // create a new "state" object without mutating
        // the original state object.
        const newState = Object.assign({}, this.state, {
          comics: newComics
        });

        // store the new state object in the component's state
        this.setState(newState);
      })
      .catch(error => console.log(error));
  }

  render() {
    return (
      <div className="App">
        {/* <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">React Comic Manager</h1>
        </header> */}

        <ComicList comics={this.state.comics} />
      </div>
    );
  }
}

export default App;
