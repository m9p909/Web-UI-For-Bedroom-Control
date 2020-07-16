import React from 'react';
import{Navbar,Nav,NavDropdown} from 'react-bootstrap';
import Link from 'next/link';
export default class NavBar extends React.Component{
    render(){
        return(
          
            <Navbar collapseOnSelect bg="dark" variant="dark">
            <Link href="/"><a className = "navbar-brand navbar-dark">Bed Control</a></Link>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
              <Nav className="mr-auto">
              <Link href="/ControlPanel"><a className="nav-link">ControlPanel</a></Link>
              </Nav>

            </Navbar.Collapse>
          </Navbar>
        )
    }

}