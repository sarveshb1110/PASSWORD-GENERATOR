print("\nWE ARE MAKING AN AUTOMATIC RANDOM PASSWORD GENERATOR")

import random

characters=("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()")

password=""

l=int(input("Please enter the length of password you want (1-8):"))

for i in range(l):
    password+=random.choice(characters)

    if l<8:
            pass

    else:
        print("You can only generate password of less than 8 digits ")
        break
            
    
print(f"\nYour Password is {password}")
    
    



    
    
    


