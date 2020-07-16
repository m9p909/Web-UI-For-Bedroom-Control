import Head from 'next/head'
import React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import 'react-dom';

interface HomeProps {
  temp:Number;
  
}
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
    <h1> Bedroom App</h1>
    <Row>
      <Col></Col>
    </Row>
    </Container>
    

    </main>
  </div>
    )
  }
}

export async function getServerSideProps(){

}