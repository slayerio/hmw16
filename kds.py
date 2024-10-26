import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="gommuno777",
                        port=5433)

cursor = conn.cursor()
cursor.execute("select version();")
print(cursor.fetchone())
