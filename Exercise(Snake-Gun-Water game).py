def game():
    import random 

    print("Welcome to Snake, Gun, Water Game!")
    print("RULES:")
    print("Gun vs Snake: Gun wins")
    print("Water vs Gun: Water wins")
    print("Snake vs Water: Snake wins")

    choices = ["1", "2", "3"]
    print("Enter your choice (1 for Snake, 2 for Gun, 3 for Water):")
    user_score = 0
    computer_score = 0
    while True:
        user=input("Enter the choice (1/2/3) or 'exit' to quit: ")
        if user=='exit':
            break
        if user not in choices:
            print("Invalid choice! Please choose 1, 2, or 3.")
            continue
        computer=random.choice(choices)
        print(f"Computer chose: {computer}")
        if user==computer:
            print('It is tie')
        elif (user=='1' and computer=='3') or (user=='2' and computer=='1') or (user=='3' and computer=='2'):
            print('You win!')
            user_score+=1
        else:
            print('Computer wins!')
            computer_score+=1
        print(f"Score: You {user_score} - Computer {computer_score}")

game()