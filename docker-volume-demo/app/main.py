import psycopg2
import time

for attempt in range(10):
    try:
        conn = psycopg2.connect(
            host="db",
            user="user",
            password="password",
            dbname="mydb"
        )
        break
    except psycopg2.OperationalError as e:
        print("Database not ready, retrying in 2 seconds...")
        time.sleep(2)
else:
    print("Could not connect to the database after several attempts.")
    exit(1)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")
# ...rest of your code...