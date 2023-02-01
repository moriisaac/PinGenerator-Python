##Author Mori Isaac

import random
number = int(input("Input Pin Number: "))
trial = 0
while(trial != number):
    trial = random.randint(0, 9999)
    print(trial)
print("Your Pin is" + str(number))
