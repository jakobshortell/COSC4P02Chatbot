import React from 'react';

import logo from '../assets/logo.png';

export function Header() {

	return (
		<header className='chatbot-header'>
			<img src={logo} className='logo' alt='logo' />
		</header>
	)

}