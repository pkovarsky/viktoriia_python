"""- Define class Worker derived from Human with:
  week_salary, work_hours_per_day properties
  money_per_hour() method, returns money earned per hour by the worker
  do_hobby - print 'reading' or some another hobby. """

from lesson_7_hw.lesson_7_hw_1 import Human


class Worker(Human):
    def __init__(self, first_name, last_name, work_hours_per_day, week_salary):
        super().__init__(first_name, last_name)
        self.__work_hours_per_day = work_hours_per_day
        self.__week_salary = week_salary

    @property
    def week_salary(self):
        return self.__week_salary

    @property
    def work_hours_per_day(self):
        return self.__work_hours_per_day

    def money_per_hour(self):
        return self.__week_salary / self.__work_hours_per_day * 5

    def __repr__(self):
        return '({}, {}, {}, {})'.format(self._first_name, self._last_name,
                                         self.__week_salary,
                                         self.__work_hours_per_day)

    def do_hobby(self):
        return "chilling"
