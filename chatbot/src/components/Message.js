import React from "react";
import Linkify from "react-linkify";

// Styling
import MessageCSS from "../css/Message.module.css";

// Assets
import botIcon from "../assets/brock.png";
import userIcon from "../assets/user.png";
import linkIcon from "../assets/linkRed.png";

const Message = ({ author, content, time }) => {
	if (author === "user") {
		return (
			<li className={` ${MessageCSS.message} ${MessageCSS.userMessage} `}>
				<img
					className={MessageCSS.messageIcon}
					src={userIcon}
					alt="user-icon"
				/>
				<div
					className={` ${MessageCSS.messageBubble} ${MessageCSS.userMessageBubble} `}
				>
					<div>
						<span className={` ${MessageCSS.userName} ${MessageCSS.name} `}>
							You
						</span>
						<span className={MessageCSS.time}>{time}</span>
					</div>
					<span>{content}</span>
				</div>
			</li>
		);
	} else {
		return (
			<li className={` ${MessageCSS.message} ${MessageCSS.botMessage} `}>
				<img className={MessageCSS.messageIcon} src={botIcon} alt="bot-icon" />
				<div
					className={` ${MessageCSS.messageBubble} ${MessageCSS.botMessageBubble} `}
				>
					<div>
						<span className={` ${MessageCSS.botName} ${MessageCSS.name} `}>
							Brock University
						</span>
						<span className={MessageCSS.time}>{time}</span>
					</div>
					<span>
						<Linkify
							componentDecorator={(decoratedHref: string, key: Key) => (
								<SecureLink href={decoratedHref} key={key}>
									{decoratedHref}
									<img className={MessageCSS.link} src={linkIcon} alt="Link" />
								</SecureLink>
							)}
						>
							{content}
						</Linkify>
					</span>
				</div>
			</li>
		);
	}
};
export default Message;
