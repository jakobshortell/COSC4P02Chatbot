import React from "react";

// Styling
import HeaderCSS from "../css/Header.module.css";

// Assets
import brockLogo from "../assets/brocklogo.jpeg";
import settingsIcon from "../assets/setting.png";
import helpIcon from "../assets/help.png";

const Header = ({ modal }) => {
	const displayModal = () => {
		modal.current.style.display = "flex";
	};

	return (
		<header className={HeaderCSS.chatbotHeader}>
			<a href="https://brocku.ca/" target="_blank" rel="noreferrer">
				<img className={HeaderCSS.logo} src={brockLogo} alt="logo" />
			</a>
			<div className={HeaderCSS.list}>
				<img
					className={`${HeaderCSS.icon} ${HeaderCSS.help}`}
					src={helpIcon}
					alt="help"
					onClick={displayModal}
				/>
				<img
					className={`${HeaderCSS.icon} ${HeaderCSS.settings}`}
					src={settingsIcon}
					alt="settings"
				/>
			</div>
		</header>
	);
};

export default Header;