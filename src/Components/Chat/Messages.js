import React from 'react'
import { connect } from 'react-redux'
import Message from './Message'

class Messages extends React.Component {

	componentDidMount() {
		const div = document.getElementById('messageList');
		div.scrollTop = div.scrollHeight;
	}

	componentDidUpdate() {
		const div = document.getElementById('messageList');
		div.scrollTop = div.scrollHeight;
	}

	render() {

		return (
			<div id="messageList" className="messages">
				{this.props.messages.map(msg => {
					return <Message to={msg.to} message={msg.message} />
				})}
			</div>
		)
	}
}

const mapStateToProps = (state) => {
    return {
        messages: state.messages
    }
}

export default connect(mapStateToProps)(Messages)