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

The homepage of Clone|Reddit serves as the central hub for user interaction and content discovery. Here's what users will find:

- **Navigation Header**: At the top, users are greeted with the Clone|Reddit logo and options for profile access and logging out, providing a clear path to account management.
  
- **Create Post**: Users are invited to contribute to the community with an easily accessible 'Create Post' button, that opens the form to create a brand new post.
  
- **Post List**: The main area displays a list of posts, where users can:
  - Quickly view the post title, subreddit association, and content.
  - Interact with posts through upvote and downvote buttons, visually represented by upward and downward arrows.
  - See the post's comment count and timestamp, giving context to the activity level and recency.
  - Utilize 'Edit Post' and 'Delete Post' options for their own posts, allowing for straightforward content management.
  
- **Subreddit Navigation**: A sidebar offers quick access to various subreddits like r/FirstUsers, simplifying the exploration of different topics.


### Making Posts and Comments
* Our platform encourages active participation and content creation from our user community. By clicking on the 'Create Post' button, accessible both from the homepage and within each subreddit page, users are presented with a straightforward form. This form is the gateway to sharing new ideas, stories, or discussions.

The form fields are concise, requiring:
- **Title**: A catchy heading for the post.
- **Content**: The main body of the post where users can express their thoughts, share information, or ask questions.
- **Subreddit**: A dropdown to select which subreddit the post belongs to, making sure the content reaches the right audience.

After filling out the form, users can hit 'Submit' to instantly share their new post with the community. Alternatively, if they change their mind or need to go back, a 'Close' button is also available to exit the form without posting.

Within the detailed view of each post, a comment form is placed at the bottom of the page. This feature allows users to share their thoughts and engage directly with the content.

Here's how it works:
- **Comment Form**: Users can find a simple form to submit their comments, promoting an active dialogue related to the post.
- **Feedback Message**: Upon submitting the comment, users will immediately receive a confirmation message, acknowledging their participation.
- **Review Process**: To maintain the quality of discussions, each comment is placed in a review queue within the admin panel. Once reviewed and approved by an admin, the comment will become visible to all users under the post.


## Subreddits

Subreddits are the cornerstone of our platform, acting as dedicated spaces for specific topics or discussions. They are carefully curated and established by administrators through the admin panel, ensuring that each subreddit serves a distinct purpose and upholds community standards.

Here's what users can expect when accessing a subreddit:

- **Subreddit Header**: At the top of each subreddit page, users are greeted by the subreddit's name, prominently displayed. This serves as a clear indication of the community theme and topic.

- **Introductory Paragraph**: Beneath the header, there's a brief introductory text. This paragraph provides users with context about the subreddit, guidelines, or any welcoming messages from the moderators.

- **Posts Listing**: The main area of the subreddit page presents a list of posts that have been created under this subreddit. Users can browse through these posts, which fosters engagement and interaction within the subreddit's community.


## User Profile

Upon successful registration, each user gains access to a personal profile to showcase their individuality and contributions on the platform. The profile link, conveniently located in the navigation bar, directs users to their profile page.

Here's the composition of the User Profile page:

- **Profile Picture**: Positioned on the left side, the profile section starts with a profile picture. A default avatar is provided initially, and users have the option to personalize their profile by adding their own picture. This can be done by clicking on the edit icon, which appears above the profile information within the page.

- **Bio**: Below the profile picture, users have a space to write a bio. This personal touch allows users to introduce themselves to the community or share any details they find pertinent.

- **Posts Overview**: On the right side of the profile page, there's a dedicated area that lists all the posts made by the user. This personal log of activity not only highlights the user's contributions but also provides quick access to their content. Each post comes with 'Edit' and 'Delete' options, giving users control over their shared content.

### Admin Panel and Content Moderation

The backbone of the platform's content governance is the robust admin panel, which grants administrators comprehensive control over the site's content. This includes the ability to oversee and manage posts, comments, subreddits, and user profiles (planned for future implementation).

![Admin Panel Posts](https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/8d983e7e-5769-49b3-8ea1-d507f1466958)

Administrators can utilize powerful filters to sort posts by status or creation date and employ a search function for quick access. The creation of new content is streamlined through an 'Add Post +' button, and the ability to toggle post status from 'Draft' to 'Published' ensures only quality content is displayed.

![Admin Panel Comments](https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/ede8ea3e-a2c5-4004-99b2-ca59458fdaf3)

The 'Comments' section mirrors this functionality, allowing for meticulous moderation. User-generated comments are queued for admin review, ensuring that only appropriate content is made public, while admins can also contribute to the discourse directly.

![Admin Panel Subreddits](https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/aa993318-0204-4c7a-8d26-5960f4bb0914)

Subreddit management is an exclusive admin privilege, with capabilities to filter, edit, and curate these community spaces. This control ensures that the platform remains organized and aligned with the community's interests and guidelines.

### Future Enhancements

Looking ahead, we are committed to evolving our platform to enhance user connectivity and content management. Planned upgrades include:

- The rollout of friend requests and direct messaging to foster personal connections within the community.
- Advanced search features and sorting options to streamline content discovery.
- Sophisticated moderation tools to uphold and enforce community guidelines more effectively.

## Testing and Deployment

Key functionalities of the application underwent functional testing to ensure reliable operation. The platform has been deployed to Heroku, streamlining the deployment process for this Django application. Essential configuration for Heroku deployment was implemented, and the application is now live on Heroku's cloud platform.

The Lighthouse performance results below showcase the application's performance metrics:

![Lighthouse Performance Results](https://github.com/Sofia-Bourdon/Reddit-clone-Project/assets/112895499/596165f3-d954-465b-a537-c99986e2a532)


## Credits

### Acknowledgments
Special thanks to mentor Akshat Garg and the tutors at the Code Institute for their guidance throughout this project.

Appreciation is also extended to the communities on platforms like Stack Overflow for their assistance and shared knowledge, which were valuable in the development process.

### Sources
Useful resources and guidance were found at the following:
- [Django Central: Creating a Comments System with Django](https://djangocentral.com/creating-comments-system-with-django/)
- [Stack Overflow: Django Redirect for Non-Authenticated Users](https://stackoverflow.com/questions/21123559/django-redirect-all-non-authenticated-users-to-landing-page)
- [Django Official Documentation](https://docs.djangoproject.com/en/4.2/ref/models/fields/)
- [Django Crispy Forms Documentation](https://django-crispy-forms.readthedocs.io/en/latest/index.html)
- [Developer Handbook: Django User Profile](https://www.devhandbook.com/django/user-profile/)
- https://codinggear.blog/how-to-register-model-in-django-admin/?utm_content=cmp-true
- https://www.makeuseof.com/create-custom-404-error-page-django/
