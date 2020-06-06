import React, { Component } from 'react';
import { connect } from 'react-redux';
import Chat from './Components/Chat';

class App extends Component {

  render() {
    return (
      <div>
        <Chat />
      </div>
    );
  }
}


export default App;
