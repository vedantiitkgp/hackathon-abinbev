import React, { Component } from 'react';
import { connect } from 'react-redux';
import { sendMsg } from './chat';

class App extends Component {
  // state = {
  //   input: '',
  // }

  // handleChange = (e) => {
  //   this.setState({
  //     [e.target.name]: e.target.value,
  //   });
  // }

  // handleSubmit = (e) => {
  //   e.preventDefault();

  //   this.setState({input: ''});
  // }

  render() {
    const { feed, sendMsg } = this.props;
    return (
      <div>
        <h1>Hello Chat!</h1>
        <ul>
          {feed.map(entry => <li>{entry.text}</li>)}
        </ul>
        <input type="text" onKeyDown = {(e) => (e.keyCode === 13) ? sendMsg(e.target.value) : null} />
      {/*
        <form onSubmit={this.handleSubmit}>
          <input type="text" name="input" value={this.state.input} onChange={this.handleChange}></input>
          <button>Submit</button>
        </form>
      */}
      </div>
    );
  }
}

const mapStateToProps = state => ({
  feed: state
});

export default connect(mapStateToProps, {sendMsg})(App);
