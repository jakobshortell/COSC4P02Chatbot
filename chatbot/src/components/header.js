import React from 'react';

import HeaderCSS from '../css/Header.module.css';

import brockLogo from '../assets/brocklogo.jpeg';
import settingsIcon from '../assets/setting.png';

export function Header() {

	return (
		<header className={ HeaderCSS.chatbotHeader }>
			<img className={ HeaderCSS.logo } src={ brockLogo } alt='logo' />
			<img className={ HeaderCSS.settings } src={ settingsIcon } alt='settings' />
		</header>
	)

}