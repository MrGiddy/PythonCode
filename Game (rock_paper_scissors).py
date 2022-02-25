import random
computer_score = 0
user_score = 0
valid_choices = ["rock", "paper", "scissors"]

while True:
    user_picks = input("Choose \"Rock\", \"Paper\" or \"Scissors\" to play. Enter q to quit game: ").lower()
    if user_picks == "q":
            break
    if user_picks not in valid_choices:
        print("You like breaking rules.")
        print("Please enter a valid option.")
        continue
    random_number = random.randint(0,2)
    computer_picks = valid_choices[random_number]  #3 is "rock", 4 is "paper", 5 is "scissors"
    if computer_picks == "rock" and user_picks == "scissors":
            computer_score += 1
            print("Computer won.", "Computer score is", str(computer_score) + ".", "Your score is", user_score)
    elif computer_picks == "paper" and user_picks == "rock":
            computer_score += 1
            print("Computer won.", "Computer score is", str(computer_score) + ".", "Your score is", user_score)
    elif computer_picks == "scissors" and user_picks == "paper":
            computer_score += 1
            print("Computer won.", "Computer score is", str(computer_score) + ".", "Your score is", user_score)
    elif computer_picks == user_picks:
            print("Whoa! This is a draw.")
    else:
            user_score += 1
            print("You won", "Your score is", user_score, "Computer score is", computer_score)


#Many thanks to Tech With Tim