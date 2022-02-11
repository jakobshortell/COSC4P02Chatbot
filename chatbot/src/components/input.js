import React from 'react';

import sendIcon from '../assets/send.png';

export function Input({ userInput, onClick }) {

	return (
		<div className='input-container'>
			<textarea className='input-field' type='text' ref={userInput} rows='1' placeholder='Type your question here' />
			<button className='send-button' type='button' onClick={onClick}>
				<img className='send-button-image' src={sendIcon} alt='sendButtonImage' />
			</button>
		</div>
	)

}