import logo from "./logo.svg";
import "./App.css";
import React from 'react'
import {BrowserRouter} from 'react-router-dom'



import Main from './components/Main/Main'

function App() {
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>DockerHub demo - by MNievas</p>
      </header>
      <BrowserRouter>
      <div className="App-body">
        <Main />
      </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
