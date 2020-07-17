[1mdiff --git a/my-app/Components/navBar/NavBar.tsx b/my-app/Components/navBar/NavBar.tsx[m
[1mindex 4d711c1..94cb618 100644[m
[1m--- a/my-app/Components/navBar/NavBar.tsx[m
[1m+++ b/my-app/Components/navBar/NavBar.tsx[m
[36m@@ -6,16 +6,14 @@[m [mimport NavButton from "./NavButton";[m
 export default class NavBar extends React.Component {[m
   render(): JSX.Element {[m
     return ([m
[31m-      <Navbar collapseOnSelect bg="dark" variant="dark">[m
[31m-        <Link href="/">[m
[31m-          <a className="navbar-brand navbar-dark">Bed Control</a>[m
[31m-        </Link>[m
[32m+[m[32m      <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">[m
[32m+[m[32m        <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>[m
         <Navbar.Toggle aria-controls="responsive-navbar-nav" />[m
         <Navbar.Collapse id="responsive-navbar-nav">[m
           <Nav className="mr-auto">[m
[31m-            <NavButton href="/ControlPanel" text="Control Panel" />[m
[31m-            <NavButton href="/mood" text="Mood" />[m
[31m-            <NavButton href="/settings" text="Settings" />[m
[32m+[m[32m            <NavButton href="/Control" text="Control Panel" />[m
[32m+[m[32m            <NavButton href="/" text="home" />[m
[32m+[m[32m            <NavButton href="/" text="home" />[m
           </Nav>[m
         </Navbar.Collapse>[m
       </Navbar>[m
