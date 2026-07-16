from database.db_connection import DBConnection
from database.db_queries import *


class DBHelper:

    def __init__(self):
        self.db = DBConnection()

    def create_table(self):
        self.db.execute(CREATE_TABLE)

    def clear_students(self):
        self.db.execute(DELETE_ALL)

    def insert_student(self, name, grade, school):
        self.db.execute(
            INSERT_STUDENT,
            (name, grade, school)
        )

    def get_all_students(self):
        self.db.execute(SELECT_ALL)
        return self.db.fetchall()

    def get_student_by_name(self, name):
        self.db.execute(
            SELECT_BY_NAME,
            (name,)
        )
        return self.db.fetchall()

    def update_grade(self, name, grade):
        self.db.execute(
            UPDATE_GRADE,
            (grade, name)
        )

    def delete_student(self, name):
        self.db.execute(
            DELETE_STUDENT,
            (name,)
        )

    def get_student_count(self):
        self.db.execute(COUNT_STUDENTS)
        return self.db.fetchall()[0][0]

    def close(self):
        self.db.close()