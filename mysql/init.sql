CREATE USER 'usuario'@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'usuario'@'%';
FLUSH PRIVILEGES;

CREATE TABLE DISTRITOS (
    id INT PRIMARY KEY AUTO_INCREMENT,
    distrito JSON
);