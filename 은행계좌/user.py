# 은행 고객에 대한 클래스
class BankUser:
    def __init__(self, name, money):
        self.__accounts = []
        self.__accounts = []
        self.__name = name
        self.__money = money

    def get_name(self):
        return self.__name

    def add_account(self, account):
        self.__accounts.append(account) # list에 append가 추가

    def get_accounts(self): # 보유하고 있는 계좌의 목록을 출력 
        for account in self.__accounts:
            account.info()

    def add_money(self, amount):
        self.__money += amount

    def deduct_money (self, amount):
        self.__money -= amount

    def get_assets(self): # 자산 보유 메소드 
        print(f"이름: {self.__name}, 보유 현금: ${self.__money}")
        self.get_accounts()

