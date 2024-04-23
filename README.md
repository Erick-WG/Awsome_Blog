# Awsome_Blog.
This repo will be a guide in understanding python and django, by creating a basic blog app following the convention of creating web apps using the CRUD operations, for creating, reading, updating and deleting content from the database.


## Cloning the Repository.
Create a local folder to contain our project, open a terminal in the same directory we have created.
After opening a terminal window on the dir, run these command to clone the repo.

```bash
git clone https://github.com/Erick-WG/Awsome_Blog.git

```
## Understanding the files.
After successfully cloning the repository, you should see a file tree like so: 
```
Blog-env
    |---env files
    |
BlogApp
    ├───blog
    │   ├───migrations
    │   │   └───__pycache__
    │   ├───templates
    │   └───__pycache__
    ├───BlogApp
    │   └───__pycache__
    └───Members
        ├───migrations
        │   └───__pycache__
        ├───templates
        │   └───registration
        └───__pycache__
```
All the files needed to run the project successfully can be found here at a scope, we'll have a deep dive into understanding the essential files we'll be working with.

#### Important files.

_Blog-env_ : This is the virtual environment we'll be using to run our project.

_manage.py file_ : This file will help us in running most commands for starting and configuring our django application.

_BlogApp_ : This is where our project files are located, including the _manage.py_ file.

_blog_ : This folder contains all of our blogs logic to create, read, update and delete blog posts.

_Members_ : This folder contains all of our members logic to create, read, update and delete members.


_db.sqlite3_ : This is the database file that will be created when we run our project.

_requirements.txt_ : This file contains all the packages and dependencies that we need to run our project.


## Running the virtual environment.
After successfully installing the requirements, we need to run the virtual environment.

First navigate one level up to where we can have a birds eye view on our files.

From here we can then activate the virtual environment and navigate back into our BlogApp dir to work on some code for our blog web app.

To Run the virtual environment we need to run:

#### Windows:
1. Open the command prompt (cmd).
2. Navigate to the directory where your Django project is located.
3. Use the following command to activate the virtual environment:

```bash
Blog-env\Scripts\activate
```
#### MacOS and Linux:
1. Open a terminal.
2. Navigate to the directory where your Django project is located.
3. Use the following command to activate the virtual environment:

```bash
source Blog-env/bin/activate
```

## Installing the requirements.
By understanding the file system we are set to go, but hold on a bit, we need to install the required files for our environment files.

First navigate into the 'BlogApp' dir,

```bash
cd BlogApp
```

Then we need to run a command to install all our requirements inside the _'requirements.txt'_ file located in the _BlogApp_ dir.

Run this command and make sure you have installed python locally to use pip (' The python package manager ')

```bash
pip install -r requirements.txt
```

## Creating the database.
For the database we need to make sure first we are on the right directory _( BlogApp )_, then we need to make migrations to our local database, by running a command that utilizes the _manage.py_ file

## Creating the superuser.
You'll need a super user in order to manage the sites data from a user interface, creating a super user allows you to utilize the admin dashboard and you can also create, modify and delete users and blogs for the site.


Run this command to create a new superuser, follow the prompts to add the credentials you'll use to access the admin dashboard.

```bash
python manage.py createsuperuser
```

## Running the server.

Running the server is pretty easy, just run this command.
```bash
python manage.py runserver
```
You'll need to run the server every time you need to access the site.
A link will be provided for local host '8000' by default, the link will open a new browser window with the user interface of the blog app, and you'll be required to create an account before you can make posts.

```
Happy coding,
Erick-Wg
```