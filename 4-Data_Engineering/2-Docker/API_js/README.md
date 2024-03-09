# Frontend Assesment - Fusuma

This repository is designed to evaluate developer basic skills using React.js

## Background

This app is created using `create-react-app`. It uses simple CSS styling following the templates recommendations. In this project a Post / Comments app needs to be implemented that allows:

1. List all the Posts in the Database
2. Navigate to the view of a post (Popup or new route)
3. Add a comment to a Post
4. Create a new Post
5. Delete a Post

## How to submit ?

In order to submit your solution create a Fork and create a Pull Request. Feel free to add comments to your request.
### Considerations

* Backend server is mocked using `json-server`. A script is added in `package.json`. Run `npm run serve` to start the server at `http://localhost:3001`.
* No user data or authentication is required, users are identified by username to keep the project simple.
* Developers are free to use whatever framework or solution you feel confortable with.

## Recomendations
* To show the detail view of the Posts use a simple React Router implementation or Popup.
* Take care in being consistant with your code: Name conventions, scafolding, orderings.
* Global state management is not required for the minimum requirements. Feel free to introduce Redux or Context but focus in meeting the requirements.

## Extra

As an extra challenge, you can focus on the Data access layer of the project. If you followed the scafolding proposed at the beggining, both `services/comments.js`and `services/posts.js` must be very similar. Take some time in refactoring how the application access the db in a way that you repeat as less code as possible and its easy to add services for new endpoints.


## Final Thoughts

Feel free to contact us at `fran@fusuma.io` or `adrian@fusuma.io` for information. Good luck and happy coding!

