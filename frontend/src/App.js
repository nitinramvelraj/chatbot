import React, { useState, useEffect, useRef } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const ws = useRef(null);

  useEffect(() => {
    // Connect to WebSocket server
    ws.current = new WebSocket('wss://3.128.21.121/ws/chat');
    
    ws.current.onopen = () => console.log("connected to ws");
    ws.current.onclose = (e) => console.log("ws connection closed", e);

    ws.current.onmessage = (e) => {
      const message = { message: e.data, sender: 'bot' };
      setMessages(prevMessages => [...prevMessages, message]);
    };

    return () => {
      ws.current.close();
    };
  }, []);

  const sendMessage = (e) => {
    e.preventDefault();
    if (input.trim()) {
      ws.current.send(JSON.stringify({ message: input }));
      setMessages(prevMessages => [...prevMessages, { message: input, sender: 'user' }]);
      setInput('');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Elisity Chatbot</h1>
      </header>
      <div className="chat-container">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.message}
          </div>
        ))}
      </div>
      <form onSubmit={sendMessage} className="input-form">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message here..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;
