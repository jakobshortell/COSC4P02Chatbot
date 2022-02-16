import React from 'react';

import MessageContainerCSS from '../css/MessageContainer.module.css';

import { Message } from './Message';

export function MessageContainer({ messages }) {

	return (
		<div className={ MessageContainerCSS.messageContainer }>
			<ul className={ MessageContainerCSS.scrollable } id='scroll'>
				{
					messages.map((message) => {
						return <Message key={ message.id } author={ message.author } content={ message.content } time={ message.timestamp } />
					})
				}
			</ul>
		</div>
	)

}
