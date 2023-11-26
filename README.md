# Welcome to Reddit Clone

Reddit Clone is a dynamic web application inspired by Reddit, focusing on community engagement and interactive content sharing. It offers a familiar yet unique platform for users to explore, discuss, and connect. Our goal is to replicate key functionalities of Reddit, including account creation, post submission, commenting, and user interaction through voting and discussions.

## Table of Contents
* [Introduction](#introduction)
  * [How to Use](#how-to-use)
* [Strategy](#strategy)
  * [Goals and Requirements](#goals-and-requirements)
* [Structure Plane](#structure-plane)
  * [User Stories](#user-stories)
  * [Database Schema](#database-schema)
* [UX Planning](#ux-planning)
  * [Wireframes](#wireframes)
  * [Color Palette](#color-palette)
* [Features](#features)
  * [User Registration and Authentication](#user-registration-and-authentication)
  * [Homepage and Navigation](#homepage-and-navigation)
  * [Making Posts and Comments](#making-posts-and-comments)
  * [Subreddits](#subreddits)
  * [User Profile](#user-profile)
  * [Admin Panel and Content Moderation](#admin-panel-and-content-moderation)
  * [Future Enhancements](#future-enhancements)
* [Testing and Deployment](#testing-and-deployment)
* [Technologies](#technologies)
* [Credits](#credits)
  * [Acknowledgments](#acknowledgments)
  * [Sources](#sources)


## Introduction
### How to Use
* **Registration**: Sign up with a username, email (optional), and password.
* **Interaction**: Access posts, comments, and subreddits upon successful registration.
* **Content Creation**: Create new posts within chosen subreddits.
* **Engagement**: Comment, upvote, or downvote posts. View the total count of votes for each post.

## Strategy
### Goals and Requirements

* **Connection**: Create a platform where users connect through engaging in discussions, making posts, leaving comments, voting on posts.

* **Content Organization**: Implement a system to categorize content into various topics or "subreddits" to allow for easier navigation and focused discussions.

* **User Experience**: Design an intuitive and responsive user interface that provides a seamless experience across different devices.

* **Security**: Implement robust authentication and authorization to protect user data and prevent common security threats.

## Structure Plane
### User Stories
User stories are critical to ensuring that the functionality of the Reddit Clone meets the needs of its users. Acceptance criteria specify the boundaries of a user story and are used to confirm when a story is completed and working as intended.

| As a/an          | I want to be able to...                         | So that I can...                                | Acceptance Criteria |
|------------------|-------------------------------------------------|-------------------------------------------------|---------------------|
| User             | view a paginated list of posts                  | browse through content in an organized manner   | - The number of posts per page is consistent |
| Registered User  | log in and out of my account                    | securely manage my session                      | - The login form requires a username and password<br>- Users see a confirmation message and are redirected to the homepage upon login<br>- A logout option is available and redirects to the homepage upon use |
| User             | access any subreddit                            | engage with different communities              | - A list of subreddits is visible and accessible from the main navigation or homepage<br>- Users can click on a subreddit and view a list of posts associated with it<br>- The interface for accessing subreddits is intuitive |
| Admin            | create drafts of posts before they are published | ensure the quality and relevance of the content | - Admins have the option to save a post as a draft<br>- Drafts are stored in an admin-specific area where they can be reviewed, edited, or deleted |
| Admin            | create and manage subreddits                    | maintain the quality and organization of the platform | - Admins have the ability to create a new subreddit with necessary details<br>- Admins can edit or delete a subreddit as necessary |
| User             | view the comments on a post                     | read and engage with the discussions            | - Users can click on a post and be directed to a detailed view where comments are displayed<br>- Comments are displayed in a nested format showing replies to individual comments<br>- The number of comments on a post is displayed on the post summary |
| Admin            | access advanced moderation tools in the admin panel | effectively manage the platform                 | - Admins have a dedicated moderation panel with tools for content review<br>- Admins can sort and filter content that requires attention |
| Admin            | moderate posts and comments                     | keep the platform appropriate and safe          | - Admins have easy access to moderation tools<br>- Admin actions on posts and comments are logged and can be reviewed |
| User             | have a responsive design application            | have a consistent experience across all devices | - The application is usable on screens as small as 320px wide without horizontal scrolling or elements overlapping<br>- Media queries are used to adapt the layout to different screen sizes<br>- Touch targets are appropriately sized for mobile users |
| User             | upvote and downvote posts                       | express my opinion on the content              | - Each post has an upvote and downvote button<br>- Clicking the upvote button increases the score by 1, clicking again undoes the upvote<br>- Clicking the downvote button decreases the score by 1, clicking again undoes the downvote<br>- The current score is displayed between the upvote and downvote buttons |
| User             | delete posts and comments I made                | correct mistakes or remove outdated information | - Users can delete their own posts and comments |
| User             | comment on a post                               | engage with the post and express myself         | - A comment input box is visible below the post content<br>- Users can submit a comment and it immediately appears in the Admin panel <br>- Users receive feedback upon successful submission or an error message if the submission fails |
| User             | create a new post                               | share and express my thoughts with a community  | - The "Create Post" button is visible on the main page<br>- Clicking the "Create Post" button takes the user to a form where they can enter a title and body text<br>- Submitting the form creates a new post which then appears on the homepage |
| User             | enter a profile picture and bio                 | personalize my profile and see my activity      | - Users can upload a profile picture and write a bio in their profile settings<br>- Users have a section to view their own activity including posts and comments |
| User             | edit their own posts                            | update information or correct errors            | - An edit button is available on the user's own posts<br>- Users can change the content of their posts and save changes |


### Database Schema
The database schema  was generated using dbdiagram.io. It outlines the relationships between users, posts, comments, and subreddits, ensuring efficient data management and retrieval.

![databasediagram](https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/7debb626-5eef-44fc-8246-436e98ee3ee6)


## UX Planning
### Wireframes
**Homepage**
* The homepage for the Reddit Clone has been crafted with a minimalist design ethos using Figma. It features a prominent posting button, a feed of the latest discussions, and an easy-to-navigate subreddit sidebar, all laid out to foster a community-driven experience.

![homepage_wireframe](https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/f48bf89e-05a8-4869-84cc-480d5cae6f3e)


**Subreddit Page**
* Created with Figma, this design underscores a content-centric subreddit page that's both minimalist and functional, ensuring users can focus on reading and engaging with posts.

![subreddit-wireframe](https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/8aace0e6-b78f-45ab-b394-f8e060e27fce)

**Post Detail Page**
* The post detail page is structured to focus on individual post interactions, enabling users to read, comment, and engage with specific content. Crafted using Figma, the design offers a comment section directly below the post, encouraging active discussions.

![post-detail-wireframe](https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/068796f8-4601-42c3-bb4c-6910edbd2681)


### Color Palette

Our design uses a refined color palette to create a visually harmonious user interface. The colors are selected to ensure readability, draw attention to key areas, and reflect the branding of our Reddit Clone project.

Here are the primary colors used in the design:

![IMG_0184](https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/2b0fb2f6-63ab-4933-bfa6-9522075b7bde)


## Features
### User Registration and Authentication

<img width="910" alt="Screenshot 2023-06-29 at 23 10 52" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/619b1d72-1e80-48c1-b82a-4ca0bc51693a">

<img width="901" alt="Screenshot 2023-06-29 at 23 12 37" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/817ee35d-8dcd-442e-81b2-91d01ff9076c">

<img width="911" alt="Screenshot 2023-06-29 at 23 15 23" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/463dc61a-c37f-49fc-914c-eb630f141c5c">

* Users can signup for an account with a unique username, email, and password by clicking on the Register link on the navbar.
* Secure authentication system to protect user accounts.

### Homepage and Navigation
* The homepage showcases a feed of the most popular posts based on the upvotes to downvotes ratio.
* All the subreddits are displayed on the sidebar.

### Making Posts and Comments
* Intuitive interface for post creation within user-selected subreddits.
* Facilitated discussions through a robust commenting system.

## Subreddits

## User Profile

### Admin Panel and Content Moderation

<img width="1512" alt="Screenshot 2023-06-30 at 09 26 25" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/8d983e7e-5769-49b3-8ea1-d507f1466958">

* A registered admin (superuser) can access the admin panel where all posts, comments, subreddits, and profiles (future) can be edited or deleted.

<img width="1510" alt="Screenshot 2023-06-30 at 09 34 03" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/ede8ea3e-a2c5-4004-99b2-ca59458fdaf3">

<img width="1510" alt="Screenshot 2023-06-30 at 09 34 03" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/ede8ea3e-a2c5-4004-99b2-ca59458fdaf3">

* Posts can be filtered by their 'status' and 'created on' or searched on the search bar for easier access.
* A new post can also be made by an admin by clicking 'add post +'.
* Admins can edit and change the status of posts (from 'Draft' to 'Published' and vice versa) which allows the posts made by users to be displayed on the homepage. 

<img width="1509" alt="Screenshot 2023-06-30 at 09 42 19" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/aa993318-0204-4c7a-8d26-5960f4bb0914">

* Comments can also be moderated by admins by clicking the 'Comments' section on the admin panel.
* Similarly to the 'Posts' section the 'Comments' allows all comments to be filtered for easier access.
* All comments made by users must be approved by admins before displaying under a post.
* Admins can also make new comments by clicking on the 'Add Comment +' button.

<img width="1509" alt="Screenshot 2023-06-30 at 09 47 19" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/6f367407-9311-47c7-b967-56cd7e9414d4">

* The 'Subreddits' section allows registered admins to filter, edit and delete subreddits.
* New subreddits can only be created by admins through the admin panel by clicking on 'Add Subreddit.

### Future Enhancements
* Introduction of friend requests and direct messaging.
* Advanced search and sorting functionalities.
* Enhanced moderation tools for community guideline enforcement.

## Testing and Deployment
* Extensive testing covering accessibility, performance, and best practices.
* Iterative development with manual and automated testing to ensure functionality.
* The app tested high in accessibility, performance, and best practices.

<img width="599" alt="Screenshot 2023-06-29 at 22 50 10 1" src="https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/596165f3-d954-465b-a537-c99986e2a532">

## Credits
### Acknowledgments
* Special thanks to mentor Akshat Garg and the Code Institute's tutor team.
* Gratitude to online communities like Stack Overflow for their invaluable support.
* Recognition of various resources and documentation that guided the project's development.

### Sources
* The following websites were consulted for additional information and guidance:
https://djangocentral.com/creating-comments-system-with-django/
https://stackoverflow.com/questions/21123559/django-redirect-all-non-authenticated-users-to-landing-page
https://docs.djangoproject.com/en/4.2/ref/models/fields/
https://django-crispy-forms.readthedocs.io/en/latest/index.html
https://www.devhandbook.com/django/user-profile/
