import React from "react";
import { Nav, Col } from "react-bootstrap";
import '../../styles/sidebar.css'
import logo from '../../maverick_logo.png'

export default function Sidebar() {
  return (
    <Col xs ={2} id="sidebar-wrapper">
      <Nav className="col-md-12 d-none d-md-block bg-light sidebar">
        <div className="sidebar-sticky"></div>
        <Nav.Item className="nav-name">
          <b><h3>BusinessBot</h3></b>
          <span style={{color: 'grey'}}>Building the future</span>
        </Nav.Item>
        <Nav.Item className="nav-footer">
          <img src={logo} alt="Maverick"/><br/>
          IIT Kharagpur<br />
          Team:<b> MonsterTrio</b>
        </Nav.Item>
      </Nav>
    </Col>
  );
};