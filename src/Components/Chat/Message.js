import React from 'react'

class Message extends React.Component {
	render() {
		const place = this.props.to ? 'right' : 'left';
		return (
			<div className={`message ${place}`}>
				<div className="msg-body">
					{this.props.message}
				</div>
			</div>
		);
	}
}

export default Message