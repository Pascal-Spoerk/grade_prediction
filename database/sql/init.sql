DROP DATABASE grade_prediction;
CREATE DATABASE grade_prediction;
USE grade_prediction;

CREATE TABLE students_training (
    id INT AUTO_INCREMENT PRIMARY KEY,
    school VARCHAR(10),
    sex VARCHAR(1),
    age INT,
    address VARCHAR(1),
    famsize VARCHAR(4),
    Pstatus VARCHAR(1),
    Medu INT,
    Fedu INT,
    Mjob VARCHAR(20),
    Fjob VARCHAR(20),
    reason VARCHAR(20),
    guardian VARCHAR(20),
    traveltime INT,
    studytime INT,
    failures INT,
    schoolsup VARCHAR(5),
    famsup VARCHAR(5),
    paid VARCHAR(5),
    activities VARCHAR(5),
    nursery VARCHAR(5),
    higher VARCHAR(5),
    internet VARCHAR(5),
    romantic VARCHAR(5),
    famrel INT,
    freetime INT,
    goout INT,
    Dalc INT,
    Walc INT,
    health INT,
    absences INT,
    G3 INT
);