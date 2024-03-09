import React from "react";
import { shallow } from "enzyme";
import NewComment from "./NewComment";

describe("NewComment", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<NewComment />);
    expect(wrapper).toMatchSnapshot();
  });
});
