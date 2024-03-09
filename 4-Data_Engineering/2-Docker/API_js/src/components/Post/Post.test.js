import React from "react";
import { shallow } from "enzyme";
import Post from "./Post";

describe("Post", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<Post />);
    expect(wrapper).toMatchSnapshot();
  });
});
