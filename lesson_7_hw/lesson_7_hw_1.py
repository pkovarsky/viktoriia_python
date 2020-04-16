"""- Define abstract class Human with:
  first_name, last_name fields (private)
  full_name property
  and a do_hobby abstract method """

from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def full_name(self):
        return self.__first_name, self.__last_name

    @abstractmethod
    def do_hobby(self):
        pass
