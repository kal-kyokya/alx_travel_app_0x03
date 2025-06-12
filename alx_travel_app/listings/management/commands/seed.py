import os
import mysql.connector
from dotenv import load_dotenv
from pathlib import Path

class DatabaseConnection():
    """
    automatically handles opening and closing databse connections
    """
    def __init__(self):
        load_dotenv()
        self.DB_NAME = os.getenv("DB_NAME")
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_HOST = os.getenv("DB_HOST")
        self.conn = None

    def __enter__(self):
        print(f"DEBUG: Connecting to Database: {self.DB_name} with:")
        print(f"DEBUG: User: {self.DB_user}, Host: {self.DB_host} and Password: {'*' * len(self.DB_password) if self.DB_password else 'None/Empty'}")
        print("_" * 30)

        try:
            self.conn = mysql.connector.connect(
                host=self.DB_host,
                user=self.DB_user,
                password=self.DB_password,
                database=self.DB_name
                )
            return self.conn
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL server: {err}")
            return None

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.conn is not None:
            self.conn.close()

def execute_queries(sql_file_name, conn):
    file_path = Path(__file__).with_name(sql_file_name)

    with file_path.open('r') as sql_file:
        sql_script = sql_file.read()

    sql_commands = [
        s.strip() for s in sql_script.split(';') if s.strip()
    ]

    print(f"Executing {len(sql_commands)} from {sql_file_name}")

    for command in sql_commands:
        try:
            cursor = conn.cursor()
            cursor.execute(command)
        except mysql.connector.Error as err:
            print(f"Error executing command: {command[:100]} in {sql_file_name}")
            print("Error: : {err}")
            raise
    conn.commit()
    print("Successfully executed: {sql_file_name}")

with DatabaseConnection() as conn:

    execute_queries('schema.sql', conn)
    execute_queries('seed.sql', conn)
