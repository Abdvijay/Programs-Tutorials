from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Its running")

class Programmer:
    def work(self,com):
        print("Solving bugs...")
        com.process()

c1 =Laptop()

pg = Programmer()
pg.work(c1)
