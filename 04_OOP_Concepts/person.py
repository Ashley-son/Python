from abc import ABC, abstractmethod

# 추상클라스 ABC import
class Person(ABC):
    def __init__(self, name,age, job=None):
        self.name = name
        self.age = age  
        self.job = job

    @abstractmethod
    def introduce(self):
        pass

    def hello(self):
        print(f"Hello, I'm {self.name}!")

    def update_age(self,age):
        if age < 0 :
            raise ValueError("나이는 음수일 수 없습니다.")
        
        else:
            self.age = age
            print(f"Now I'm {self.age} years old!")
        self.age = age 

if __name__ == "__main__":
    man = Person("John", 30)
    man.hello()
    man.update_age(31)