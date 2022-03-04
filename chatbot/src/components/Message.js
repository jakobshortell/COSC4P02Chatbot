import React from 'react';
import Linkify from 'react-linkify';
import MessageCSS from '../css/Message.module.css';

import botIcon from '../assets/brock.png';
import userIcon from '../assets/user.png';

export function Message({ author, content, time }) {

	if (author === 'user') {
		return (
			<li className={` ${MessageCSS.message} ${MessageCSS.userMessage} `}>
				<img className={ MessageCSS.messageIcon } src={ userIcon } alt='user-icon' />
				<div className={` ${MessageCSS.messageBubble} ${MessageCSS.userMessageBubble} `}>
					<div>
						<span className={` ${MessageCSS.userName} ${MessageCSS.name} `}>You</span>
						<span className={ MessageCSS.time }>{ time }</span>
					</div>
					<span>{ content }</span>
				</div>
			</li>
		)
	} else {
		return (
			<li className={` ${MessageCSS.message} ${MessageCSS.botMessage} `}>
				<img className={ MessageCSS.messageIcon } src={ botIcon } alt='bot-icon' />
				<div className={` ${MessageCSS.messageBubble} ${MessageCSS.botMessageBubble} `}>
					<div>
						<span className={` ${MessageCSS.botName} ${MessageCSS.name} `}>Brock University</span>
						<span className={ MessageCSS.time }>{ time }</span>
					</div>
					<span><Linkify properties={{target: '_blank'}}>{ content }</Linkify></span>
				</div>
			</li>
		)
	}

}
