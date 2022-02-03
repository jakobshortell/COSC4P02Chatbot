import React from "react";
import { Message1 } from "./message1";

export function MessageContainer1({ messages1 }) {

	return (
		messages1.map((message1) => {
			return <Message1 key={message1.id} author={message1.author} content={message1.content}/>
		})
	);

}