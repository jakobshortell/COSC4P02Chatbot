import React from "react";

// Styling
import InputCSS from "../css/Input.module.css";

// Assets
import clearIcon from "../assets/clear.png";
import sendIcon from "../assets/send.png";

const Input = ({ userInput, sendMessage }) => {
	const clearMessage = () => {
		userInput.current.value = "";
	};

	return (
		<div className={InputCSS.inputContainer}>
			<textarea
				id="inputfield"
				className={InputCSS.inputField}
				type="text"
				ref={userInput}
				rows="1"
				placeholder="Type your question here"
			/>
			<button
				className={InputCSS.clearButton}
				type="button"
				onClick={clearMessage}
			>
				<img
					className={InputCSS.clearButtonImage}
					src={clearIcon}
					alt="clearButtonImage"
				></img>
			</button>
			<button
				className={InputCSS.sendButton}
				type="button"
				onClick={sendMessage}
			>
				<img
					className={InputCSS.sendButtonImage}
					src={sendIcon}
					alt="sendButtonImage"
				/>
			</button>
		</div>
	);
};

export default Input;
