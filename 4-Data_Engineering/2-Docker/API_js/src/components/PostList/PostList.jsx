import React from "react";
import {Link} from 'react-router-dom'

import './PostList.css'

import Post from '../Post'

const PostList = (props) => {

  const postList = props.postInfo.postList

  const paintPosts = () =>{
    if(props.postInfo){


      return postList.slice(0,5).map((postInfo,i)=><div className="postList" key={postInfo.id}><Link to={`/post/?id=${postInfo.id}`}><Post postInfo={postInfo} key={postInfo.id}/></Link><button className='postButton' onClick={()=>props.postInfo.deletePost(i,postInfo.id)}>Borrar</button></div>)
    }
   }   
  return <div className="productList">
      {paintPosts()}
  </div>;
};

export default PostList;
