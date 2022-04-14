import { useRef, useState } from "react";

// Styling
import AppCSS from "../css/App.module.css";



// Components
import Header from "./Header";
import Modal from "./Modal";
import MessageContainer from "./MessageContainer";
import Input from "./Input";

const uuid = require("uuid");

const App = () => {
	const inputRef = useRef();
	const modalRef = useRef();
	const languageRef = useRef();
	const [messages, setMessages] = useState([
		{
			author: "bot",
			content: "I'm a Bot, ask me a question!",
			timestamp: getTime(),
			id: uuid.v4(),
		},
	]);

	function getTime() {
		let date = new Date();
		let hours = date.getHours();
		let minutes = date.getMinutes();

		// Correct minutes
		if (minutes < 10) {
			minutes = "0" + minutes.toString();
		}

		// Correct hours
		if (hours <= 12) {
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
			return [
				...previousMessages,
				{
					author: message.author,
					content: message.content,
					timestamp: getTime(),
					id: uuid.v4(),
				},
			];
		});
		scroll();
	}

	async function addUserMessage() {
		const message = inputRef.current.value;

		if (message !== "") {
			addMessage({
				author: "user",
				content: message,
			});

			inputRef.current.value = null;
			document.getElementById("activedot").style.display = "flex";
			setTimeout(() => {addBotMessage(message);}, 3000);
		}
	
	}

	function addBotMessage(userMessage) {
		try {
		var timeout = setTimeout(myTimeout, 30000);
		fetch("/api", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({
				userMessage: userMessage,
				language: languageRef.current.value,
			}),
		})
			.then((response) => {
				// Check response
				if (response.ok) {
					return response.json();
				} else {
					console.log(response.status);
				}
			})
			.then((data) => {
				// Create bot message
				document.getElementById("activedot").style.display = "none";
				if (data !== {}) {
					addMessage({
						author: "bot",
						content: data.content,
					});
					clearTimeout(timeout);
				}
			});
		}
		catch(err) {
			addMessage({
				author: "bot",
				content: "Error, chatbot is not working right now",
			});
		}
	}

	function myTimeout() {
		addMessage({
			author: "bot",
			content: "Chatbot is taking longer then expected.",
		});
	  }

	function scroll() {
		let chatHistory = document.getElementById("scroll");
		chatHistory.scrollTop = chatHistory.scrollHeight;
	}

	return (
		<div className={AppCSS.app}>
			<Header modal={modalRef} language={languageRef} />
			<Modal modal={modalRef} />			
			<MessageContainer messages={messages}/>
			<Input input={inputRef} sendMessage={addUserMessage} />
		</div>
	);
};

export default App;