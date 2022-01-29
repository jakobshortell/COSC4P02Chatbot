import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';

function App() {

	const [data, setData] = useState({})

	useEffect(() => {
		fetch('/api').then((response) => {
			if (response.ok) {
				return response.json();
			}
		}).then((data) => {
			setData(data);
		})
	});

	return (
		<div className="App">
			<header className="App-header">
				<img src={logo} className="App-logo" alt="logo" />
				<p><code>{JSON.stringify(data)}</code></p>
				<a className="App-link" href="https://reactjs.org" target="_blank" rel="noopener noreferrer">Learn React</a>
			</header>
		</div>
	);

}

export default App;