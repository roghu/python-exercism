from src.grade_school import School


class TestGradeSchool:
    def test_adding_a_student_adds_them_to_the_sorted_roster(self) -> None:
        school = School()
        school.add_student(name="Aimee", grade=2)
        expected = ["Aimee"]
        assert school.roster() == expected

    def test_adding_more_students_adds_them_to_the_sorted_roster(self) -> None:
        school = School()
        school.add_student(name="Blair", grade=2)
        school.add_student(name="James", grade=2)
        school.add_student(name="Paul", grade=2)
        expected = ["Blair", "James", "Paul"]
        assert school.roster() == expected

    def test_adding_students_to_different_grades_adds_them_to_the_same_sorted_roster(
        self,
    ) -> None:
        school = School()
        school.add_student(name="Chelsea", grade=3)
        school.add_student(name="Logan", grade=7)
        expected = ["Chelsea", "Logan"]
        assert school.roster() == expected

    def test_roster_returns_an_empty_list_if_there_are_no_students_enrolled(
        self,
    ) -> None:
        school = School()
        expected: list[str] = []
        assert school.roster() == expected

    def test_student_names_with_grades_are_displayed_in_the_same_sorted_roster(
        self,
    ) -> None:
        school = School()
        school.add_student(name="Peter", grade=2)
        school.add_student(name="Anna", grade=1)
        school.add_student(name="Barb", grade=1)
        school.add_student(name="Zoe", grade=2)
        school.add_student(name="Alex", grade=2)
        school.add_student(name="Jim", grade=3)
        school.add_student(name="Charlie", grade=1)
        expected = ["Anna", "Barb", "Charlie", "Alex", "Peter", "Zoe", "Jim"]
        assert school.roster() == expected

    def test_grade_returns_the_students_in_that_grade_in_alphabetical_order(
        self,
    ) -> None:
        school = School()
        school.add_student(name="Franklin", grade=5)
        school.add_student(name="Bradley", grade=5)
        school.add_student(name="Jeff", grade=1)
        expected = ["Bradley", "Franklin"]
        assert school.grade(5) == expected

    def test_grade_returns_an_empty_list_if_there_are_no_students_in_that_grade(
        self,
    ) -> None:
        school = School()
        expected: list[str] = []
        assert school.grade(1) == expected
