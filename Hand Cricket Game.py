#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[8]:


import random

class HandCricketGame:
    def __init__(self):
        self.total_runs = 0

    def play_hand_cricket(self):
        print("Welcome to Hand Cricket!")

        while True:
            print("\nLet's play:")
            print("1. Batting")
            print("2. Bowling")
            print("3. Quit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                self.play_batting()
            elif choice == '2':
                self.play_bowling()
            elif choice == '3':
                print("Thank you for playing Hand Cricket!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def play_batting(self):
        print("\nYou are batting!")

        while True:
            try:
                your_number = int(input("Enter your number (1-6): "))
                if not (1 <= your_number <= 6):
                    print("Please enter a number between 1 and 6.")
                    continue

                computer_number = random.randint(1, 6)
                print(f"Computer's number: {computer_number}")

                if your_number == computer_number:
                    print("Out! Your innings is over.")
                    break
                else:
                    self.total_runs += your_number
                    print(f"Total runs: {self.total_runs}")

            except ValueError:
                print("Invalid input. Please enter a number.")

        print(f"\nYour total runs: {self.total_runs}")

    def play_bowling(self):
        print("\nYou are bowling!")

        while True:
            try:
                your_number = int(input("Enter your number (1-6): "))
                if not (1 <= your_number <= 6):
                    print("Please enter a number between 1 and 6.")
                    continue

                computer_number = random.randint(1, 6)
                print(f"Computer's number: {computer_number}")

                if your_number == computer_number:
                    print("Out! You took a wicket.")
                    break
                else:
                    self.total_runs += computer_number
                    print(f"Computer runs: {computer_number}")
                    print(f"Total runs to chase: {self.total_runs}")

            except ValueError:
                print("Invalid input. Please enter a number.")

        print(f"\nComputer's total runs: {self.total_runs}")

# Main program
if __name__ == "__main__":
    game = HandCricketGame()
    game.play_hand_cricket()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




