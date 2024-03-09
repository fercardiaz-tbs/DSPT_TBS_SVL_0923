import React from "react";
import { shallow } from "enzyme";
import PostList from "./PostList";

describe("PostList", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<PostList />);
    expect(wrapper).toMatchSnapshot();
  });
});
