import React from 'react';

import brockLogo from '../assets/brocklogo.jpeg';
import settingsIcon from '../assets/setting.png';

export function Header() {

	return (
		<header className='chatbot-header'>
			<img className='logo' src={brockLogo} alt='logo' />
			<img className='settings' src={settingsIcon} alt='settings' />
		</header>
	)

}