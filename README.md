# Welcome to Your Reddit Clone

Your Reddit Clone is a web application designed to replicate some of the functionalities and features of the popular social media platform Reddit. It allows users to create accounts, submit posts, comment on posts, and interact with other users through voting and discussions.

## How to Use
* Become a new user by registering a username, email (optional), and password.
* Upon successful registration, entire access posts, comments, and subreddits will be granted.
* Registered users can create new posts inside a subreddit of their choice.
* Registered users can also Comment and upvote or downvote posts.
* The total number of upvotes and downvotes is displayed alongside each post.
* Users can add a profile picture and bio to their profile page.
* Users can update their profile information, including their profile picture and bio.

## Features

### User Registration and Authentication
<img width="910" alt="Screenshot 2023-06-29 at 23 10 52" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/619b1d72-1e80-48c1-b82a-4ca0bc51693a">
* Users can signup for an account with a unique username, email, and password by clicking on the Register link on the navbar.

<img width="901" alt="Screenshot 2023-06-29 at 23 12 37" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/817ee35d-8dcd-442e-81b2-91d01ff9076c">
* Users can later log in with the same account by clicking on the login link on the navbar.

<img width="911" alt="Screenshot 2023-06-29 at 23 15 23" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/463dc61a-c37f-49fc-914c-eb630f141c5c">
* When leaving, users can log out of their accounts by clicking the logout link on the navbar.

### Homepage and Navigation
<img width="1512" alt="Screenshot 2023-06-29 at 23 08 54" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/c803a11e-b0cd-4933-8d3e-aa453afb7af0">
* The homepage showcases a feed of the most popular posts based on the upvotes to downvotes ratio.
* All the subreddits are displayed on the sidebar.

### Making posts and comments
<img width="1159" alt="Screenshot 2023-06-29 at 23 26 38" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/060802b5-418f-42ce-bf77-4e3c5c87b522">
* Inside a subreddit of choice a registered user can create a new post with a title, slug, and content.

<img width="1159" alt="Screenshot 2023-06-29 at 23 26 38" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/7dcbb9bd-4973-4830-bdd6-1278c39c1aa5">
* All posts from the same subreddit are displayed inside the subreddit page and categorized on the homepage by displaying the subreddit tag.

<img width="1069" alt="Screenshot 2023-06-29 at 23 31 13" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/f52abbea-8dec-4ae6-bc37-a04df0cd07ad">
* Other users can upvote or downvote posts to indicate their preference.
* Posts with the highest ratio of upvotes to downvotes will be displayed first.
* Comments can be added to posts, fostering discussions and interactions.

### Future Enhancements
* User Profiles and Customization feature where users can add a profile picture and bio when registering to later revisit or edit.
* Friend request feature where users can add each other and connect.
* A search bar with sorting options for a better browsing experience.
* Moderation tools to manage and enforce community guidelines.
* A 'slugify' feature where the slugs for posts will generate automatically.

## Testing & Debugging
* The user tested high in accessibility, performance, and best practices.
<img width="599" alt="Screenshot 2023-06-29 at 22 50 10 1" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/596165f3-d954-465b-a537-c99986e2a532">
* Manual and automated tests were carried out during the development of the application.
* An initial problem when posting on a subreddit was solved by adding a slug field inside the post.

## Credits

This project was made possible with the initial guidance of my tutor Akshat Garg and the support of tutors from Code Institute.
The following external sources were consulted:
Code Institute for providing the necessary tools, guidance, and inspiration.
Stack Overflow and other online developer communities for troubleshooting and problem-solving.
The following websites were consulted for additional information and guidance:
https://djangocentral.com/creating-comments-system-with-django/
https://stackoverflow.com/questions/21123559/django-redirect-all-non-authenticated-users-to-landing-page
https://docs.djangoproject.com/en/4.2/ref/models/fields/
https://django-crispy-forms.readthedocs.io/en/latest/index.html
https://www.devhandbook.com/django/user-profile/
