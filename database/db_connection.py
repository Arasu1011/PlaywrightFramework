import sqlite3


class DBConnection:

    def __init__(self):
        self.connection = sqlite3.connect("database/student.db")
        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()