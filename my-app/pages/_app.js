import bootstrap from 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from '../Components/navBar/navBar';
export default function MyApp({ Component, pageProps }) {
  return (
    <>
    <NavBar></NavBar>
  <Component {...pageProps} />
  </>
  )
}