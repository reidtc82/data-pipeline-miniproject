DROP DATABASE IF EXISTS TicketSystem;
CREATE DATABASE IF NOT EXISTS TicketSystem;
USE TicketSystem;
CREATE TABLE IF NOT EXISTS sales (
    ticket_id INT NOT NULL,
    trans_date DATE NOT NULL,
    event_id INT NOT NULL,
    event_name VARCHAR(50) NOT NULL,
    event_date DATE NOT NULL,
    event_type VARCHAR(10) NOT NULL,
    event_city VARCHAR(20) NOT NULL,
    customer_id INT NOT NULL,
    price DECIMAL NOT NULL,
    num_tickets INT NOT NULL,
    PRIMARY KEY (ticket_id));

