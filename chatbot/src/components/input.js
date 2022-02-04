import React from 'react';

export function Input({ userInput, onClick }) {

	return (
		<div className='input-container'>
			<input className='input-field' ref={userInput} type='text' />
			<button type='button' className='send-button' onClick={onClick}>Send</button>
		</div>
	)

}