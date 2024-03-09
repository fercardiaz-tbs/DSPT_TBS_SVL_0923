import React from "react";
import { shallow } from "enzyme";
import NewPost from "./NewPost";

describe("NewPost", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<NewPost />);
    expect(wrapper).toMatchSnapshot();
  });
});
