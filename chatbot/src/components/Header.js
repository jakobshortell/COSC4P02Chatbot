import React, { useRef } from "react";

// Styling
import HeaderCSS from "../css/Header.module.css";

// Assets
import brockLogo from "../assets/brocklogo.jpeg";
import settingsIcon from "../assets/setting.png";
import helpIcon from "../assets/help.png";
import copyIcon from "../assets/copy.png";

const Header = ({ modal, language }) => {
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

	const saveLogs = () => {
		const lines = new Array();
		var msg = '';
		let messages = document.querySelectorAll('[class*="Message_messageBubble"]');
		messages.forEach(function(message){
			let messagecontent = message.querySelectorAll("span");
			msg = messagecontent[2].innerHTML.replaceAll('mailto:', '');
			msg = msg.replaceAll('<a target="_blank" rel="noopener noreferrer" href="', '');
			msg = msg.replaceAll('">Link<img class="Message_link__oEo7f" src="/static/media/linkRed.41693c8127b2c2eede2e.png" alt="Link"></a>', '');
			lines.push(messagecontent[0].innerHTML.concat(" (", messagecontent[1].innerHTML.concat("): ", msg)));
			
		});
		let toCopy = lines.join("\n");
		alert("Chatlog copied to clipboard");
		var copy = document.createElement("textarea");
		document.body.appendChild(copy);
		copy.value = toCopy;
		copy.select();
		document.execCommand("copy");
		document.body.removeChild(copy);
	};

	return (
		<header className={HeaderCSS.chatbotHeader}>
			<div className={HeaderCSS.logoContainer}>
				<a href="https://brocku.ca/" target="_blank" rel="noreferrer">
					<img
						className={HeaderCSS.logo}
						src={brockLogo}
						alt="logo"
					/>
				</a>
			</div>
			<ul className={HeaderCSS.list}>
				<li className={HeaderCSS.listItem}>
					<img
						className={`${HeaderCSS.icon} ${HeaderCSS.help}`}
						title="Help"
						src={helpIcon}
						alt="help"
						onClick={displayModal}
					/>
				</li>
				<li className={HeaderCSS.listItem}>
					<img
						className={`${HeaderCSS.icon} ${HeaderCSS.copy}`}
						title="Copy Chatlog to Clipboard"
						src={copyIcon}
						alt="Copy Chatlog"
						onClick={saveLogs}
					/>
				</li>
				<li className={`${HeaderCSS.listItem} ${HeaderCSS.dropdown}`}>
					<img
						className={`${HeaderCSS.icon} ${HeaderCSS.settings}`}
						title="Settings"
						src={settingsIcon}
						alt="settings"
						onClick={toggleSettings}
					/>
					<ul ref={settingsMenu} className={HeaderCSS.dropdownMenu}>
						<li>
							<label
								className={HeaderCSS.languageLabel}
								for="language"
							>
								Language
							</label>
							<select
								ref={language}
								className={HeaderCSS.languageSelector}
								id="language"
							>
								<option value="en">EN</option>
							</select>
						</li>
					</ul>
				</li>
			</ul>
		</header>
	);
};

export default Header;