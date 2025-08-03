import psycopg2
import time

for i in range(10):
    try:
        conn = psycopg2.connect(
            host="db",
            user="user",
            password="password",
            dbname="mydb"
        )
        break
    except psycopg2.OperationalError:
        print("Waiting for PostgreSQL to be ready...")
        time.sleep(2)
else:
    print("Could not connect to PostgreSQL.")
    exit(1)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")

students = [
    (100, 'Manoj', 22),
    (99, 'Mick', 24),
    (98, 'Raj', 25)
]

cursor.executemany(
    "INSERT INTO students (student_id, name, age) VALUES (%s, %s, %s) ON CONFLICT (student_id) DO NOTHING",
    students
)
conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()