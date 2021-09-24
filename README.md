# data-pipeline-miniproject

### Mini-project for mySQL data pipeline for a ticket sales system.

### Setup
1. Install and configure mySQL per instructions found here https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/
2. Either use your root user or create a new user with sufficient privileges to read and write to the database, as well as create and delete database and tables.

### DDL
Included is a .sql file for the ticket system database DDL. Follow instructions below.
1. Make note of the full path of the DDL file.
2. From a terminal or the command line enter the mySQL shell using $mysql
3. Run the following to establish teh database and schema. mysql> source /Users/[your path]/data-pipeline-miniproject/salesDDL.sql 
4. Confirm that the database was created and tables setup correctly using mysql> USE TicketSystem; mysql> SHOW TABLES; mysql> DESCRIBE sales;

### Running Pipeline
The pipeline code is in data_loader.py. In the same directory should be the preliminary data file. Leave these files in place.
1. From terminal or command line $ python data_loader.py
2. It will prompt for your user name and a password. This will be the credentials you established when installing and setting up mySQL.
