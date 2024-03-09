import React from "react";
import { shallow } from "enzyme";
import CommentList from "./CommentList";

describe("CommentList", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<CommentList />);
    expect(wrapper).toMatchSnapshot();
  });
});
