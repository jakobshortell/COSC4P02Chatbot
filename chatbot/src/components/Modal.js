import React from "react";

// Styling
import ModalCSS from "../css/Modal.module.css";

// Assets
import brockLogo from "../assets/brock.png";

const Modal = ({ modal }) => {
	async function ModalClear() {
		modal.current.style.display = "none";
	}

	return (
		<div ref={modal} className={ModalCSS.shadow}>
			<div className={ModalCSS.modal}>
				<img className={ModalCSS.modalIcon} src={brockLogo} alt="logo" />
				<h1 className={ModalCSS.title}>
					Welcome to the Brock University Chatbot
				</h1>

				<div className={ModalCSS.info}>
					<h2 className={ModalCSS.intro}>What can this bot do?</h2>
					<ul>
						<li>Get information on Clubs &amp; Events</li>
						<li>Get information on specific BU courses &amp; programs</li>
						<li>Ask the chatbot about important dates</li>
						<li>Have fun little conversations!</li>
					</ul>
				</div>

				<p>*All information is scraped through the Brock University Website</p>
				<input type="button" value="I understand" onClick={ModalClear} />
			</div>
		</div>
	);
};

export default Modal;