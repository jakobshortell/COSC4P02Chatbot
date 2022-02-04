import React from 'react';

import { Message } from './message';

export function MessageContainer({ messages }) {

	return (
		<div className='message-container' id='scroll'>
			{
				messages.map((message) => {
					return <Message key={message.id} author={message.author} content={message.content} />
				})
			}
		</div>
	)

}
