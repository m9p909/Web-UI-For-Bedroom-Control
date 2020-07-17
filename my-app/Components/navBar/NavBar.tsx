import React from "react";
import { Navbar, Nav } from "react-bootstrap";
import Link from "next/link";
import NavButton from "./NavButton";
//partially copied from the bootstrap React examples: https://react-bootstrap.netlify.app/components/navbar/#navbars
export default class NavBar extends React.Component {
  render(): JSX.Element {
    return (
      <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
        <Link href="/">
          <a className="navbar-brand navbar-dark">Bed Control</a>
        </Link>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="mr-auto">
            <NavButton href="/ControlPanel" text="Control Panel" />
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}
