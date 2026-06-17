create database nayepankh;
use nayepankh;

create table volunteers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL,
    city VARCHAR(100),
    skills VARCHAR(255),
    availability VARCHAR(100),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table admins(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

insert into admins(username,password)
VALUES('admin','admin123');
select * from volunteers;
SHOW CREATE TABLE volunteers;
SHOW INDEX FROM volunteers;
SELECT id, name, skills
FROM volunteers;