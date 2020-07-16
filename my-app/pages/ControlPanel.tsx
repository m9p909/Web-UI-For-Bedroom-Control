import Head from "next/head";
import React from "react";

export default class Home extends React.Component {
  render(): JSX.Element {
    return (
      <div className="container">
        <Head>
          <title>Create Next App</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>

        <main></main>
      </div>
    );
  }
}
