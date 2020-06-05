import { applyMiddleware, createStore } from 'redux';
import { ApiAiClient } from 'api-ai-javascript';

const accessToken = '1c7d7d66782b42d4a31735b40c1efee8';
const client= new ApiAiClient({ accessToken });
const ON_MSG = 'ON_MESSAGE';

export const sendMsg = (text, sender='user') => ({
	type: ON_MSG,
	payload: {text, sender}
});

const msgMiddleware = () => next => action => {
	next(action);
	if (action.type === ON_MSG) {
		const text = action.payload;
		client.textRequest(text)
		.then((response) => {
			console.log(response);
			// console.log(response.result.fulfillment.speech);
			next(sendMsg(response.result.fulfillment.speech, 'hot'));
		}).catch((error) => {
			console.log(error);
		})
	}
}

const initState = [{text: 'hey'}];
const msgReducer=(state=initState, action) => {
	switch(action.type) {
		case ON_MSG:
			return [...state, action.payload]
		default:
			return state
	}
}

export const store=createStore(msgReducer, applyMiddleware(msgMiddleware))