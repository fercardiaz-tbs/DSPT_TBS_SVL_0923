import React from "react";

import Comment from "../Comment"


const CommentList =({commentsList}) => {

  const paintComments = () =>{

    return  commentsList.slice(0,10).map((commentInfo,i)=><Comment key={i} commentInfo={commentInfo}/>)    
   }   

  return <div className="commentList">
  {commentsList?paintComments():null}
  </div>;
};

export default CommentList;
