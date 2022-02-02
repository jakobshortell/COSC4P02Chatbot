import React from "react";
import planet from './planet.png';
import User from './User.png';
export function Message({ author, content }) {
	if (author == 'User') {
		return (
			<p class="box1 sb1"><img src={User} class="botimg" alt="User" />{content}</p>
		)
	}
	return (
		<><p class="box2 sb2"><img src={planet} class="botimg" alt="planet" />{content}</p></>
	)
	
}