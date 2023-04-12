CREATE DATABASE IF NOT EXISTS proprojectsdb;

USE `proprojectsdb`;

grant all privileges on proprojectsdb.* to 'webapp'@'%';
flush privileges;

DROP TABLE IF EXISTS `Companies`;

CREATE TABLE Companies
(
    company_id   int PRIMARY KEY,
    company_name varchar(50) NOT NULL,
    country      varchar(50),
    city         varchar(50),
    state        varchar(50),
    zip_code     int
);

DROP TABLE IF EXISTS `Clients`;

CREATE TABLE Clients
(
    client_id      int PRIMARY KEY,
    first_name     varchar(50) NOT NULL,
    last_name      varchar(50) NOT NULL,
    country        varchar(50),
    city           varchar(50),
    state          varchar(50),
    zip_code       int,
    age            int,
    gender         varchar(50),
    date_of_birth  DATE,
    company_id     int         NOT NULL,
    CONSTRAINT fk_1 FOREIGN KEY (company_id) REFERENCES Companies (company_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `Client_Email_Addresses`;

CREATE TABLE Client_Email_Addresses
(
    client_id     int,
    email_address varchar(50),
    PRIMARY KEY (client_id, email_address),
    CONSTRAINT fk_2 FOREIGN KEY (client_id) REFERENCES Clients (client_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `Projects`;

CREATE TABLE Projects
(
    project_id int PRIMARY KEY,
    client_id  int         NOT NULL,
    lead_id    int         NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name  varchar(50) NOT NULL,
    CONSTRAINT fk_3 FOREIGN KEY (client_id) REFERENCES Clients (client_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `Departments`;

CREATE TABLE Departments
(
    department_id       int PRIMARY KEY,
    department_name     varchar(50) NOT NULL,
    department_location varchar(50) NOT NULL
);

DROP TABLE IF EXISTS `Teams`;

CREATE TABLE Teams
(
    team_id       int PRIMARY KEY,
    team_name     varchar(50) NOT NULL,
    meeting_time  time        NOT NULL,
    department_id int         NOT NULL,
    CONSTRAINT fk_6 FOREIGN KEY (department_id) REFERENCES Departments (department_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `Team_projects`;

CREATE TABLE Team_projects
(
    project_id int,
    team_id    int,
    PRIMARY KEY (project_id, team_id),
    CONSTRAINT fk_4 FOREIGN KEY (project_id) REFERENCES Projects (project_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_5 FOREIGN KEY (team_id) REFERENCES Teams (team_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `TicketTypes`;

CREATE TABLE TicketTypes
(
    ticket_type_id int PRIMARY KEY,
    type_name      varchar(50) NOT NULL
);

DROP TABLE IF EXISTS `Tickets`;

CREATE TABLE Tickets
(
    ticket_id      int,
    project_id     int,
    ticket_type_id int,
    PRIMARY KEY (ticket_id, project_id, ticket_type_id),
    ticket_name    varchar(50) NOT NULL,
    description    varchar(50) NOT NULL,
    CONSTRAINT fk_7 FOREIGN KEY (project_id) REFERENCES Projects (project_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_8 FOREIGN KEY (ticket_type_id) REFERENCES TicketTypes (ticket_type_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `Employees`;

CREATE TABLE Employees
(
    employee_id   int PRIMARY KEY,
    first_name    varchar(50) NOT NULL,
    last_name     varchar(50) NOT NULL,
    country       varchar(50),
    city          varchar(50),
    state         varchar(50),
    zip_code      int,
    age           int,
    gender        varchar(50),
    date_of_birth DATE,
    salary        int,
    is_remote     boolean,
    supervisor_id int,
    team_id       int,
    CONSTRAINT fk_9 FOREIGN KEY (supervisor_id) REFERENCES Employees (employee_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_10 FOREIGN KEY (team_id) REFERENCES Teams (team_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `Ticket_Assignments`;

CREATE TABLE Ticket_Assignments
(
    employee_id  int,
    ticket_id    int,
    PRIMARY KEY (employee_id, ticket_id),
    is_completed boolean NOT NULL,
    CONSTRAINT fk_11 FOREIGN KEY (employee_id) REFERENCES Employees (employee_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_12 FOREIGN KEY (ticket_id) REFERENCES Tickets (ticket_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `Roles`;

CREATE TABLE Roles
(
    role_id   int PRIMARY KEY,
    role_name varchar(50) NOT NULL
);

DROP TABLE IF EXISTS `Roles`;

CREATE TABLE Employee_Roles
(
    role_id   int,
    employee_id int,
    PRIMARY KEY (role_id, employee_id),
    CONSTRAINT fk_13 FOREIGN KEY (role_id) REFERENCES Roles (role_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_14 FOREIGN KEY (employee_id) REFERENCES Employees (employee_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);





