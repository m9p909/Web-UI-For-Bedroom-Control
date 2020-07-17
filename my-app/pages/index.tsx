import Head from "next/head";
import React, { Props } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Image from "react-bootstrap/Image";
import "react-dom";
import RaspberryPi from "../lib/RaspberryPi";
import { GetServerSideProps } from "next";

interface HomeProps {
  temp: number;
  light: number;
  humidity: number;
  roomEmpty: boolean;
}
//makes new raspPi
const PI_IP_ADDRESS = "http://localhost";
const PI_PORT = 808;
const pi = new RaspberryPi(PI_IP_ADDRESS, PI_PORT);
//Just renders the Index
export default class RunIndex extends React.Component<HomeProps> {
  render(): JSX.Element {
    const yes = "/green.png";
    const no = "/red.jpeg";
    let emptyRoom = "";
    if (this.props.roomEmpty) {
      emptyRoom = "yes";
    } else {
      emptyRoom = "no";
    }
    return (
      <div className="container">
        <Head>
          <title>Bed Control</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>
        <main>
          <Container>
            <h1> Bedroom App</h1>
            <Row>
              <Col>Temperature: {this.props.temp}</Col>
              <Col>Light: {this.props.light}</Col>
            </Row>
            <Row>
              <Col>Humidity:{this.props.humidity} </Col>
              <Col>Empty Room:{emptyRoom}</Col>
            </Row>
          </Container>
        </main>
      </div>
    );
  }
}
//Data gathering is done serverside for security
//function gets props from raspberry pi and sends them on each request of the page
export const getServerSideProps = async () => {
  const temp = await pi.getTemp();
  const light = await pi.getLight();
  const humidity = await pi.getHumidity();
  const roomEmpty = await pi.doorOpen();

  return {
    props: {
      temp,
      light,
      humidity,
      roomEmpty,
    },
  };
};
