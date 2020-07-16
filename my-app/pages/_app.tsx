import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from '../Components/navBar/navBar';
import {AppProps} from 'next/app';

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
    <NavBar></NavBar>
  <Component {...pageProps} />
  </>
  )
}