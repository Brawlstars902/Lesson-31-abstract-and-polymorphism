from abc import ABC, abstractmethod

class ABCclass(ABC):

    def print(self,x):
        print('passed value is',x)

    @abstractmethod
    def task(self):
        print('We are inside ABsclass task')


class test_class(ABCclass):
    def task(self):
        print('We are inside test_class class')

test_obj=test_class()
test_obj.task()
test_obj.print(100)