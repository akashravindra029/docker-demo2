import psycopg2

conn = psycopg2.connect(
    host="db",
    user="user",
    password="password",
    dbname="mydb"
)

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

# ...existing code...
cursor.executemany(
    "INSERT INTO students (student_id, name, age) VALUES (%s, %s, %s) ON CONFLICT (student_id) DO NOTHING",
    students
)
# ...existing code...  
conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
