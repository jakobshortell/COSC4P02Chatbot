import { useRef, useState } from 'react';

import AppCSS from '../css/App.module.css';

import ModalCSS from '../css/Modal.module.css';
import botIcon from '../assets/brock.png';

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

   async function ModalClear(){
	  var ModalContainer = document.getElementById("modalContainer");
	  ModalContainer.style = "display:none";
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
			<div id="modalContainer" className={ModalCSS.ModalContainer}>
			 <div className ={ModalCSS.ModalDiv}>
				 <img src ={ botIcon } alt='logo'></img>
             <h1>Welcome to the Brock University Chatbot</h1>
			 <h2>What can this bot do?</h2>
			 <ul>
			 <li>Get information on Clubs &amp; Events</li>
			 <li>Get information on specific BU courses &amp; programs</li>
			 <li>Ask the chatbot about important dates</li>
			 <li>Have fun little conversations!</li>
			 </ul>
			 <p id="legaleze">*All information is scraped through the Brock University Website</p>
              <input type="button" value="I Understand"  onClick={ ModalClear }/>
              </div>
			  </div>
			<MessageContainer messages={ messages } />
			<Input userInput={ userInput } onClick={ addUserMessage } />
		</div>
	)

}

export default App;
