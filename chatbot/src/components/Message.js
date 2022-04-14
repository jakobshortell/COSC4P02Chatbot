import React from 'react';
import Linkify from 'react-linkify';
import MessageCSS from '../css/Message.module.css';
import { SecureLink } from "react-secure-link";
import botIcon from '../assets/loading.gif';
import userIcon from '../assets/user.png';
import linkIcon from '../assets/linkRed.png';

export function Message({ author, content, time }) {

	if (author === 'user') {
		return (
			<li className={` ${MessageCSS.message} ${MessageCSS.userMessage} `}>

				<div className={` ${MessageCSS.messageBubble} ${MessageCSS.userMessageBubble} `}>
					<div>
						<span className={` ${MessageCSS.userName} ${MessageCSS.name} `}>You</span>
						<span className={ MessageCSS.time }>{ time }</span>
					</div>
					<span>{ content }</span>
				</div>
				<img className={ MessageCSS.messageIconUser } src={ userIcon } alt='user-icon' />
			</li>
		)
	} else {
		return (
			<li className={` ${MessageCSS.message} ${MessageCSS.botMessage} `}>
			
				<div className={` ${MessageCSS.messageBubble} ${MessageCSS.botMessageBubble} `}>
					<div>
						<span className={` ${MessageCSS.botName} ${MessageCSS.name} `}>Brock University</span>
						<span className={ MessageCSS.time }>{ time }</span>
					</div>
						<span><Linkify
       						componentDecorator={(
          					decoratedHref: string, key: Key) => (<SecureLink href={decoratedHref} key={key}>
								  Link<img className={MessageCSS.link} src={linkIcon} alt='Link'/></SecureLink>)}>
								  {content}
								</Linkify></span>
					</div>
			</li>
		)
	}
}
export default Message;