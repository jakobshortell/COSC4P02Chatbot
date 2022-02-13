import React from 'react';

import MessageCSS from '../css/Message.module.css';

import botIcon from '../assets/brock.png';
import userIcon from '../assets/user.png';

export function Message({ author, content, time }) {

	if (author === 'user') {
		return (
			<li className={ MessageCSS.userMessage }>
				<img className={ MessageCSS.userMessageIcon } src={ userIcon } alt='user-icon' />
				<div className={ MessageCSS.messageBubble }>
					<div>
						<span className={ MessageCSS.userName }>You</span>
						<span className={ MessageCSS.time }>{ time }</span>
					</div>
					<span className={ MessageCSS.messageContent }>{ content }</span>
				</div>
			</li>
		)
	} else {
		return (
			<li className={ MessageCSS.botMessage }>
				<img className={ MessageCSS.botMessageIcon } src={ botIcon } alt='bot-icon' />
				<div className={ MessageCSS.messageBubble }>
					<div>
						<span className={ MessageCSS.botName }>Brock University</span>
						<span className={ MessageCSS.time }>{ time }</span>
					</div>
					<span className={ MessageCSS.messageContent }>{ content }</span>
				</div>
			</li>
		)
	}

}
