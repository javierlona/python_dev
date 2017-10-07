# Table of Contents
* How To Run The Code
* Design Logic

# How To Run The Program
## Setup the Database
Download and unzip newsdata.sql file from [CloudFront](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Save the newsdata.sql file on your computer. Make note in which directory you saved the file.
Navigate to directory where the newsdata.sql file is saved. In the Linux command prompt enter the following commands:
```
sudo su postgres
psql
CREATE USER user1 WITH PASSWORD 'password';
ALTER USER user1 WITH SUPERUSER;
CREATE DATABASE news;
GRANT ALL on DATABASE news to user1;
\q
psql -d news -f newsdata.sql
psql -d news -U user1
```
## Create the Following Views
### Question 1 "What are the most popular three articles of all time?"
```
CREATE VIEW get_the_count AS
SELECT COUNT(path) AS views, SUBSTR(path,10) AS slug
FROM log
WHERE path LIKE '/article/%'
GROUP by path;
```
### Question 2 "Who are the most popular article authors of all time?"
```
CREATE VIEW viewed_article AS
SELECT SUBSTR(path,10) AS slug, COUNT(path) viewed
FROM log
WHERE path LIKE '/article/%'
GROUP by path
ORDER by COUNT(path) DESC;
```
### Question 3 "On which days did more than 1% of requests lead to errors?"
```
CREATE VIEW working AS
SELECT COUNT(*) as hits, DATE(time) as date
FROM log
WHERE status LIKE '200%'
GROUP by date;
```
```
CREATE VIEW nonworking AS
SELECT COUNT(*) as errors, DATE(time) as date
FROM log
WHERE status like '404%'
GROUP by date;
```
## How to Execute the Python Script
Issue the following commands in a Linux virtual machine.
Navigate to directory where **PYPostgreSQL.py** python script is saved.
Make the script executable with the following command **chmod +x PYPostgreSQL.py**.
Execute the script with the command **./PYPostgreSQL.py**

# Design Logic
## General Comments
The database was created and queried on a local Linux machine environment. Thus, the host is localhost.
## SQL Statements
The SQL queries use views. Views help filter the data which satisfies the question. The SQL statements in the Python file perform further screening to narrow the results.

## Python File
### Function main
 Main calls three functions. The Three functions are used to answer the three problems given in the assignment. The three functions have one parameter, a cursor. A cursor is created to be used throughout the database programming with Python to execute the query in each function. It contains connection information to connect to the database using credentials of user "user1".

### The Three Non Main Functions
The command cur.execute, executes a SQL statement. These functions use the routine cur.fetchall() to gather all the rows of a query result, into a list. The for loops output the data in each function.
