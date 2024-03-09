import React from "react";

import {Link} from 'react-router-dom'

import './NewPost.css'

const NewPost = () => {
  return (
    <div>
    <Link to='/newpost'>
    <button className="newPostButton"> + NEW POST</button>
    </Link>

    </div>)
};

export default NewPost;
