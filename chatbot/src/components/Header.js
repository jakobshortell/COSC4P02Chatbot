import React from 'react';

// Styling
import HeaderCSS from '../css/Header.module.css';

// Assets
import brockLogo from '../assets/brocklogo.jpeg';
import settingsIcon from '../assets/setting.png';

const Header = () => {

	return (
		<header className={ HeaderCSS.chatbotHeader }>
			<a href='https://brocku.ca/' target='_blank' rel='noreferrer'>
				<img className={ HeaderCSS.logo } src={ brockLogo } alt='logo' />
			</a>
			<img className={ HeaderCSS.settings } src={ settingsIcon } alt='settings' />
		</header>
	)

}

export default Header;