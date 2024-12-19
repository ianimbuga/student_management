# Student Management System

By **IAN LIDAVALIA***

A Python-based CLI application that manages student and course data using SQLAlchemy for database management and Alembic for migrations.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)
- [Database Migrations](#database-migrations)
- [Dependencies](#dependencies)

## Features
- **Add**: Create new student and course entries.
- **Update**: Modify existing student and course details.
- **Delete**: Remove students and courses from the database.
- **List**: Display all students and courses.
- **Validation**: Ensure input data meets specified criteria.

## Technologies
- **Python**: The programming language used for development.
- **SQLAlchemy**: For ORM and database management.
- **Alembic**: For database migrations.
- **Python-dotenv**: For loading environment variables.

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system

2.Install dependencies using Pipenv

```bash
Copy code
pipenv install

3.Create a .env file Add the following line to specify your database URL:
DATABASE_URL=sqlite:///your_database.db

4.Run database migrations To set up the database schema, run:
```bash
Copy code
alembic upgrade head

# Usage
To run the CLI application:

```bash
Copy code
pipenv run python cli.py
# Follow the on-screen prompts to manage students and courses.

Database Migrations
Alembic is used for handling database migrations. To create a new migration after making changes to your models, run:

```bash
Copy code
alembic revision --autogenerate -m "Your message"

# Then apply the migrations with:

```bash
Copy code
alembic upgrade head

# Dependencies
*SQLAlchemy: ORM for database interactions.
*Alembic: Migration tool for SQLAlchemy.
*Python-dotenv: Loads environment variables from a .env file.

# Future Enhancements
1.User Authentication:
Implement user login and registration features to secure access to the system.

2.Advanced Reporting:
Add features to generate reports on student performance, course statistics, and enrollment trends.

3.Email Notifications:
Implement an email notification system to inform students of important updates, deadlines, or announcements.

4.Integration with External APIs:
Integrate with educational APIs to provide additional resources or functionality, such as course materials or online assessments.

# LISENCE
This project is licensed under the MIT License 

# Contributing
Contributions are welcome! Please create a pull request for any improvements or bug fixes.




