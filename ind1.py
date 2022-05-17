#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Man:
    def __init__(self, name, age, sex, weight):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__weight = weight

    def change_name(self, new_name):
        self.__name = new_name

    def change_age(self, new_age):
        self.__age = new_age

    def change_weight(self, new_weight):
        self.__weight = new_weight

    def print_info(self):
        print("Class Man")
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Sex: {self.__sex}")
        print(f"Weight: {self.__weight}")


class Student(Man):
    def __init__(self, name, age, sex, weight, study_year):
        super().__init__(name, age, sex, weight)
        self.__study_year = study_year

    def change_study_year(self, new_st_year):
        self.__study_year = new_st_year

    def increment_study_year(self):
        self.__study_year += 1

    def print_info(self):
        print("Class Student")
        super().print_info()
        print(f"Study year: {self.__study_year}")


if __name__ == '__main__':
    man = Man('Arseniy', 23, 'male', 89)
    man.print_info()
    man.change_name('Alex')
    man.change_age(24)
    man.change_weight(95)
    man.print_info()
    st1 = Student('Eugene', 20, 'male', 70, 2)
    st1.print_info()
    st1.change_weight(72)
    st1.change_name('Alex')
    st1.increment_study_year()
    st1.change_study_year(6)
    st1.print_info()
