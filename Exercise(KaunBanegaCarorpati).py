def play_game():
    Questions = [
        "1. What is the capital of India?",
        "2. Which function is used to display output in Python?",
        "3. What is the national animal of India?"
    ]

    Option = [
        "[Mumbai, New Delhi, Kolkata, Chennai]",
        "[input(), show(), print(), output()]",
        "[Lion, Elephant, Tiger, Cheetah]"
    ]

    Answer = ["New Delhi", "print()", "Tiger"]
    PrizeMoney=0
    for i in range(len(Questions)):
        print(Questions[i])
        print(Option[i])
        UserInput=(input("Enter the User Answer: "))
        if UserInput.strip().lower() == Answer[i].lower():
            print("Sahi Jawab!")
            PrizeMoney+=100
            print(PrizeMoney)
        else:
            print("Galat Jawab!")
            PrizeMoney=0
            print(PrizeMoney)
            break
    return f"The Final Prize is: {PrizeMoney}"


print(play_game())


#Practice:-
# Ques1="What is the capital of India?"
# print(Ques1)
# Option=["Mumbai","New Delhi","Kolkata","Chennai"]
# print(Option)
# PrizeMoney=0
# UserInput=(input("Enter the input: "))
# if UserInput== "Mumbai":
#     print("Galat Jawab!")
#     PrizeMoney-=10
#     print(PrizeMoney)
     
# elif UserInput== "New Delhi":
#     print("Sahhi Jawab!")
#     PrizeMoney+=10
#     print(PrizeMoney)
 
# elif UserInput== "Kolkata":
#      print("Galat Jawab!")
#      PrizeMoney-=10
#      print(PrizeMoney)

# elif UserInput== "Chennai":
#      print("Galat Jawab!")
#      PrizeMoney-=10
#      print(PrizeMoney)

# else:
#      print("Invalid Answer Please check and try Again!")












