import React from 'react';
import Chat from './Components/Chat';
import Sidebar from './Components/Sidebar';
import { Container, Row } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <Container fluid>
    	<Row>
	    	<Sidebar />
	      <Chat />
      </Row>
    </Container>
  );
}

export default App;