import React from 'react';

import planet from '../assets/planet.png';
import user from '../assets/user.png';

export function Message({ author, content }) {

	if (author === 'user') {
		return (
			<p className='user-message-bubble sb1'>
				<img src={user} className='user-icon' alt='User' />
				{content}
			</p>
		);
	} else {
		return (
			<p className='bot-message-bubble sb2'>
				<img src={planet} className='user-icon' alt='planet' />
				{content}
			</p>
		);
	};

};