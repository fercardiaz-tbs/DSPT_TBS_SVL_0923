import React from "react";
import { shallow } from "enzyme";
import PostDetail from "./PostDetail";

describe("PostDetail", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<PostDetail />);
    expect(wrapper).toMatchSnapshot();
  });
});
