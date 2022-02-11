import React from 'react';

import planet from '../assets/planet.png';
import user from '../assets/user.png';

export function Message({ author, content }) {

	if (author === 'user') {
		return (
			<div className='user-message-bubble'>
				<img src={user} className='message-icon' alt='user-icon' />
				{content}
			</div>
		)
	} else {
		return (
			<div className='bot-message-bubble'>
				<img src={planet} className='message-icon' alt='bot-icon' />
				{content}
			</div>
		)
	}

}
