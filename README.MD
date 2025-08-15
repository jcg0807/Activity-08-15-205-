_Na expire license ng Pycharm sa school, di tuloy na push on time    ):_

# OBJOR Activity

# Django Twitter Website

This is a simple Django application that allows users to register, post tweets with optional images, and view a feed of tweets.

## Features

- User register, login and logout.
- Create tweets with text and optional image uploads.
- View a list of all tweets.
- User registration with username filtering (prohibits "shit", "fuck", "bobo").

## Setup Instructions

Follow these steps to get the project up and running on your local machine.

### Clone the Repository

```bash
git clone https://github.com/jcg0807/Activity-08-15-205-.git
cd Activity-08-15-205-
```

### install Pillow
```bash
python -m pip install Pillow
```

### Run the Server
```bash
py manage.py runserver
```

## How to Use

Register an Account
Navigate to http://127.0.0.1:8000/register/.
Fill out the registration form.

Login
If you registered, you'll be automatically logged in.

Create a Tweet
Once logged in, click on the "Create New Tweet" link or navigate to http://127.0.0.1:8000/tweet/create/.
Enter your text.
or, upload an image.
Click "Tweet" to post.

View Tweets
The home page (http://127.0.0.1:8000/) displays all tweets even when logged out.
