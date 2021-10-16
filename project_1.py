def game():
    print("WELCOME TO THE QUIZ SHOW")
    play = input("Do you wanna start the game? Type Y for Yes and N for No- ")
    if play.lower()!="y":
        quit()
    point = 0
    if play.lower()=="y":
        print("What is the capital of India?")
        answer = input()
        if answer=="Delhi":
            print("You got it right!! ")
            point = point+1
            print(f"congratulations, you got 1 point. Total Points so far - {point}")
        else:
            print("incorrect answer!!")
            print(f"No point this time. Total Point till this answer - {point}")

        print("What is the capital of USA?")
        answer = input()
        if answer == "Washington":
            print("You got it right!! ")
            point = point + 1
            print(f"congratulations, you got 1 point. Total Points so far - {point}")
        else:
            print("incorrect answer!!")
            print(f"No point this time. Total Point till this answer - {point}")

        print("What is the capital of Russia?")
        answer = input()
        if answer == "Moscow":
           print("You got it right!! ")
           point = point + 1
           print(f"congratulations, you got 1 point. Total Points so far - {point}")
        else:
           print("incorrect answer!!")
           print(f"No point this time. Total Point till this answer - {point}")

        print("What is the capital of China?")
        answer = input()
        if answer == "Beijing":
           print("You got it right!! ")
           point = point + 1
           print(f"congratulations, you got 1 point. Total Points so far - {point}")
        else:
           print("incorrect answer!!")
           print(f"No point this time. Total Point till this answer - {point}")

    print("QUIZ OVER!")

    result = input("Do you wanna see your result? Type Y for yes, N for no- ")
    if result.lower()=="n":
        print("Thanks for playing. GoodBye!!")
        quit()
    else:
        print(f"Your score is {point}")
        print("Thanks for playing. GoodBye!!")

    again = input("D you wanna play again? Type Y for yes and N for no: ")
    if again.lower()!="y":
        quit()
    else:
        game()

print(game())