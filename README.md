# awwwards

> [default-007](https://github.com/default-007)

# Description

This project allows users to post their projects for other users to rate according to design, usability and content

## Live Link

Click [View Site](https://awwwards-007.herokuapp.com/) to visit the site

## Behavior Driven Development

| Input                                         | Behaviour                                                                                | Output                                                                                                                                 |
| --------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| User registers for an account by filling form | Page redirects user to login page                                                        | User is redirected tpo login page                                                                                                      |
| User logs in                                  | User is taken to the home page                                                           | Redirect you to the homepage where the user is greeted with a feed of most recent photos posted                                        |
| User clicks upload button and fills the form  | The page reloads                                                                         | User's new post is displayed on the feed                                                                                               |
| User clicks on the like button                | The page reloads                                                                         | Like count of the post is increased by one value                                                                                       |
| User clicks on the comment button             | User is redirected to a page containing the single post, its comments and a comment form | A page displaring the single post is displayed                                                                                         |
| User posts a comment by filling the form      | The page reloads                                                                         | The new comment is added onto the post's comment section , showing th comment and its author, and comment count is updated in the feed |

## Screenshots

###### Home page

<img src="https://raw.githubusercontent.com/default-007/awwwards/master/static/images/profile.png">
 
 ###### Rating of a post
<img src="https://raw.githubusercontent.com/default-007/awwwards/master/static/images/profile.png">

## User Story

- A user can view posted projects and their details.
- A user can post a project to be rated/reviewed.
- A user can rate/ review other users' projects.
- Search for projects.
- View projects overall score.
- A user can view their profile page.

## Setup and Installation

To get the project .......

##### Cloning the repository:

```bash
https://github.com/default-007/awwwards.git
```

##### Navigate into the folder and install requirements

```bash
cd project-awwards pip install -r requirements.txt
```

##### Install and activate Virtual

```bash
- python3 -m venv virtual - source virtual/bin/activate
```

##### Install Dependencies

```bash
pip install -r requirements.txt
```

##### Setup Database

SetUp your database User,Password, Host then make migrate

```bash
python manage.py makemigrations instagram
```

Now Migrate

```bash
python manage.py migrate
```

##### Run the application

```bash
python manage.py runserver
```

##### Testing the application

```bash
python manage.py test
```

Open the application on your browser `127.0.0.1:8000`.

### Api Endpoints

- https://chawwards.herokuapp.com/api/users/
- https://chawwards.herokuapp.com/api/profile/
- https://chawwards.herokuapp.com/api/posts/

## Technology used

- [Python3.6](https://www.python.org/)
- [Django 2.2](https://docs.djangoproject.com/en/2.2/)
- [Heroku](https://heroku.com)

## Known Bugs

- There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information

If you have any question or contributions, please email me at [brianokola@gmail.com]

## License

- [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/default-007/awwwards/blob/master/LICENSE)
- Copyright (c) 2019 **Brian Otieno**
