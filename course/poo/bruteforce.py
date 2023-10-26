from random import choice
import string
import time
from os.path import exists

class BruteForce:
    def __init__(self, size: int = 1) -> None:
        self.size = size
        self.new_password = ''
    
    def generate_password(self) -> str:
        if self.size > 6 :
            return 'Longueur trop longue. (Maximum 6 caractères)'
        new_password = ''
        asc = string.digits + string.ascii_letters + '()[]:;!'
        for i in range (0, self.size):
            new_password += choice(asc)
        self.new_password = new_password
        return f'Generated password : {self.new_password}'
    
    
    def brute_force(self) -> str:
        if self.new_password == '':
            self.generate_password()
        if self.size > 6:
            return
        start = time.perf_counter()
        asc = string.digits + string.ascii_letters + '()[]:;!'
        decoded_password = ''
        while decoded_password != self.new_password:
            decoded_password = ''.join(choice(asc) for i in range(self.size))
        end = time.perf_counter()
        elapsed_time = round(end - start, 5)
        if exists('./password_logs.txt'):
            t = open('password_logs.txt', "a")
        else:
            t = open('password_logs.txt', 'w')
        t.write(f'The password: {decoded_password} with a length of {self.size} characters took {elapsed_time}s to be forcebrute\n')
        t.close()
        return print(f'The password: {decoded_password} with a length of {self.size} characters took {elapsed_time}s to be forcebrute')
        
toto = BruteForce(3)
# print(toto.generate_password())
toto.brute_force()
