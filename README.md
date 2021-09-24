# data-pipeline-miniproject

### Mini-project for mySQL data pipeline for a ticket sales system.

### Setup
1. Install and configure mySQL per instructions found here https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/
2. Either use your root user or create a new user with sufficient privileges to read and write to the database, as well as create and delete database and tables.

### DDL
Included is a .sql file for the ticket system database DDL. Follow instructions below.
1. Make note of the full path of the DDL file.
2. From a terminal or the command line enter the mySQL shell using $mysql
3. Run the following to establish the database and schema.

        mysql> source /Users/[your path]/data-pipeline-miniproject/salesDDL.sql 
4. Confirm that the database was created and tables setup correctly using 

        mysql> USE TicketSystem; 
        
        mysql> SHOW TABLES; 
        +------------------------+
        | Tables_in_ticketsystem |
        +------------------------+
        | sales                  |
        +------------------------+
        1 row in set (0.00 sec)
        
        mysql> DESCRIBE sales;
        +-------------+---------------+------+-----+---------+-------+
        | Field       | Type          | Null | Key | Default | Extra |
        +-------------+---------------+------+-----+---------+-------+
        | ticket_id   | int           | NO   | PRI | NULL    |       |
        | trans_date  | int           | NO   |     | NULL    |       |
        | event_id    | int           | NO   |     | NULL    |       |
        | event_name  | varchar(50)   | NO   |     | NULL    |       |
        | event_date  | date          | NO   |     | NULL    |       |
        | event_type  | varchar(10)   | NO   |     | NULL    |       |
        | event_city  | varchar(20)   | NO   |     | NULL    |       |
        | customer_id | int           | NO   |     | NULL    |       |
        | price       | decimal(10,0) | NO   |     | NULL    |       |
        | num_tickets | int           | NO   |     | NULL    |       |
        +-------------+---------------+------+-----+---------+-------+
        10 rows in set (0.01 sec)

### Running Pipeline
The pipeline code is in data_loader.py. In the same directory should be the preliminary data file. Leave these files in place.
1. From terminal or command line 

        $ python data_loader.py
3. It will prompt for your user name and a password. This will be the credentials you established when installing and setting up mySQL. This will run the loader and return the query for the top 3 events by their total sales.

        Enter user: [your user]
        Password: [your password]
        Here are the top 3 events by ticket sales for the month:
        - 5 tickets sold for  Washington Spirits vs Sky Blue FC
        - 5 tickets sold for  Christmas Spectacular
        - 4 tickets sold for  The North American International Auto Show
