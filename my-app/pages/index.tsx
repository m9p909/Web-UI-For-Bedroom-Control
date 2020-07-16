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
const pi = new RaspberryPi("IpAddress", 1234);
export default class RunIndex extends React.Component<HomeProps> {
  render(): JSX.Element {
    const yes = "/green.png";
    const no = "/red.jpeg";
    let emptyRoom = "";
    if (this.props.roomEmpty) {
      emptyRoom = yes;
    } else {
      emptyRoom = no;
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
              <Col>
                Empty Room:
                <Image src={emptyRoom} roundedCircle></Image>
              </Col>
            </Row>
          </Container>
        </main>
      </div>
    );
  }
}

export const getServerSideProps = async () => {
  const temp = pi.getTemp();
  const light = pi.getLight();
  const humidity = pi.getHumidity();
  const roomEmpty = pi.getRoomEmpty();

  return {
    props: {
      temp,
      light,
      humidity,
      roomEmpty,
    },
  };
};
