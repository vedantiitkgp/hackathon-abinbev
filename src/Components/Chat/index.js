import React from 'react'
import Messages from './Messages'
import ChatInput from './ChatInput'
import { Col } from 'react-bootstrap'
import '../../styles/chat.css'

function Chat() {
	return (
		<Col xs={10} className="content-box">
			<div className="chat-to">
				<span style={{color: 'grey'}}>To: </span>
				<b>BusinessBot</b>
			</div>
			<div className="chat-container">
				<Messages />
				<ChatInput />
			</div>
		</Col>
	);
}
export default Chat;