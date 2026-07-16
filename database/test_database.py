from database.db_helper import DBHelper


def test_database():

    db = DBHelper()

    # -----------------------------
    # Create Table
    # -----------------------------
    db.create_table()

    # -----------------------------
    # Delete Existing Records
    # -----------------------------
    db.clear_students()

    # -----------------------------
    # Insert
    # -----------------------------
    db.insert_student(
        "Hamsika",
        5,
        "Alagappa"
    )

    students = db.get_all_students()

    print(students)

    assert len(students) == 1
    assert students[0][1] == "Hamsika"
    assert students[0][2] == 5
    assert students[0][3] == "Alagappa"

    print("Insert Test Passed")

    # -----------------------------
    # Select by Name
    # -----------------------------
    student = db.get_student_by_name("Hamsika")

    print(student)

    assert len(student) == 1
    assert student[0][1] == "Hamsika"

    print("Select Test Passed")

    # -----------------------------
    # Update
    # -----------------------------
    db.update_grade("Hamsika", 6)

    student = db.get_student_by_name("Hamsika")

    assert student[0][2] == 6

    print("Update Test Passed")

    # -----------------------------
    # Count
    # -----------------------------
    count = db.get_student_count()

    print("Student Count :", count)

    assert count == 1

    print("Count Test Passed")

    # -----------------------------
    # Delete
    # -----------------------------
    db.delete_student("Hamsika")

    student = db.get_student_by_name("Hamsika")

    assert len(student) == 0

    print("Delete Test Passed")

    db.close()

    print("\nDatabase CRUD Framework PASSED")