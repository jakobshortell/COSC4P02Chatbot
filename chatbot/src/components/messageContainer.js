import React from 'react';

import { Message } from './Message';

export function MessageContainer({ messages }) {

	return (
		<div className='message-container' id='scroll'>
			<ul>
				{
					messages.map((message) => {
						return <Message key={ message.id } author={ message.author } content={ message.content } />
					})
				}
			</ul>
		</div>
	)

}
