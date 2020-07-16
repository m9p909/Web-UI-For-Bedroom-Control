import Head from 'next/head'
import React from 'react';
import NavBar from '../Components/navBar/navBar';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import 'react-dom';
export default class Home extends React.Component{
  render(){
    return(
    <div className="container">
    <Head>
      <title>Create Next App</title>
      <link rel="icon" href="/favicon.ico" />
      
    </Head>
    <main>
    <Container>
    <h1> Control Panel</h1>
    <Row>
      <Col>I like trains</Col>
    </Row>
    </Container>
    

    </main>
  </div>
    )
  }
}
