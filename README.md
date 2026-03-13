📌 Project Overview

This project is a simple Python-based CRUD (Create, Read, Update, Delete) application that interacts with a MySQL database. It allows users to manage records in a user table by inserting, displaying, updating, and deleting user data through Python scripts.

The project demonstrates how Python can connect to a MySQL database and perform basic database operations.

🧰 Technologies Used

Python

MySQL

mysql-connector-python

📂 Project Files
1️⃣ Database Connection

File: connection.py

This file creates a connection between Python and the MySQL database using the mysql.connector library. It returns a database connection object that is used in all other scripts.

2️⃣ Insert Data

File: insert.py

This script allows the user to insert a new record into the user table by entering:

Username

Email

Password

The data is inserted into the database using an SQL INSERT query.

3️⃣ Show Data

File: showdata.py

This script retrieves all records from the user table using a SELECT query and prints them in the console.

4️⃣ Update Data

File: update.py

This script updates existing user information based on the entered ID.
It allows modification of:

Username

Email

Password

The update is performed using an UPDATE SQL query.

5️⃣ Delete Data

File: delete.py

This script deletes a user record by entering the ID of the user to be removed from the database.

🗄 Database Structure
Database Name
userdata
Table Name
user
Table Fields
Field	Type
id	INT (Primary Key, Auto Increment)
username	VARCHAR
email	VARCHAR
password	VARCHAR

Example SQL:

CREATE DATABASE userdata;

USE userdata;

CREATE TABLE user(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(100),
email VARCHAR(100),
password VARCHAR(100)
);
⚙ Installation
1️⃣ Install MySQL Connector
pip install mysql-connector-python
2️⃣ Configure Database

Update the credentials inside connection.py if needed.

host="localhost"
user="root"
password=""
database="userdata"
▶ How to Run

Run each script individually:

Insert Data
python insert.py
Show Data
python showdata.py
Update Data
python update.py
Delete Data
python delete.py
🚀 Features

Connect Python to MySQL

Insert new records

Display all records

Update user data

Delete user records

Simple command-line interface

🎯 Learning Outcomes

This project helps in understanding:

Python database connectivity

SQL CRUD operations

Using mysql.connector

Managing database records through Python scripts
