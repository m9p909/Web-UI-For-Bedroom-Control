//Author: Jack Clarke
import "bootstrap/dist/css/bootstrap.min.css";
import NavBar from "../Components/navBar/NavBar";
import { AppProps } from "next/app";
import React from "react";

export default function MyApp({ Component, pageProps }: AppProps): JSX.Element {
  return (
    <>
      <NavBar></NavBar>
      <Component {...pageProps} />
    </>
  );
}
