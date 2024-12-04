
# KitchenMastery:
## E-commernce webiste that sells cooking supplies and offers some cooking recipes and tips that website visitor my be interested in. The Project is a web application that was created using Django and Bootstrap frameworks and MongoDB as the backend database.

### Steps to run the entire web application:

1- In Anaconda Prompt, Navigate to the project's directory.

2- Create the virtual environment with conda.
```
conda create --name kitchenEnv django
```
3- Activate the environment.
```
conda activate kitchenEnv
```
4- Install project dependecies from a text file.
```
pip install -r requirements.txt
```
5- Connect Django project with MongoDB.
```
python manage.py makemigrations
```
```
python manage.py migrate
```
6- Populate Database wtih sample data.
```
python manage.py shell < setup.py
```
7- create super user
```
python manage.py createsuperuser
```
8- Run the server
```
python manage.py runserver
```
