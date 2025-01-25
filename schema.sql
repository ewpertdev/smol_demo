-- Crear y usar la base de datos
DROP DATABASE IF EXISTS gastos_demo;
CREATE DATABASE gastos_demo;
USE gastos_demo;

-- Eliminar tablas si existen (en orden inverso por las foreign keys)
DROP TABLE IF EXISTS expenses;
DROP TABLE IF EXISTS users;

-- Crear tablas
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    username VARCHAR(100) NOT NULL
);

CREATE TABLE expenses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    description VARCHAR(255) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
); 