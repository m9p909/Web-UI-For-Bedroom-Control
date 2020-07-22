//Author: Jack Clarke
import React from "react";
import NavButton from "../Components/navBar/NavButton";
import renderer from "react-test-renderer";



it("button renders correctly", () => {
  const tree = renderer
    .create(<NavButton href="/" text="I like to eat" />)
    .toJSON();
  expect(tree).toMatchSnapshot();
});
