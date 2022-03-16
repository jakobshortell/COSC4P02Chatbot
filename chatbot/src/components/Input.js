import React from "react";

// Styling
import InputCSS from "../css/Input.module.css";

// Assets
import clearIcon from "../assets/clear.png";
import sendIcon from "../assets/send.png";

const Input = ({ input, sendMessage }) => {
	const clearMessage = () => {
		input.current.value = "";
	};

	return (
		<div className={InputCSS.inputContainer}>
			<textarea
				id="inputfield"
				className={InputCSS.inputField}
				type="text"
				ref={input}
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