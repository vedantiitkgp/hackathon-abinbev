import React from 'react'
import { bindActionCreators } from "redux";
import { connect } from 'react-redux'
import { sendMessages } from '../../config/apiConfig'
import { sendNewMsg } from '../../Actions'

class ChatInput extends React.Component {
	state = {
		msg: ''
	};

	handleChange = (e) => {
		this.setState({ msg: e.target.value });
	}

	process_reply = (reply) => {
		if (reply.msg) {
			this.props.sendNewMsg({message: reply.msg, to: 0, pop: 0});
		} else {
			this.props.sendNewMsg({message: reply.data, to: 0, pop: 1});
		}
	}

	handleSubmit = async (e) => {
		e.preventDefault()
		if (!this.state.msg)
			return;
		const reply = await sendMessages({id: 1, message: this.state.msg, to: 1});
		console.log(reply);
		this.props.sendNewMsg({message: this.state.msg, to: 1, pop: 0});
		this.process_reply(reply)
		// this.props.sendNewMsg({message: reply.data, to: 0, pop: 1});
		this.setState({ msg: ''});
	}

	render() {
		return (
			<form onSubmit={this.handleSubmit} className="chat-input">
				<input type="text"
					onChange={this.handleChange}
					value={this.state.msg}
					placeholder="Write a message..."
					required />
				<input type="submit"
					value="Send" />
			</form>
		)
	}
}

const mapStateToProps = (state) => {
    return {
    }
}

function matchDispatchToProps(dispatch) {
    return bindActionCreators({
    	sendNewMsg: sendNewMsg
    }, dispatch)
}

export default connect(mapStateToProps,matchDispatchToProps)(ChatInput)