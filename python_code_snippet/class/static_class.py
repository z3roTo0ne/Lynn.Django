# coding=utf-8
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._nick_name = ""

    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, your_nick_name):
        if not isinstance(your_nick_name, str):
            raise ValueError("nick_name must be string.")
        self._nick_name = your_nick_name

    def full_name(self):
        return self.last_name + self.first_name

    @classmethod
    def display_city(cls, city_name):
        print("your city is: {}".format(city_name))

    @staticmethod
    # static method out `self` agrument
    def display_country():
        print("all of you are chinese.")


class Student(Person):
    def __init__(self, first_name, last_name):
        super(Student, self).__init__(first_name, last_name)

if __name__ == "__main__":
    a = Student("lin","chen")
    a.nick_name = "snake"
    print("getattr: {}".format(getattr(a, "last_name")))
    # print(a._nick_name)
    # Access to a protected member _nick_name of a class，不要直接访问protect或者private变量，
    # 通过方法暴露出来
    print(a.nick_name)
    print(a.display_city("mianyang"))
    print(Person.display_city("shenzhen"))

