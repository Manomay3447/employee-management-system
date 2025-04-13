# Employee Management System 

A simple Employee Management System built using **Django** and **MySQL**, containerized with **Docker**. This project helped me explore full-stack application development and deployment using Docker, and gain deeper insights into Django's ORM and app structure.

## Features

- Add, update, and delete employee records
- Relational database support with MySQL
- Django Admin interface for quick data handling
- Dockerized for easy setup and portability

## Technologies Used

- Python 3.10.12
- Django 5.0.6
- MySQL 8.0.41
- Docker + Docker Compose
- Gunicorn (for production-ready WSGI server)

## Setup Instructions

1. Clone the repository
    - git clone git@github.com:Manomay3447/employee-management-system.git
    - cd employee-management-system

2. Start the containers
    - docker-compose up --build
      App will be available at http://localhost:8000
      
3. Access MySQL
    -The MySQL server runs at port 3307.
     Use the following credentials:
      User: myuser1
      Password: 3447
      Database: EMS1

4. Apply Migrations
    - docker-compose exec web python manage.py migrate
  
5. Testing
  You can run the Django development server separately for testing:
    - docker-compose exec web python manage.py runserver 0.0.0.0:8000
