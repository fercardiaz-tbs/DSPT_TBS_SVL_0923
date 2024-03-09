import React from "react";

import './Post.css'

const Post = (props) => {

  const infoPost = props.postInfo  

  return (
    <div className="post">
      <h3 className="postTitle">{infoPost.title.toUpperCase().slice(0,10)}</h3>
      <p className="userName">@Prueba</p>
      <p className="postText"> {infoPost.body}</p>
    </div>
  );
};

export default Post;
