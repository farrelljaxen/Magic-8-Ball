import random


while True:
    print("Enter 'help' if you need to know the instructions of the game")
    question = input("Ask the magic 8 ball any question (Press 'q' to quit): \n>").lower()

    answer =random.randint(1,8)
    if question =="":
        print("You didnt enter anything, please enter a question")
    elif question == "help":
        print("""Ok this is the instructions menu:
        In this game you will ask a 'Will' question
        Just like the magic 8 ball it will respond
        """)
    elif question == "q":
        print("Ok I hope you play again!!")
        break
    elif question == "quit":
        print("Ok quitting now.")
        break
    elif 'will' not in question[:4]:
        print("Please start your question with 'Will'")
    elif '?' not in question:
        print("Please add a '?' to your question\n")
    elif answer == 1:
        print("It is certain\n")
    elif answer == 2:
        print("Yes\n")
    elif answer == 3:
        print("Don't count on it\n")
    elif answer == 4:
        print("Cannot predict now\n")
    elif answer == 5:
        print("Very doubtful\n")
    elif answer == 6:
        print("Outlook good\n")
    elif answer == 7:
        print("Ask again later\n")
    elif answer == 8:
        print("My reply is no\n")






