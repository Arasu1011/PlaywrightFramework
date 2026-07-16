CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS students(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,

grade INTEGER,

school TEXT

)
"""


INSERT_STUDENT = """
INSERT INTO students(name,grade,school)

VALUES(?,?,?)
"""


SELECT_ALL = """
SELECT *

FROM students
"""


SELECT_BY_NAME = """
SELECT *

FROM students

WHERE name=?
"""


UPDATE_GRADE = """
UPDATE students

SET grade=?

WHERE name=?
"""


DELETE_STUDENT = """
DELETE FROM students

WHERE name=?
"""


DELETE_ALL = """
DELETE FROM students
"""


COUNT_STUDENTS = """
SELECT COUNT(*)

FROM students
"""