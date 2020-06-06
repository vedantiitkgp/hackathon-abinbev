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

	handleSubmit = async (e) => {
		e.preventDefault()
		if (!this.state.msg)
			return;
		const msg = await sendMessages({id: 1, message: this.state.msg, to: 1});
		console.log(msg);
		this.props.sendNewMsg({message: this.state.msg, to: 1});
		this.props.sendNewMsg({message: msg.data, to: 0});
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