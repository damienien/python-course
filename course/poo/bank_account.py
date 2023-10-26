from typing import Type, Self

class BankAccount:
    def __init__(self, name: str = 'John', balance: float = 1000) -> None:
        self.name = name
        self.balance = balance
        
    def deposit(self, balance: float) -> float:
        self.balance += balance
        return self.balance
    
    def withdraw(self, balance: float) -> None:
        if balance > self.balance:
            print('Vous n\'avez pas assez de fonds pour retirer.')
            return
        
        self.balance -= balance
        return self.balance
    
    def __str__(self) -> str:
        return f'name: {self.name}\nbalance: {self.balance} €\n'
    
    def transfert(self, balance: float, other:Type[Self]) -> float:
        if balance > self.balance:
            print('Vous n\'avez pas assez de fonds pour retirer.')
            return
        
        other.balance += balance
        self.balance -= balance
        print(f'La somme de {balance} € a bien été transféré sur le compte de {other.name} depuis le compte de {self.name}\n')
        return self.balance
    
john = BankAccount()
toto = BankAccount('Toto', 2500.52)

john.deposit(150.05)
print(john)
john.withdraw(3000)
john.withdraw(300)
print(john)

print(toto)
toto.transfert(1000, john)
print(john)
print(toto)