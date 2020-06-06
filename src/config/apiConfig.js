import axios from 'axios'
import { store } from '../index'

export const HTTP = axios.create({
    baseURL: 'http://127.0.0.1:8000',
});


export const getMessages = (data) => 
  HTTP.post('api/getmessages', JSON.stringify(data), {
    headers: {
        "Content-Type": "application/json"
    }
  }).then(res => {
    return res.data
  }).catch(err => {
    console.log(err);
    return null;
  });

export const sendMessages = (data) => 
  HTTP.post('api/sendMessage', JSON.stringify(data), {
    headers: {
      "Content-Type": "application/json"
    }
  }).then(res => {
    return res.data
  }).catch(err => {
    console.log(err);
    return null;
  });