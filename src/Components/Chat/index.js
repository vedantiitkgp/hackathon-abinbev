import React from 'react'
import Messages from './Messages'
import ChatInput from './ChatInput'
import '../../styles/chat.css'

class Chat extends React.Component {
	render() {
		return (
			<div className="page">
				<div className="chat-container">
					<h1 className="page-title">CHAT WITH ME!!!</h1>
					<Messages />
					<ChatInput />
				</div>
			</div>
		);
	}
}
export default Chat;