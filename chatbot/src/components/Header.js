import React, { useRef } from "react";

// Styling
import HeaderCSS from "../css/Header.module.css";

// Assets
import brockLogo from "../assets/brocklogo.jpeg";
import settingsIcon from "../assets/setting.png";
import helpIcon from "../assets/help.png";

const Header = ({ modal }) => {
	const settingsMenu = useRef();

	const displayModal = () => {
		modal.current.style.display = "flex";
	};

	const toggleSettings = () => {
		let menu = settingsMenu.current;
		if (menu.style.display === "none") {
			menu.style.display = "block";
		} else {
			menu.style.display = "none";
		}
	};

	return (
		<header className={HeaderCSS.chatbotHeader}>
			<div className={HeaderCSS.logoContainer}>
				<a href="https://brocku.ca/" target="_blank" rel="noreferrer">
					<img className={HeaderCSS.logo} src={brockLogo} alt="logo" />
				</a>
			</div>
			<ul className={HeaderCSS.list}>
				<li className={HeaderCSS.listItem}>
					<img
						className={`${HeaderCSS.icon} ${HeaderCSS.help}`}
						src={helpIcon}
						alt="help"
						onClick={displayModal}
					/>
				</li>
				<li className={`${HeaderCSS.listItem} ${HeaderCSS.dropdown}`}>
					<img
						className={`${HeaderCSS.icon} ${HeaderCSS.settings}`}
						src={settingsIcon}
						alt="settings"
						onClick={toggleSettings}
					/>
					<ul ref={settingsMenu} className={HeaderCSS.dropdownMenu}>
						<li>
							<input type="checkbox" />
							<span>im super scuffed</span>
						</li>
						<li>
							<input type="checkbox" />
							<span>same lol</span>
						</li>
					</ul>
				</li>
			</ul>
		</header>
	);
};

export default Header;
