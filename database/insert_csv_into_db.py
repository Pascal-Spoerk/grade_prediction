import pandas as pd
import mariadb

mat = pd.read_csv("dataset/student-mat.csv", sep=";")
por = pd.read_csv("dataset/student-por.csv", sep=";")

students = pd.concat([mat, por], ignore_index=True)

conn = mariadb.connect(
    user="root",
    password="weixlberg",
    host="localhost",
    port=3306,
    database="grade_prediction"
)
cursor = conn.cursor()

query = """
INSERT INTO students_training (
    school, sex, age, address, famsize, Pstatus,
    Medu, Fedu, Mjob, Fjob, reason, guardian,
    traveltime, studytime, failures, schoolsup, famsup, paid,
    activities, nursery, higher, internet, romantic,
    famrel, freetime, goout, Dalc, Walc, health,
    absences, G3
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

for _, row in students.iterrows():
    cursor.execute(query, (
        row["school"], row["sex"], int(row["age"]), row["address"], row["famsize"], row["Pstatus"],
        int(row["Medu"]), int(row["Fedu"]), row["Mjob"], row["Fjob"], row["reason"], row["guardian"],
        int(row["traveltime"]), int(row["studytime"]), int(row["failures"]), row["schoolsup"], row["famsup"], row["paid"],
        row["activities"], row["nursery"], row["higher"], row["internet"], row["romantic"],
        int(row["famrel"]), int(row["freetime"]), int(row["goout"]), int(row["Dalc"]), int(row["Walc"]), int(row["health"]),
        int(row["absences"]), int(row["G3"])
    ))

conn.commit()
conn.close()
