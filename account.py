class Account:
    '''
    Method to create accounts.
    '''
    def __init__(self, name: str) -> None:
        '''
        Function to create account variables.
        :param name: string variable to be used as account name.
        '''
        self.__account_name = name
        self.__account_balance = 0
    
    def deposit(self, amount: float) -> bool:
        '''
        Function to add to account balance by the amount
        :param amount: integer variable to add
        :return: boolean variable to signal transaction result
        '''
        if not amount <= 0:
            self.__account_balance += amount
            return True
        else:
            return False
    
    def withdraw(self, amount: float) -> bool:
        '''
        Function to subtract from account balance by the amount
        :param amount: integer variable to subtract
        :return: boolean variable to signal transaction result
        '''
        if not amount <= 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    
    def get_balance(self) -> float:
        '''
        Method to get the account balance
        :return: hidden account balance integer variable
        '''
        return self.__account_balance
    
    def get_name(self) -> str:
        '''
        Method to get the account name
        :return: hidden account name string variable
        '''
        return self.__account_name