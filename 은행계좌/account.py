import random # random 라이브러리 호출 
from abc import ABC, abstractmethod # 추상 method 호출 

# balance = 잔액
# holder_name = 소유주명
# account_number = 계좌번호

class BankAccount(ABC): # 예금 계좌 클래스 생성 
    def __init__(self, holder_name, balance):
        self._account_number = random.randint(10000000, 99999999)
        self._holder_name = holder_name
        self.__balance = balance

    def get_account_number(self): # Getter 메서드 생성  
        return self._account_number # return 값을 통한 결과값 전달 

    def get_balance (self) : # get 메소드 선언 필요 
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount # 캡술화 구현 

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError
        else:
            self.__balance -= amount
            return self.__balance

    @abstractmethod
    def info(self):
        pass    

        
class SavingAccount(BankAccount):
    def __init__(self, holder_name, balance, interest_rate):
        super().__init__(holder_name, balance) # 부모클래스가 갖는 초기 속성이 설정
        self.__interest_rate = interest_rate # private field
        self.__is_locked = True

    def withdraw(self, amount):
        if self.__is_locked == True:
            raise AttributeError
        else:
            super().withdraw(amount)

    def unlock(self): 
        self.__is_locked = False
        interest = self.get_balance() * self.__interest_rate # 잔액 * 이율
        self.deposit(interest) # 결국엔 이율 곱한게 저축으로 되는 거니까 deposit에 넣어줘야함

    def info(self): # info 메소드 정의
            print(f"[예금/{self.get_account_number()}] 잔액${self.get_balance()}, 이율{self.__interest_rate*100}%, 출금 제한 여부: {self.__is_locked}")
            
class CheckingAccount(BankAccount): # 입출금 계좌 class 생성 
    def __init__(self, holder_name, balance, withdraw_limit = 500): # 생성자 정의 
            super().__init__(holder_name, balance)
            self.__withdraw_limit = withdraw_limit

    def update_limit(self, new_limit): # 출금 한도 설정 
            self.__withdraw_limit = new_limit


    def withdraw(self, amount):
            if(self.__withdraw_limit < amount): # 출금 계좌가 한도 이상이면 밸류에러 발생 
                raise ValueError
            else:
                super().withdraw(amount) # 그게 아니라면 부모계좌에 금액을 차감하는 시스템 

    def info(self):
            print(f"[입출금/{self.get_account_number()} 잔액 $ {self.get_balance()},출금한도 ${self.__withdraw_limit}]")
