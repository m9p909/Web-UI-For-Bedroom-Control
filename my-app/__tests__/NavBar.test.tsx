import React from "react";
import NavButton from "../Components/navBar/NavButton";
import renderer from "react-test-renderer";
import NavBar from "../Components/navBar/NavButton";
import { Screen } from "react-testing-library";

it("button renders correctly", () => {
  const tree = renderer
    .create(<NavButton href="/" text="I like to eat" />)
    .toJSON();
  expect(tree).toMatchSnapshot();
});
