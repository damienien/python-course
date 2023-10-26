from bank_account import BankAccount

class SavingAccounts(BankAccount):
    def __init__(self, name: str = 'John', balance: float = 1000, interet: float = 3) -> None:
        super().__init__(name, balance)
        self.interet = interet
        
    def set_rate(self, value):
        self.interet = value
        return self.interet
    
    def capitalization(self, month_count: int):
        capital = (self.interet * self.balance) / 100
        capital = capital * month_count
        return print(f'Solde atteint pour {month_count} mois : {capital} €')
    
    def __str__(self) -> str:
        
        return super().__str__() + f'Taux d\'intérêt : {self.interet} %'

tata = SavingAccounts('tata')
tata.set_rate(25)
tata.capitalization(5)
