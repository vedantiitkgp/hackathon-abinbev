export const addMsg = (messages) => {
    return {
        type: 'ADD_MSG',
        payload:messages
    }
};

export const sendNewMsg = (message) => {
    return {
        type: 'ADD_NEW_MSG',
        payload: message
    }
};