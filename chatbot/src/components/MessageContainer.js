import React from "react";

// Styling
import MessageContainerCSS from "../css/MessageContainer.module.css";

// Components
import Message from "./Message";
import Dot from "./ActiveButton";

const MessageContainer = ({ messages }) => {
	return (
		<div className={MessageContainerCSS.messageContainer}>
			<Dot />
			<ul className={MessageContainerCSS.scrollable} id="scroll">
				{messages.map((message) => {
					return (
						<Message
							key={message.id}
							author={message.author}
							content={message.content}
							time={message.timestamp}
						/>
					);
				})}
			</ul>
		</div>
	);
};

export default MessageContainer;
