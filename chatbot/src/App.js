import React, { useRef, useState } from 'react';
import { MessageContainer } from './components/messageContainer';
import logo from './logo.png';
import './App.css';

const uuid = require('uuid');

function App() {

	const [messages, setMessages] = useState([]);
	const inputContent = useRef();

	async function addUserMessage() {

		const message = inputContent.current.value

		if (message !== '') {
			setMessages((previousMessages) => {
				return [...previousMessages, {
					'author': 'User',
					'content': message,
					'id': uuid.v4()
				}];
			});
		const response = await fetch('/api', {
		method: "POST",
		headers: {'Content-Type' : 'application/json'},
		body: JSON.stringify(message)
		}).then((response) => {
			if (response.ok) {
				return response.json();
			} else {
				console.log(response.status)
			}
		}).then((data) => {
			if (data !== {}) {
				setMessages((previousMessages) => {
					return [...previousMessages, {
						'author': 'Bot',
						'content': data.content,
						'id': uuid.v4()
					}];
				});
			}
		})
			inputContent.current.value = null;
		}

	}

	function addBotMessage() {

		fetch('/api').then((response) => {
			if (response.ok) {
				return response.json();
			} else {
				console.log(response.status)
			}
		}).then((data) => {
			if (data !== {}) {
				setMessages((previousMessages) => {
					return [...previousMessages, {
						'author': 'Bot',
						'content': data.content,
						'id': uuid.v4()
					}];
				});
			}
		})

	}

	return (
		
		<><div className="App">
			<header className="App-header">
				<img src={logo} className="Applogo" alt="logo" />
				<div class="box">-----I'm a Bot, ask me a question-----
					<MessageContainer messages={messages} />
					</div>
					<div class="chat">
					<input class="input" ref={inputContent} type='text' />
					<button type="button" class="button" onClick={addUserMessage}>Send</button>
					</div>
				<button type="button" class="button" onClick={addBotMessage}>TESTING: ADD BOT RESPONSE</button>
			</header>
		</div></>
		
	);

}

export default App;
