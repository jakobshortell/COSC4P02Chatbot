import { useRef, useState } from 'react';

import AppCSS from '../css/App.module.css';

import { MessageContainer } from './MessageContainer';
import { Header } from './Header';
import { Input } from './Input';

const uuid = require('uuid');


function App() {

	const userInput = useRef();
	const [messages, setMessages] = useState([
		{
			'author': 'bot',
			'content': 'I\'m a Bot, ask me a question!',
			'timestamp': getTime(),
			'id': uuid.v4()
		}
	])

	function getTime() {
		// Gets the current time as a string

		var date = new Date();
		var hours = date.getHours();
		var minutes = date.getMinutes();

		// Correct minutes
		if (minutes < 10) {
			minutes = '0' + minutes.toString();
		}

		// Correct hours
		if (hours < 12) {
			if (hours === 0) {
				hours = 12;
			}
			return `${hours}:${minutes} am`;
		} else {
			hours = hours - 12;
			return `${hours}:${minutes} pm`;
		}

	}

	function addMessage(message) {
		setMessages((previousMessages) => {
			return [...previousMessages, {
				'author': message.author,
				'content': message.content,
				'timestamp': getTime(),
				'id': message.id
			}]
		})
		scroll()
	}

	async function addUserMessage() {

		const message = userInput.current.value

		if (message !== '') {
			addMessage({
				'author': 'user',
				'content': message,
				'id': uuid.v4()
			})
			
			userInput.current.value = null
			addBotMessage(message)
		}

	}

	function addBotMessage(userMessage) {

		fetch('/api', {
			method: "POST",
			headers: {'Content-Type' : 'application/json'},
			body: JSON.stringify({
				'userMessage': userMessage
			})
		}).then((response) => {

			// Check response
			if (response.ok) {
				return response.json();
			} else {
				console.log(response.status)
			};

		}).then((data) => {

			// Create bot message
			if (data !== {}) {
				addMessage({
					'author': 'bot',
					'content': data.content,
					'id': uuid.v4()
				})
			}

		})

	}

	function scroll() {
		var chatHistory = document.getElementById('scroll')
		chatHistory.scrollTop = chatHistory.scrollHeight
	}

	return (
		<div className={ AppCSS.app }>
			<Header />
			<MessageContainer messages={ messages } />
			<Input userInput={ userInput } onClick={ addUserMessage } />
		</div>
	)

}

export default App;
