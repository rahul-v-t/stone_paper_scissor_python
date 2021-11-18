import random
# Rock Paper Scissor Game

choices = ["rock", "paper", "scissor"]
print("Choices :",choices)

user_choice = input("Enter a choice from choices :")
computer_choice = random.choice(choices)

print("Computer choice :",computer_choice)
print("Users choice :",user_choice)

if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("Paper covers rock! You lose.")
    else:
        print("Rock smashes scissors! You win!")
elif user_choice == "paper":
    if computer_choice ==  "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_choice == "scissor":
    if computer_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
else:
    print("Please Enter a proper choice")