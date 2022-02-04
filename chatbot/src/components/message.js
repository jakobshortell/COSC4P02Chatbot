import React from 'react';

import planet from '../assets/planet.png';
import user from '../assets/user.png';

export function Message({ author, content }) {

	if (author === 'user') {
		return (
			<p className='user-message-bubble'>
				<img src={user} className='message-icon' alt='user-icon' />
				{content}
			</p>
		)
	} else {
		return (
			<p className='bot-message-bubble'>
				<img src={planet} className='message-icon' alt='bot-icon' />
				{content}
			</p>
		)
	}

}
