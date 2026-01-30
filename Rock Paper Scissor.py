import random 

options = ("rock" , "paper" , "scissors")
running = True
user_score = 0
computer_Score = 0

print("-----------------------------------")
print("Welcome to Rock-Paper-Scissors Game")
print("-----------------------------------")

while running:

    player = None
    print("\nChosse one:")
    print("Rock | Paper | Scissors")

    player = input("Enter a choice: ").lower()

    if player not in options:
        print("Invalid Choice! Please Choose (Rock | Paper | Scissors)")
        continue
    
    computer = random.choice(options)


    print(f"Player Choice: {player}")
    print(f"Computer Choice: {computer}")    

    if player == computer:
        print("It's a tie!")
    elif (
         ( player == "rock" and computer == "scissors" ) or
         ( player == "paper" and computer == "rock" ) or
         ( player == "scissors" and computer == "paper" ) ):
        print("You Win!")
        user_score += 1
              
    else:
        print("You Lose!") 
        computer_Score += 1


    print()
    print("------------------------")
    print("Score Board")
    print("------------------------")
    print(f"Player: {user_score}")
    print(f"Computer: {computer_Score}")


    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False
        print()
        print("Thanks for playing!")   
        print("------------------------")
        print("Final Score: ")
        print("------------------------")
        print(f"Player: {user_score} | Computer: {computer_Score}")   
        if user_score > computer_Score :
            print("Player Win")
        elif user_score == computer_Score:
            print("It's a tie")    
        else :
            print("Computer Win")        

            
             