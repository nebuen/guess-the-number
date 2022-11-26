#Number Guessing Game Objectives:
from art import logo
import random
#print(logo)
game_should_end = False
attempts = 0
user_guess = 0
computer_number_guess = random.randint(1,5)
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


  
def compare(computer):
  global attempts
  global user_guess
  user_guess = int(input("Make a guess: "))
  if user_guess == computer:
    print(f"You got it! The answer was {computer}")
    return
  elif user_guess > computer:
    print("Too high")
    attempts = attempts - 1
    print(f"You have {attempts} attempts remaining")
  elif user_guess < computer:
    print("Too low")
    attempts = attempts - 1
    print(f"You have {attempts} attempts remaining")
  

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number betwween 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
  print("You have 10 attempts remaining to guess the number")
  attempts = 10
  print(attempts)
else:
  print("You have 5 attempts remaining to guess the number.")
  attempts = 5
  print(attempts)

for attempt in range(1, attempts + 1):
  compare(computer_number_guess)
  if user_guess == computer_number_guess:
    #print(f"You have {attempts}")
    break
  