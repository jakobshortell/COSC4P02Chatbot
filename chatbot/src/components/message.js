import React from 'react';

import MessageCSS from '../css/Message.module.css';

import planet from '../assets/planet.png';
import user from '../assets/user.png';

export function Message({ author, content }) {

	if (author === 'user') {
		return (
			<li className={ MessageCSS.userMessageBubble }>
				<img className={ MessageCSS.messageIcon } src={ user } alt='user-icon' />
				<span className='messageContent'>{ content }</span>
			</li>
		)
	} else {
		return (
			<li className={ MessageCSS.botMessageBubble }>
				<img className={ MessageCSS.messageIcon } src={ planet } alt='bot-icon' />
				<span className='messageContent'>{ content }</span>
			</li>
		)
	}

}
