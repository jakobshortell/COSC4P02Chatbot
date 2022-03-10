import React from 'react';

// Styling
import InputCSS from '../css/Input.module.css';

// Assets
import sendIcon from '../assets/send.png';

const Input = ({ userInput, onClick }) => {

	return (
		<div className={ InputCSS.inputContainer }>
			<textarea className={ InputCSS.inputField } type='text' ref={ userInput } rows='1' placeholder='Type your question here' />
			<button className={ InputCSS.sendButton } type='button' onClick={ onClick }>
				<img className={ InputCSS.sendButtonImage } src={ sendIcon } alt='sendButtonImage' />
			</button>
		</div>
	)

}

export default Input;