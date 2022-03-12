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
	const userInput = useRef();
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
			return [
				...previousMessages,
				{
					author: message.author,
					content: message.content,
					timestamp: getTime(),
					id: message.id,
				},
			];
		});
		scroll();
	}

	async function addUserMessage() {
		const message = userInput.current.value;

		if (message !== "") {
			addMessage({
				author: "user",
				content: message,
				id: uuid.v4(),
			});

			userInput.current.value = null;
			addBotMessage(message);
		}
	}

	function addBotMessage(userMessage) {
		fetch("/api", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({
				userMessage: userMessage,
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
				if (data !== {}) {
					addMessage({
						author: "bot",
						content: data.content,
						id: uuid.v4(),
					});
				}
			});
	}

	function scroll() {
		let chatHistory = document.getElementById("scroll");
		chatHistory.scrollTop = chatHistory.scrollHeight;
	}

	return (
		<div className={AppCSS.app}>
			<Header />
			<Modal />
			<MessageContainer messages={messages} />
			<Input userInput={userInput} sendMessage={addUserMessage} />
		</div>
	);
};

export default App;
