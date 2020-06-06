import React from 'react'
import { bindActionCreators } from "redux";
import { connect } from "react-redux";
import Messages from './Messages'
import ChatInput from './ChatInput'
import '../../styles/chat.css'
import { getMessages } from '../../config/apiConfig'
import { addMsg } from '../../Actions'

class Chat extends React.Component {

	componentDidMount() {
		this.intervalID = setInterval(() => this.newMsgs(), 20000);
	}

  componentWillUnmount() {
	    clearInterval(this.intervalId);
	}

  async newMsgs() {
  	let msgs = await getMessages({id: 1});
  	this.props.addMsg(msgs.message);
  }

	render() {
		return (
			<div className="page">
				<h1 className="page-title">CHAT WITH ME!!!</h1>
				<div className="chat-container">
					<Messages />
					<ChatInput />
				</div>
			</div>
		);
	}
}

function mapStateToProps(state) {
    return {
    }
}

function matchDispatchToProps(dispatch) {
    return bindActionCreators({
    	addMsg: addMsg
    }, dispatch)
}

export default connect(mapStateToProps, matchDispatchToProps)(Chat);