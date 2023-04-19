# Project Management Website

This repo contains the backend for our project ticket and employee management website. It contains:
- The SQL file containing the tables and data in the database
- Blueprints containing routes for the employees and projects data
- Thunder Client tests for each of the routes

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
2. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
3. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
4. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
5. Build the images with `docker compose build`
6. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

## How to use Thunder Client tests

1. Using VSCode, install the thunder client extension
2. Open Thunder Client by clicking on the icon in the toolbar
3. Access the collection you want to test (either employees or projects)
4. Select the test for the route you want to test

## How to start the Appsmith website

1. Start the containers using `docker compose up` (follow setup instructions above)
2. Open your browser of choice and navigate to localhost:8080
3. Click on the three dots next to the "New" button and select import and import from Git repository
4. Enter the SSH URL for the front end repository

## Link to Demonstration Video
https://youtu.be/-qTAQBy5w8I



