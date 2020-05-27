"""## Homework 8 ##
- Implement PhoneBook class.
- Class should be an iterable.
- Class should contain methods:
  add_contact method (take object: IContact and add it to phone book)
  find_contact method (first match by name)
  remove_contact method (by name)
  call method (take object: IContact and print 'Calling to <contact name>...'])
  recent_calls property (returns recent calls<IContact>)
  add_to_favorites method (take object: IContact and add it to favorites
(only if exists))
  favorites property (returns favorites contacts<IContact>)
- add_contact should check contact's number with regex(or other IValidator)
before add it to phone book
- use OOP and SOLID
** IContact - Interface, PhoneBookContact - class
** IValidator - Interface, RegexValidator - class
** One validator per phone book instance
- Enjoy!"""


from abc import ABC, abstractmethod
from typing import List


class IContact(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def number(self):
        pass


class PhoneBookContact(IContact):
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def number(self):
        return self.__number


class PhoneBook:
    def __init__(self):
        self.__contacts: List[IContact] = []
        self.__calls: List[IContact] = []
        self.__favorites: List[IContact] = []

    def __iter__(self):
        return iter(self.__contacts)

    def add_contact(self, contact: IContact):
        self.__contacts.append(contact)

    def add_to_favorites(self, contact: IContact):
        self.__favorites.append(contact)

    def find_contact(self, name):
        match = list(filter(lambda x: x.name == name, self.__contacts))
        if len(match) != 0:
            return match[0]
        raise Exception(" Just No")

    def remove_contact(self, name):
        item = self.find_contact(name)
        self.__contacts.remove(item)

    def call(self, contact: IContact):
        subscriber = self.find_contact(contact.name)
        print(f"Calling to {subscriber.number}... ")
        self.__calls.append(contact)

    @property
    def recent_calls(self):
        return self.__calls[:10]

    @property
    def favorites(self):
        return self.__favorites
