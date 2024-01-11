# Gamers Nest

## Gamers Nest API Goals

1. **User Interaction:** Enable sharing and engagement among gamers.
2. **Community Building:** Foster connections and friendships in the gaming community.
3. **Content Discovery:** Facilitate game recommendations and tips.
4. **User-Friendly Interface:** Ensure an intuitive and seamless user experience.
5. **Data Models:** Implement structured models for posts, profiles, comments, likes, and bookmarks.
6. **Security:** Prioritize secure user authentication and authorization.
7. **Third-Party Integrations:** Integrate services like Cloudinary for efficient media management.
8. **Documentation:** Provide clear and comprehensive developer documentation.
9. **Deployment:** Streamline deployment for accessibility on platforms like Heroku.

In summary, the API aims to create a vibrant platform for gamers to connect, share, and explore the gaming world together.
Here is a link to the React [Gamers Nest](https://gamers-nest-27823b8a37a8.herokuapp.com/) app.

## Admin Credentials

SuperUsers:

1. - Username: george
   - Password: password

2. - Username: username
   - Password: password

3. - Username: username2
   - Password: password2




## Table of contents

1. [Gamers Nest](#gamers-nest)
    1. [Gamers Nest API Goals](#gamers-nest-api-goals)
    2. [Table of contents](#table-of-contents)
    3. [Planning](#planning)
        1. [Data models](#data-models)
    4. [API endpoints](#api-endpoints)
    5. [Frameworks, libraries, and dependencies](#frameworks-libraries-and-dependencies)
    6. [Testing](#testing)
        1. [Manual testing](#manual-testing)
        2. [Automated tests](#automated-tests)
        3. [Python validation](#python-validation)
    7. [Deployment](#deployment)
    8. [Credits](#credits)

## Planning

### Data models
Data model schema were planned in parallel with the API endpoints, using an entity relationship diagram.

Custom models implemented for Tribehub are:

### Bookmark
Represents the post bookmark and user bookmarks, using a many-to-one relationship to both Post and User.
Each user can bookmark any post they want as long as they are logged in.

### Comment_likes
Represents the likes of the comments, using a many-to-one relationship to both Comment and User.
Each user can like any comment they want as long as they are logged in.

## API endpoints

| Endpoint                | URL                     | HTTP Method | Description                        |
|-------------------------|-------------------------|-------------|------------------------------------|
| Profile List            | `/profiles/`            | `GET`       | Get a list of profiles             |
| Profile Creation        | `/profiles/`            | `POST`      | Create a new profile               |
| Profile Detail          | `/profiles/<int:pk>/`   | `GET`       | Get details of a specific profile  |
| Profile Update          | `/profiles/<int:pk>/`   | `PUT`       | Update details of a profile        |
| Profile Deletion        | `/profiles/<int:pk>/`   | `DELETE`    | Delete a specific profile          |
| Post List               | `/posts/`               | `GET`       | Get a list of posts                |
| Post Creation           | `/posts/`               | `POST`      | Create a new post                  |
| Post Detail             | `/posts/<int:pk>/`      | `GET`       | Get details of a specific post     |
| Post Update             | `/posts/<int:pk>/`      | `PUT`       | Update details of a post           |
| Post Deletion           | `/posts/<int:pk>/`      | `DELETE`    | Delete a specific post             |
| Comment List            | `/comments/`            | `GET`       | Get a list of comments             |
| Comment Creation        | `/comments/`            | `POST`      | Create a new comment               |
| Comment Detail          | `/comments/<int:pk>/`   | `GET`       | Get details of a specific comment  |
| Comment Update          | `/comments/<int:pk>/`   | `PUT`       | Update details of a comment        |
| Comment Deletion        | `/comments/<int:pk>/`   | `DELETE`    | Delete a specific comment          |
| Like List               | `/likes/`               | `GET`       | Get a list of likes                |
| Like Creation           | `/likes/`               | `POST`      | Create a new like                  |
| Like Detail             | `/likes/<int:pk>/`      | `GET`       | Get details of a specific like     |
| Like Update             | `/likes/<int:pk>/`      | `PUT`       | Update details of a like           |
| Like Deletion           | `/likes/<int:pk>/`      | `DELETE`    | Delete a specific like             |
| Bookmark List          | `/bookmarks/`           | `GET`       | Get a list of bookmarks            |
| Bookmark Creation      | `/bookmarks/`           | `POST`      | Create a new bookmark              |
| Bookmark Detail        | `/bookmarks/<int:pk>/`  | `GET`       | Get details of a specific bookmark|
| Bookmark Update        | `/bookmarks/<int:pk>/`  | `PUT`       | Update details of a bookmark       |
| Bookmark Deletion      | `/bookmarks/<int:pk>/`  | `DELETE`    | Delete a specific bookmark         |
| Comment Like List      | `/comment_likes/`       | `GET`       | Get a list of comment likes        |
| Comment Like Creation  | `/comment_likes/`       | `POST`      | Create a new comment like          |
| Comment Like Detail    | `/comment_likes/<int:pk>/`| `GET`      | Get details of a specific comment like|
| Comment Like Update    | `/comment_likes/<int:pk>/`| `PUT`      | Update details of a comment like   |
| Comment Like Deletion  | `/comment_likes/<int:pk>/`| `DELETE`   | Delete a specific comment like     |

## Frameworks, libraries and dependencies
The Gamers Nest API is implemented in Python using [Django](https://www.djangoproject.com) and [Django Rest Framework](https://django-filter.readthedocs.io/en/stable/).
The following additional utilities, apps and modules were also used:

1. **django.contrib.staticfiles**
   - **Presentation:** Part of Django's core modules, `django.contrib.staticfiles` is responsible for handling static files (CSS, JavaScript, images) in your Django project. It simplifies the process of serving and managing static content.
   - **Link:** [Django Static Files Documentation](https://docs.djangoproject.com/en/3.2/howto/static-files/)

2. **cloudinary**
   - **Presentation:** `cloudinary` is a cloud-based image and video management service. It provides a platform-independent solution for storing, processing, and delivering media assets efficiently.
   - **Link:** [Cloudinary Website](https://cloudinary.com/)

3. **rest_framework**
   - **Presentation:** Django REST framework is a powerful and flexible toolkit for building Web APIs. It provides serializers, authentication, and view classes to simplify the process of developing robust RESTful APIs.
   - **Link:** [Django REST Framework Website](https://www.django-rest-framework.org/)

4. **django_filters**
   - **Presentation:** `django_filters` is a Django application for filtering querysets dynamically. It allows you to easily create complex query filters for your Django models, enhancing the flexibility of data retrieval.
   - **Link:** [django-filter](https://django-filter.readthedocs.io/en/stable/)

5. **rest_framework.authtoken**
   - **Presentation:** This module provides token-based authentication for Django REST Framework. It allows clients to authenticate using a token in the `Authorization` header.
   - **Link:** [DRF Token Authentication Documentation](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

6. **dj_rest_auth**
   - **Presentation:** `dj_rest_auth` is an extension of Django REST framework that provides a set of RESTful API endpoints for handling user authentication. It includes features like login, registration, and password reset.
   - **Link:** [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/introduction.html)

7. **django.contrib.sites**
   - **Presentation:** `django.contrib.sites` is a Django application for managing multiple sites within a single Django project. It's often used in conjunction with other Django applications for multi-site setups.
   - **Link:** [Django Sites Documentation](https://docs.djangoproject.com/en/3.2/ref/contrib/sites/)

8. **allauth**
   - **Presentation:** `allauth` is a Django application that provides a set of flexible authentication, registration, and account management functionalities. It's highly customizable and works seamlessly with Django projects.
   - **Link:** [django-allauth](https://django-allauth.readthedocs.io/en/latest/)

9. **corsheaders**
    - **Presentation:** `corsheaders` is a Django application for handling Cross-Origin Resource Sharing (CORS). It enables your Django server to handle requests from different origins.
    - **Link:** [django-cors-headers](https://pypi.org/project/django-cors-headers/)

## Testing

### Manual testing

Manual testing of the Gamers Nest API ensures that the endpoints are functioning correctly and handling requests as expected. Follow the steps below to perform manual testing of key API features.

#### 1. Retrieve User Profiles
- **Endpoint:** `GET /profiles/`
- **Description:** Retrieve a list of user profiles.
- **Testing Steps:**
  1. Make a GET request to the `/profiles/` endpoint.
  2. Verify that the response contains a list of user profiles with relevant information.

#### 2. Retrieve a Specific User Profile
- **Endpoint:** `GET /profiles/<user_id>/`
- **Description:** Retrieve details of a specific user profile.
- **Testing Steps:**
  1. Replace `<user_id>` with the ID of a valid user.
  2. Make a GET request to the `/profiles/<user_id>/` endpoint.
  3. Verify that the response contains the profile information for the specified user.

#### 3. Create a Post
- **Endpoint:** `POST /posts/`
- **Description:** Create a new post.
- **Testing Steps:**
  1. Make a POST request to the `/posts/` endpoint with the required data (e.g., title, content, image).
  2. Verify that the response indicates successful post creation.
  3. Check the list of posts to confirm the new post is added.

#### 4. Delete a Post
- **Endpoint:** `DELETE /posts/<post_id>/`
- **Description:** Delete a specific post.
- **Testing Steps:**
  1. Replace `<post_id>` with the ID of a post that you have created.
  2. Make a DELETE request to the `/posts/<post_id>/` endpoint.
  3. Verify that the response indicates successful post deletion.
  4. Check the list of posts to confirm the post is removed.

#### 5. Retrieve a Post
- **Endpoint:** `GET /posts/<post_id>/`
- **Description:** Retrieve details of a specific post.
- **Testing Steps:**
  1. Replace `<post_id>` with the ID of a valid post.
  2. Make a GET request to the `/posts/<post_id>/` endpoint.
  3. Verify that the response contains the post details for the specified post.

#### 6. Like a Post
- **Endpoint:** `POST /likes/`
- **Description:** Like a specific post.
- **Testing Steps:**
  1. Make a POST request to the `/likes/` endpoint with the post ID.
  2. Verify that the response indicates successful post liking.
  3. Check the post details to confirm the like is recorded.

#### 7. Unlike a Post
- **Endpoint:** `DELETE /likes/<like_id>/`
- **Description:** Unlike a specific post.
- **Testing Steps:**
  1. Replace `<like_id>` with the ID of a like that you have created.
  2. Make a DELETE request to the `/likes/<like_id>/` endpoint.
  3. Verify that the response indicates successful post unliking.

#### 8. Retrieve Post Likes
- **Endpoint:** `GET /likes/`
- **Description:** Retrieve a list of likes for a specific post.
- **Testing Steps:**
  1. Make a GET request to the `/likes/` endpoint with the post ID.
  2. Verify that the response contains a list of likes for the specified post.

#### 9. Bookmark a Post
- **Endpoint:** `POST /bookmarks/`
- **Description:** Bookmark a specific post.
- **Testing Steps:**
  1. Make a POST request to the `/bookmarks/` endpoint with the post ID.
  2. Verify that the response indicates successful post bookmarking.
  3. Check the list of bookmarks to confirm the post is bookmarked.

#### 10. Unbookmark a Post
- **Endpoint:** `DELETE /bookmarks/<bookmark_id>/`
- **Description:** Unbookmark a specific post.
- **Testing Steps:**
  1. Replace `<bookmark_id>` with the ID of a bookmark that you have created.
  2. Make a DELETE request to the `/bookmarks/<bookmark_id>/` endpoint.
  3. Verify that the response indicates successful post unbookmarking.

#### 11. Retrieve User's Bookmarked Posts
- **Endpoint:** `GET /bookmarks/`
- **Description:** Retrieve a list of posts bookmarked by the authenticated user.
- **Testing Steps:**
  1. Make a GET request to the `/bookmarks/` endpoint.
  2. Verify that the response contains a list of bookmarked posts for the authenticated user.

#### 12. Comment on a Post
- **Endpoint:** `POST /comments/`
- **Description:** Add a comment to a specific post.
- **Testing Steps:**
  1. Make a POST request to the `/comments/` endpoint with the post ID and comment text.
  2. Verify that the response indicates successful comment creation.
  3. Check the post details to confirm the comment is added.

#### 13. Delete a Comment
- **Endpoint:** `DELETE /comments/<comment_id>/`
- **Description:** Delete a specific comment.
- **Testing Steps:**
  1. Replace `<comment_id>` with the ID of a comment that you have created.
  2. Make a DELETE request to the `/comments/<comment_id>/` endpoint.
  3. Verify that the response indicates successful comment deletion.

#### 14. Retrieve Comments on a Post
- **Endpoint:** `GET /comments/`
- **Description:** Retrieve a list of comments on a specific post.
- **Testing Steps:**
  1. Make a GET request to the `/comments/` endpoint with the post ID.
  2. Verify that the response contains a list of comments for the specified post.

#### 15. Like a Comment
- **Endpoint:** `POST /comment_likes/`
- **Description:** Like a specific comment.
- **Testing Steps:**
  1. Make a POST request to the `/comment_likes/` endpoint with the comment ID.
  2. Verify that the response indicates successful comment liking.
  3. Check the comment details to confirm the like is recorded.

#### 16. Unlike a Comment
- **Endpoint:** `DELETE /comment_likes/<comment_like_id>/`
- **Description:** Unlike a specific comment.
- **Testing Steps:**
  1. Replace `<comment_like_id>` with the ID of a comment like that you have created.
  2. Make a DELETE request to the `/comment_likes/<comment_like_id>/` endpoint.
  3. Verify that the response indicates successful comment unliking.

#### 17. Retrieve User's Liked Comments
- **Endpoint:** `GET /comment_likes/`
- **Description:** Retrieve a list of comments liked by the authenticated user.
- **Testing Steps:**
  1. Make a GET request to the `/comment_likes/` endpoint.
  2. Verify that the response contains a list of liked comments for the authenticated user.

### Automated tests

Seven unit tests were written for the `posts` endpoint. These are in `posts/tests.py`, and all passed:
- test_can_list_posts
- test_logged_in_user_can_create_post
- test_user_not_logged_in_cant_create_post
- test_can_retrieve_post_using_valid_id
- test_cant_retrieve_post_using_invalid_id
- test_user_can_update_own_post
- test_user_cant_update_another_users_post

### Python validation

All files containing custom Python code were then validated using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/):
- `bookmarks/models.py` no errors found
- `bookmarks/serializers.py` no errors found
- `bookmarks/urls.py` no errors found
- `bookmarks/views.py` no errors found

- `comment_likes/models.py` no errors found
- `comment_likes/serializers.py` no errors found
- `comment_likes/urls.py` no errors found
- `comment_likes/views.py` no errors found

## Deployment
The TribeHub API is deployed to Heroku, using an ElephantSQL Postgres database.
To duplicate deployment to Heroku, follow these steps:

- Fork or clone this repository in GitHub.
- You will need a Cloudinary account to host user profile images.
- Login to Cloudinary.
- Select the 'dashboard' option.
- Copy the value of the 'API Environment variable' from the part starting `cloudinary://` to the end. You may need to select the eye icon to view the full environment variable. Paste this value somewhere for safe keeping as you will need it shortly (but destroy after deployment).
- Log in to Heroku.
- Select 'Create new app' from the 'New' menu at the top right.
- Enter a name for the app and select the appropriate region.
- Select 'Create app'.
- Select 'Settings' from the menu at the top.
- Login to ElephantSQL.
- Click 'Create new instance' on the dashboard.
- Name the 'plan' and select the 'Tiny Turtle (free)' plan.
- Select 'select region'.
- Choose the nearest data centre to your location.
- Click 'Review'.
- Go to the ElephantSQL dashboard and click on the 'database instance name' for this project.
- Copy the ElephantSQL database URL to your clipboard (this starts with `postgres://`).
- Return to the Heroku dashboard.
- Select the 'settings' tab.
- Locate the 'reveal config vars' link and select.
- Enter the following config var names and values:
    - `CLOUDINARY_URL`: *your cloudinary URL as obtained above*
    - `DATABASE_URL`: *your ElephantSQL postgres database URL as obtained above*
    - `SECRET_KEY`: *your secret key*
    - `ALLOWED_HOST`: *the url of your Heroku app (but without the `https://` prefix)*
- Select the 'Deploy' tab at the top.
- Select 'GitHub' from the deployment options and confirm you wish to deploy using GitHub. You may be asked to enter your GitHub password.
- Find the 'Connect to GitHub' section and use the search box to locate your repo.
- Select 'Connect' when found.
- Optionally choose the main branch under 'Automatic Deploys' and select 'Enable Automatic Deploys' if you wish your deployed API to be automatically redeployed every time you push changes to GitHub.
- Find the 'Manual Deploy' section, choose 'main' as the branch to deploy and select 'Deploy Branch'.
- Your API will shortly be deployed and you will be given a link to the deployed site when the process is complete.

## Credits

This API is basically taken from [CodeInstitute Django Rest Framework](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/f775d54df4da44d18309888b3fe884f7/bc5fbada70104d489aa0363a03d8bda8/) With some custom models added to it.