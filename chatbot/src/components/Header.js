import React from 'react';

import HeaderCSS from '../css/Header.module.css';

import brockLogo from '../assets/brocklogo.jpeg';
import settingsIcon from '../assets/setting.png';

export function Header() {

	return (
		<header className={ HeaderCSS.chatbotHeader }>
			<a href='https://brocku.ca/' target='_blank' rel='noreferrer'>
				<img className={ HeaderCSS.logo } src={ brockLogo } alt='logo' />
			</a>
			<img className={ HeaderCSS.settings } src={ settingsIcon } alt='settings' />
		</header>
	)

}