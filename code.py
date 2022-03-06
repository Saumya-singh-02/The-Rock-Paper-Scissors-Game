# Import the random module in the next line.
import random

# Create the count_rock, 'count_paper and count_scissors variables and set their initial values equal to 0.
count_rock = 0
count_paper = 0 
count_scissors = 0

# Create the update_counts() function.
def update_counts(user_input):
  global count_scissors, count_rock, count_paper
  if user_input == 0:
    count_rock = count_rock + 1 
  elif user_input == 1:
    count_paper = count_paper +1
  elif user_input == 2:
    count_scissors = count_scissors + 1 
    
    # Create the predict() function.
def predict():
  if count_rock > count_paper and count_rock > count_scissors:
    pred = 0
  elif count_paper > count_rock and count_paper > count_scissors:
    pred = 1 
  elif count_scissors > count_rock and count_scissors > count_paper:
    pred = 2
  else:
    pred = random.randint(0,2)
  
predict()

# Create the player_score and comp_score variables.
player_score = 0
comp_score = 0

# Create the update_scores() function.
def update_scores(user_input):
  global player_score, comp_score
  # Rock wins over scissors, scissors win over paper and paper wins over rock.
  pred = predict()
  if user_input == 0:
    if pred == 0:
      print("\nYou played ROCK, computer played ROCK.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played ROCK, computer played PAPER.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played ROCK, computer played SCISSORS.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)


  elif user_input == 1:
    if pred == 0:
      print("\nYou played ROCK, computer played ROCK.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played ROCK, computer played PAPER.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played ROCK, computer played SCISSORS.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)

      
  else:
    if pred == 2:
      print("\nYou played SCISSOR, computer played SCISSOR.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 0:
      print("\nYou played SCISSOR, computer played ROCK.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played SCISSOR, computer played PAPER.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
      
      
 # 1. Create a list: ['0', '1', '2'] and store it in the variable called valid_entries, i.e, valid_entries = ['0', '1', '2']
valid_entries = ['0','1','2']
i = 1 
# 2. Create an infinite while loop. Inside the loop, create a variable called user_input to store the input taken by the player.
while i>0:
  
  # 3. Use the input() function to take input from a player. 
  user_input = input('Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS:')

  # Inside the input() function, write the Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: statement to show it as a message to a player.

  # 4. Write another while loop to check whether the input provided by a player exists in the valid_entries list or not.
  while user_input not in valid_entries:
    # 5. If the input provided by a player does not exist in the valid_entries list, then print Invalid Input! message. 
    print('Invalid Input!')
    # In the next line, rewrite the user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ") statement.
    user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ")

  # 6. Now, outside the inner while loop, convert the user_input value to an integer value using the int() function. 
  user_input = int(user_input)
  
  # 7. Call the update_scores() function with the user_input as an input to update the scores of the computer and the player.
  update_scores(user_input)
  # 8. Call the update_counts() function with the user_input as an input to update the counts of the inputs provided by the player.
  update_counts(user_input)
  # 9. Write an if statement to check if the score is 10 for any of the player. 
      # If the comp_score == 10, then print the Computer Won! message and break the loop. 
      # Else if the player_score == 10, then print the You won! message and break the loop.
  if comp_score == 10:
   print('COMPUTER WINS')
   print('computer score=', comp_score)
   print('player score= ', player_score)
   break
  elif player_score == 10:
   print('PLAYER WINS')
   print('computer score=', comp_score)
   print('player score= ', player_score)
   break
  
