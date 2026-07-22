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
    FiftyOption=["(New Delhi, Kolkata)","(print(), output())","(Tiger, Cheetah)"]
    PrizeMoney=[100,200,500]
    Prize=0
    FiftyUsed = False

    for i in range(len(Questions)):
        print(Questions[i])
        print(Option[i])
        while True:
                UserInput = input("Enter your Answer, 50-50, or Quit: ")

                if UserInput.strip().lower() == "quit":
                     return f"The Final Prize You Won is: {Prize}"   

                elif UserInput.strip().lower() == Answer[i].lower():
                    print("Sahi Jawab!")
                    Prize=PrizeMoney[i]
                    print(Prize)
                    break

                elif UserInput.strip().lower()=="50-50" and FiftyUsed == False :
                    print(FiftyOption[i])
                    FiftyUsed=True # Lifeline use hote hi True
                    UserInput2=(input("Enter the UserInput2: "))
                    if UserInput2.strip().lower() == Answer[i].lower():
                        print("Sahi Jawab!")
                        Prize=PrizeMoney[i]
                        print(Prize)
                        break
                        
                    else:
                        print("Galat Jawab!")
                        Prize=0
                        print(Prize)
                        return f"The Final Prize You Won is: {Prize}"
                
                elif UserInput.strip().lower() == "50-50" and FiftyUsed == True:
                        print("50-50 Lifeline already used!")
 
                    
                else:
                    print("Galat Jawab!")
                    Prize=0
                    print(Prize)
                    return f"The Final Prize You Won is: {Prize}"
    return f"The Final Prize You Won is: {Prize}"


print(play_game())




# # Second way:- 
# questions = [
#     [
#         "1. What is the capital of India?",
#         "Mumbai", "New Delhi", "Kolkata", "Chennai",
#         2
#     ],
#     [
#         "2. Which programming language is known as the 'Father of AI' language?",
#         "Python", "Java", "LISP", "C++",
#         3
#     ],
#     [
#         "3. Who is known as the Father of the Indian Constitution?",
#         "Mahatma Gandhi", "Dr. B. R. Ambedkar", "Jawaharlal Nehru", "Sardar Patel",
#         2
#     ],
#     [
#         "4. Which planet is known as the Red Planet?",
#         "Earth", "Jupiter", "Mars", "Venus",
#         3
#     ],
#     [
#         "5. Which data type is used to store True or False values in Python?",
#         "int", "float", "bool", "str",
#         3
#     ],
#     [
#         "6. How many continents are there in the world?",
#         "5", "6", "7", "8",
#         3
#     ],
#     [
#         "7. Which is the largest ocean in the world?",
#         "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean",
#         3
#     ],
#     [
#         "8. Who invented the World Wide Web (WWW)?",
#         "Bill Gates", "Tim Berners-Lee", "Steve Jobs", "Elon Musk",
#         2
#     ],
#     [
#         "9. Which keyword is used to define a function in Python?",
#         "func", "define", "def", "function",
#         3
#     ]
# ]


# prize_money = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000 ]

# money=0
# for i in range(len(questions)):
#      question=questions[i]
#      print(f"\n\nQuestions for Rs. {prize_money[i]}")
#      print(f"Question Apki Screen pe ye raha: {question[0]}")
#      print(f"a. {question[1]}        b. {question[2]}  ")
#      print(f"c. {question[3]}        d. {question[4]}  ")
#      reply=int(input("Enter the answer (1-4): "))
#      if(reply == question[-1]):
#           print(f"Correct answer ,you have won Rs. {prize_money[i]}")
#           if i==3:
#             money =10000
#           elif (i==8):
#               money =320000
          
#      else:
#          print("Wrong Answer!")
#          break
# print(f"You take  home money is: {money}")
