# FitLife Project README

Welcome to FitLife, a web application designed to help users achieve their fitness goals by tracking activities, providing healthy lifestyle tips, and offering customized plans. This project is built using Django and integrates with MongoDB for efficient data management

# Features

1- Home Page: An overview of FitLife's membership plans, quick links to other pages, nutrition tips, and testimonials.

2- Classes: Access to the gym’s available fitness group classes with their time and location and the ability to add classes to the user’s classes for logged in users where they will be notified via email 6 hours before the class start time.

3- Fitness workouts suggestion: Access to a variety of fitness workouts videos with filter functionality where the user can view all workouts categories or select a preferred one.

4- Community: A place where members can share their thoughts, fitness tips, and progress with others. Posts can be filtered by category (e.g., fitness, general, nutrition, or other posts), liked, and commented on. Additionally, users have the option to sort posts by date added or alphabetically (A-Z or Z-A). They can also edit or remove their own posts.

5- Measurement tracking: a page where users can add their body measurement and refer to them anytime. Each record will include the body measurements added by the user in addition to the date and the Body Mass Index (BMI), (which will be automatically calculated based on the data inserted). They can edit or delete their measurements as well.

6- Secure profile management, login, and registration that lets users access their recorded data after each login.

# Prerequisites

## ensure you have the following installed:

- Anaconda (for managing virtual environments).
- Python 3.12
- MongoDB (for database management).

### Steps to set up and run FitLife:

1- Clone the repository
-from your terminal using the command 
git clone https://github.com/Maryam308/FitLife.git
click the green code button and select download ZIP

2- Create a database for the project called FitLife
in mongo db compass: connect to your local connection then click create database and enter FitLife as the database name and any collection name in the collection name field

3- Create a Virtual Environment using Anaconda
conda create --name FitLifeEnv django

4- Activate the Virtual Environment
conda activate FitLifeEnv

5- Install Dependencies
pip install -r requirements.txt

6- create necessary migrations and apply them
python manage.py makemigrations
python manage.py migrate

7- Populate the Database with Sample Data
2 ways to do this: - using mongodb compass: navigate to the workouts collection, click add data -> import JSON or csv file then choose "workouts.json" which is located in FitLife-Project/JSON Data - using the CLI: mongoimport --db FitLife --collection [collection name] --file "[JSON file path]"

For classes_fitnessclass collection:
mongoimport --db FitLife --collection classes_fitnessclass --file "[json file path]"

For workouts_workout collection:
mongoimport --db FitLife --collection workouts_workout --file "[json file path]"


8- Create an Admin User
python manage.py createsuperuser
then follow the prompts

    example (you can use these or any other values if you wish):
    username: admin
    email: admin@gmail.com
    password: Abyz_0908
    password confirmation: Abyz_0908

9- Start the Development Server
python manage.py runserver

##### Additional Notes

# Using the Admin Panel

The admin panel is accessible at http://127.0.0.1:8000/admin using the superuser credentials created in step 8.

## Managing Dependencies

If additional dependencies are installed during development, ensure to update the requirements.txt file using this command
pip freeze > requirements.txt

# If port 8000 is occupied, specify an alternative port when running the server:

    e.g:
    python manage.py runserver 8080


