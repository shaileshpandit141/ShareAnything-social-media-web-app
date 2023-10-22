# ShareAnything Social Media Web App

### Overview

This is a social media web application developed using Django, JavaScript, HTML, CSS, and PostgreSQL. The application allows users to create profiles, post updates, follow other users, and interact with their posts. It provides a platform for social networking and sharing content with friends and followers.

### Features
* User Registration and Authentication

* User Profiles with Profile Pictures

* User can also post different type of programming
 language code and those code is highlighted in the post

* Create and Edit User Posts

* Follow/Unfollow Other Users

* News Feed to View Posts from Followed Users

* Like and Comment on Posts

* Search for Users and Posts

* Notifications for New Followers and Post Interactions


### Technologies Used
* `Django:` The back-end framework for building the application, handling user authentication, and managing the database.

* `JavaScript:` Used for front-end interactivity and asynchronous requests.

* `HTML:` For structuring web pages and rendering content.

* `CSS:` Styling the web pages and providing a responsive design.

* `PostgreSQL:` A relational database management system used to store user data, posts, and user interactions.

### Installation

1. Clone the repository to your local machine:
  
   ```shell
   git clone https://github.com/shaileshpandit141/ShareAnything-social-media-web-app.git
   ```

2. Navigate to the project directory:

    ```shell
    cd ShareAnything-social-media-web-app
    ```

3. Create a virtual environment:

    ```shell
    python -m venv env
    ```

4. Activate the virtual environment:

    * On macOS and Linux:

    ```shell
    source venv/bin/activate
    ```
    * On Windows:

    ```shell
    venv\Scripts\activate
    ```

5. Install the project dependencies:

    ```shell
    pip install -r requirements.txt
    ```

6. Set up the PostgreSQL database. Create a new database and configure the database settings in `settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

7. Make migrations:

    ```python
    python manage.py makegigrations
    ```

8. Apply database migrations:

    ```python
    python manage.py migrate
    ```

9. Create a superuser for admin access:

    ```python
    python manage.py createsuperuser
    ```

10. Start the development server:

    ```python
    python manage.py runserver
    ```

11. Access the web app at http://localhost:8000 and log in with the superuser credentials.

## Test Users

* `Username:` **testuser01** 
* `Password:` **12345678user01**

* `Username:` **testuser02** 
* `Password:` **12345678user02**

### Usage

* Register a new user account or log in with an existing account.
  
* Customize your profile by adding a profile picture and personal information.
  
* Start following other users to see their posts on your news feed.
  
* Create new posts and interact with posts by liking and commenting.
  
* Search for users and posts.
  
* Receive notifications for new followers and post interactions.

### Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

* Fork the repository.

* Create a new branch for your feature or bug fix.

* Make your changes and test thoroughly.

* Create a pull request to merge your changes into the main repository.
  

### License
This project is licensed under the `MIT License`. Feel free to use and modify it for your own purposes.

### Contact
If you have any questions or need assistance with this project, please contact `Shailesh` at `shaileshpandit141@gmail.com`.

## Thank you for using this `ShareAnything` social media web app! Enjoy connecting with others and sharing your content.




