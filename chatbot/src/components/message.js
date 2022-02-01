import React from "react";
import planet from '../assets/planet.png';
import User from '../assets/User.png';
export function Message({ author, content }) {
	if (author == 'User') {
		return (
			<p class="box1 sb1"><img src={User} class="botimg" alt="User" />{content}</p>
		)
	}
	return (
		<><p class="box2 sb2" id="test"><img src={planet} class="botimg" alt="planet" />{content}</p></>
	)
	
}