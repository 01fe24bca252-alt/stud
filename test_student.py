import subprocess
import sys
import os

# ---------------- PATH FIX ----------------
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STUDENT_FILE = os.path.join(PROJECT_DIR, "student.py")

# Ensure student.py can be imported
sys.path.insert(0, PROJECT_DIR)

# ---------------- UNIT TESTS ----------------

def test_grade_s():
    from student import calculate_grade
    assert calculate_grade(95) == "S"

def test_grade_a():
    from student import calculate_grade
    assert calculate_grade(85) == "A"

def test_grade_b():
    from student import calculate_grade
    assert calculate_grade(70) == "B"

def test_grade_c():
    from student import calculate_grade
    assert calculate_grade(55) == "C"

def test_grade_d():
    from student import calculate_grade
    assert calculate_grade(45) == "D"

def test_grade_f():
    from student import calculate_grade
    assert calculate_grade(30) == "F"


# ---------------- INTEGRATION TEST ----------------

def test_student_program_execution():
    result = subprocess.run(
        [
            sys.executable,
            STUDENT_FILE,
            "Prasanna",
            "Integrated_MCA",
            "3",
            "98",
            "97",
            "96"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Debug help if something fails
    assert result.returncode == 0, result.stderr

    assert "Prasanna" in result.stdout
    assert "Integrated_MCA" in result.stdout
    assert "Average" in result.stdout
    assert "Grade" in result.stdout
