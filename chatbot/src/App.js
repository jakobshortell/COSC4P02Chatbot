import React, { useRef, useState } from 'react';
import { MessageContainer } from './components/messageContainer';
import logo from './assets/logo.png';
import './App.css';

const uuid = require('uuid');


function App() {

	const [messages, setMessages] = useState([]);
	const inputContent = useRef();

	function addUserMessage() {

		const message = inputContent.current.value

		if (message !== '') {
			setMessages((previousMessages) => {
				return [...previousMessages, {
					'author': 'User',
					'content': message,
					'id': uuid.v4()
				}];
			});
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
				data = JSON.stringify(data).replace("{", "");
				data = data.replace(/"/g,"");
				data = data.replace("}", "");
				setMessages((previousMessages) => {
					return [...previousMessages, {
						'author': 'Bot',
						'content': data,
						'id': uuid.v4()
					}];
				});
			}
		})

	}
	function scroll() {
		var chatHistory = document.getElementById("scroll");
		chatHistory.scrollTop = chatHistory.scrollHeight;
	
		
	}
	function clickUser() {
		addUserMessage()
		setTimeout(scroll, 200)
	}
	function clickBot() {
		addBotMessage()
		setTimeout(scroll, 200)
	
	}
	

	return (
		
		<><div className="App">
			<header className="App-header">
				<img src={logo} className="Applogo" alt="logo" />
				<div class="box" id="scroll">-----I'm a Bot, ask me a question-----
					<MessageContainer messages={messages} />
					<div class="box3"> </div>
					</div>
					<div class="chat">
					<input class="input" ref={inputContent} type='text' />
					<button type="button" class="button" onClick={clickUser} >Send</button>
					</div>
				<button type="button" class="button" onClick={clickBot}>TESTING: ADD BOT RESPONSE</button>
			</header>
		</div></>
		
	);
}




export default App;
