import React, {useState, useEffect} from "react";
import { Link, useSearchParams } from 'react-router-dom'

import Post from "../Post/Post"
import NewComment from "./NewComment/NewComment"
import CommentList from "../CommentList/CommentList"
import { getPostById } from "../../services/posts";
import {getCommentByPostId} from "../../services/comments.js"
import './PostDetail.css'


const PostDetail = (props) => {

  const [searchParams] = useSearchParams();
  const [postDetail, changePostDetail] = useState({});
  const [commentsList, changeCommentsList] = useState([]);
  const [loading, setLoading] = useState(true)

  const postId = searchParams.get('id')
  const commentsInfo={
    commentsList,
    changeCommentsList,
    postId
  }

  useEffect(()=>{
    const getPostDetail = async (id) => {
      const data = await getPostById(id)
      changePostDetail(data)
      setLoading(false)
    }
    const getCommentsDetail = async (id) => {
      const data = await getCommentByPostId(id)
      changeCommentsList(data)

    }
    getPostDetail(postId)
    getCommentsDetail(postId)
  },[])

  return <div>
  {
    loading 
      ? <p>loading...</p> 
      : <div className="noHover">
      <Link to="/"><button className='postButton' value="Submit">Home</button></Link>
      <Post postInfo={postDetail}/>
      <NewComment commentsInfo={commentsInfo}/>
      <CommentList commentsList={commentsList}/>
      </div>
  }
  </div>;
};

export default PostDetail;
