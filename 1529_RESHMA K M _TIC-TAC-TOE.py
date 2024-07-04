#!/usr/bin/env python
# coding: utf-8

# In[1]:


#game setup
import random

board = [' '] * 10
computer = 'x'
human = 'o'
#displaying board
def display_board(board):
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('-' * 11)
#This function prints out the current state of the board based on the board list.

#checking for a win
def check_win():
    if (board[1] == board[2] == board[3] != ' ') or\
       (board[4] == board[5] == board[6] != ' ') or\
       (board[7] == board[8] == board[9] != ' ') or\
       (board[1] == board[4] == board[7] != ' ') or\
       (board[2] == board[5] == board[8] != ' ') or\
       (board[3] == board[6] == board[9] != ' ') or\
       (board[1] == board[5] == board[9] != ' ') or\
       (board[7] == board[5] == board[3] != ' '):
        return True
    else:
        return False
#This function checks all possible winning combinations of Xs and Os on the board.

#checking for draw
def check_draw():
    if board.count(' ') == 1:  # Only one empty space left means draw
        return True
    else:
        return False
#This function determines if the game has ended in a draw by counting the number of empty spaces left on the board.

#Checking if a Position is Available
def is_available(pos):
    return board[pos] == ' '

#inserting a move
def insert(letter, pos):
    if is_available(pos):
        board[pos] = letter
        display_board(board)
        if check_win():
            if letter == 'x':
                print("Computer wins!")
            else:
                print("Human wins!")
            exit()
        elif check_draw():
            print("It's a draw!")
            exit()
    else:
        if letter == 'o':
            pos = int(input("Position not free! Please re-enter a position: "))
        else:
            pos = random.randint(1, 9)
        insert(letter, pos)
#This fn inserts in specified position and checks the availability of position.

#human move
#This function prompts the human player to input a position to place their 'o' move.
def human_move(letter):
    pos = int(input("Enter the position to insert (1-9): "))
    insert(letter, pos)

#computer move
#this fn generates a random position for the computer's 'x' move and inserts it into the board.
def computer_move(letter):
    pos = random.randint(1, 9)
    insert(letter, pos)

# Main game loop
while not check_win():
    display_board(board)
    computer_move(computer)
    if check_win():
        break
    human_move(human)
    
#This loop continues alternating between the computer and the human making moves until a win or draw condition is met.


# In[ ]:




