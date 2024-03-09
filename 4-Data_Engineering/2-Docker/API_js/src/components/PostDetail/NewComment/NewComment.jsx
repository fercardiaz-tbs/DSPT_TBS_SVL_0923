import React from "react";
import axios from "axios"


import "./NewComment.css"

const NewComment = ({commentsInfo}) => {

  const handleSubmit = async (e) =>{
    e.preventDefault();
    const commentData = {
      "postId": commentsInfo.postId,
      "name": "ChristianCiudad",
      "body": e.target.comment.value
    }
    axios.post('https://jsonplaceholder.typicode.com/comments', commentData)
      .then(res => {
        console.log("Comentario añadido correctamente!");
      })
      commentsInfo.changeCommentsList([commentData, ...commentsInfo.commentsList])
    e.target.comment.value = ''      
  }

  return (
    <div className="newCommentForm">
    <form onSubmit={handleSubmit}>
      <p className="userName" id='comment'>@ChristianCiudad</p>
      <input type='text' className="commentInput" placeholder="Write a comment..." name='comment'></input>
      <input className='postButton' type="submit" value="Comment"/>
    </form>
    </div>
  );
};

export default NewComment;
