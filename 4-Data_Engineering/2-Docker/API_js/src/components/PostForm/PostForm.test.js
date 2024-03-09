import React from "react";
import { shallow } from "enzyme";
import PostForm from "./PostForm";

describe("PostForm", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<PostForm />);
    expect(wrapper).toMatchSnapshot();
  });
});
