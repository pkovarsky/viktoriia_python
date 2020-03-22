"""- Define a new class Student which is derived from Human and has:
  grade field.
  do_hobby - print 'dancing' or some another hobby. """

from lesson_7_hw.lesson_7_hw_1 import Human


class Student(Human):
    def __init__(self, first_name, last_name, grade):
        super().__init__(first_name, last_name)
        self.grade = grade

    def __repr__(self):
        return '({}, {}, {})'.format(self._first_name, self._last_name,
                                     self.grade)

    def do_hobby(self):
        return 'sketching'
