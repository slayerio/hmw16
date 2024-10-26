import sqlite3

conn: any = None
cursor: any = None


def connect(file_name: str) -> any:
    global conn, cursor
    conn = sqlite3.connect(file_name)
    conn.row_factory = sqlite3.Row  # allow to use column names
    cursor = conn.cursor()  # Create cursor


def run_query_update(query: str, params=()) -> None:
    cursor.execute(query, params)
    cursor.connection.commit()


def run_query_select(query: str, params: tuple = ()) -> list[tuple]:
    cursor.execute(query, params)
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]
    return result


def close():
    cursor.close()
