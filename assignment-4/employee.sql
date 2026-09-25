CREATE DATABASE employee;

USE employee;

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary FLOAT,
    email VARCHAR(100)
);

INSERT INTO employee VALUES
(1, 'Rahul', 'IT', 50000, 'rahul@gmail.com'),
(2, 'Priya', 'HR', 45000, 'priya@gmail.com'),
(3, 'Amit', 'Finance', 55000, 'amit@gmail.com'),
(4, 'Sneha', 'IT', 60000, 'sneha@gmail.com'),
(5, 'Rohan', 'Sales', 40000, 'rohan@gmail.com');

SELECT * FROM employee;
