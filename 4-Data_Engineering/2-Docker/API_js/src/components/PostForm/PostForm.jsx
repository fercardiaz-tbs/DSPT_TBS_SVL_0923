import React from "react";
import {Link} from "react-router-dom"

import axios from 'axios';

import { useNavigate } from "react-router-dom";

import './PostForm.css'

const PostForm = (props) => {

  const navigate = useNavigate();

  const handleSubmit = (e) =>{
    e.preventDefault();
    let postData = {
      "name": e.target.title.value,
      "user": "ChristianCiudad",
      "text": e.target.text.value
    }
    axios.post(`https://jsonplaceholder.typicode.com/posts`, postData)
      .then(res => {
        console.log(res);
        const postDataState = {
          "id" : res.data.id,
          "title": e.target.title.value,
          "body": e.target.text.value
        }
        props.newPostInfo.newPost(postDataState)
      })
      navigate('/')
      
  }

  return (
    <div>
    <Link to="/"><button className='postButton' value="Submit">Home</button></Link>
    <form className="postForm" onSubmit={handleSubmit}>
      <input type='text' className="formTitle" placeholder="Write a title..." name='title'></input>
      <textarea className="formText" placeholder="Here comes your post..." name='text'></textarea>
      <button className='postButton' type="submit" value="Submit">Post</button>
    </form>
    </div>
  );
};

export default PostForm;
