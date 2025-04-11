import random


while True:
    make_choice = input("Roll the dice? (y/n): ").lower()
    if make_choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1,6)
        print(f"({die1}, {die2})")
    elif make_choice == "n":
        print("Thank you for playing")
        break
    else:
        print("Invalid choice") 



#import random

#for _ in iter(int, 1):  # infinite loop similar to while True
#    make_choice = input("Roll the dice? (y/n): ").lower()
#    if make_choice == "y":
#        die1 = random.randint(1, 6)
#        die2 = random.randint(1, 6)
#        print(f"({die1}, {die2})")
#    elif make_choice == "n":
#        print("Thank you for playing")
#        break
#    else:
#        print("Invalid choice")
          
