# FizzBuzz API

An API endpoint for “fizzbuzzes” that supports 3 operations: retrieve, list, and create.
- GET /fizzbuzz: to list all fizzbuzz objects
- GET /fizzbuzz/123: to retrieve a single fizz buzz object
- POST /fizzbuzz: to create a new fizzbuzz object

## Requirements

* Python (https://www.python.org/downloads/)

## Installation

1. Clone the repository:
```  
$ git clone https://github.com/beckybriggs/mariana_tek.git
$ cd mariana_tek
```
2. Create and activate a virtual environment: 
```  
$ python3 -m venv env
$ source env/bin/activate
```
3. Install the dependencies:
```  
(env)$ pip install -r requirements.txt
```
4. Sync the database:
```  
(env)$ python manage.py migrate
```
5. Start up Django's development server:
```  
(env)$ python manage.py runserver
```

## Usage

### API
Navigate to http://127.0.0.1:8000/fizzbuzz/ to see the browsable version of the API.

### Documentation
Navigate to http://127.0.0.1:8000/docs/ to see the API documentation.

### Tests
```  
(env)$ python manage.py test
```
