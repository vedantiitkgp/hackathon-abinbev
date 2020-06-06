import React from 'react'
import { connect } from 'react-redux'
import { Modal, Table } from 'react-bootstrap'

class Messages extends React.Component {

	state = {
		showTable: false
	}

	componentDidMount() {
		const div = document.getElementById('messageList');
		div.scrollTop = div.scrollHeight;
	}

	componentDidUpdate() {
		const div = document.getElementById('messageList');
		div.scrollTop = div.scrollHeight;
	}

	toggleTable = () => {
		this.setState({showTable: !this.state.showTable});
	}

	render() {

		return (
			<div id="messageList" className="messages">
				{this.props.messages.map(msg => {
					const place = msg.to ? 'right' : 'left';
					const headers = Object.keys(msg.message);
					const n = msg.message[headers[0]].length;
					console.log(headers, headers[0], n);
					return (msg.pop) ?
						<div className={`message ${place}`}>
							<div className="msg-body modal-link" onClick={this.toggleTable}>
								<u>Click Here</u>
							</div>
							<Modal size="lg" show={this.state.showTable} onHide={this.toggleTable}>
				        <Modal.Body>
				        	<Table bordered hover>
				        		<thead>
					        		{
					        			headers.map((name) => {
					        				return (
					        					<th>{name}</th>
				        					);
					        			})
					        		}
				        		</thead>
				        		<tbody>
				        			{
				        				[...Array(n)].map((e, i) => {
				        					return (
				        						<tr>
				        							{
				        								headers.map((name) => {
				        									return (
				        										<td>
				        											{msg.message[name][i]}
				        										</td>
			        										);
				        								})
				        							}
				        						</tr>
			        						);
				        				})
				        			}
				        		</tbody>
				        	</Table>
				        </Modal.Body>
							</Modal>
						</div>
					: <div className={`message ${place}`}>
							<div className="msg-body">
								{msg.message}
							</div>
						</div>
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