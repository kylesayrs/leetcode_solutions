from typing import Callable


class Foo:
    def __init__(self):
        self.first_sent = False
        self.second_sent = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        printFirst()
        self.first_sent = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.first_sent:
            pass
        
        printSecond()
        self.second_sent = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.second_sent:
            pass
        
        printThird()
        self.first_sent = False
        self.second_sent = False
