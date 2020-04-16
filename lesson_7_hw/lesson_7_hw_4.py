"""- Initialize a list of 5 students and sort them by grade.
- Initialize a list of 5 workers and sort them by money per hour.
- Concatenate the lists and call do_hobby on each object."""
from typing import List

from lesson_7_hw.lesson_7_hw_1 import Human
from lesson_7_hw.lesson_7_hw_2 import Student
from lesson_7_hw.lesson_7_hw_3 import Worker


STUDENTS: List[Human] = [Student("Matthew", "Bale", 89),
                         Student("Sarah", "Michaelsson", 87),
                         Student("Alison", "Walters", 80),
                         Student("Eugene", "Licht", 91),
                         Student("Audrey", "Foubbe", 88)]

WORKERS: List[Human] = [Worker("Jong", "Chris", 8, 200),
                        Worker("Paola", "Murrey", 5, 350),
                        Worker("Freeda", "Pauls", 12, 5),
                        Worker("Richard", "Poulsson", 15, 75),
                        Worker("Stanley", "Racken", 1, 100000)]


def sort_students_grade(student):
    return student.grade


def sort_workers_salary(worker):
    return worker.money_per_hour()


sorted_students_grade = sorted(STUDENTS, key=sort_students_grade)
sorted_workers_salary = sorted(WORKERS, key=sort_workers_salary)

result = STUDENTS + WORKERS
print(result)

hobbies = map(lambda x: x.do_hobby(), result)
