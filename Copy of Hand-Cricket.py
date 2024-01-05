import random
import math

score = 0
ai_score = 0

while True:    
    toss_choice = str(input("Please enter odd or even : "))

    toss_choice = toss_choice.lower()
    
    if toss_choice != "odd" and toss_choice != "even" and toss_choice != "o" and toss_choice != "e":
        print("")
        print("Invalid input")
        print("")
        continue
    
    if toss_choice == "odd" or toss_choice == "o":
        toss_choice = "odd"
        ai_choice = "even"
    elif toss_choice == "even" or toss_choice == "e":
        toss_choice = "even"
        ai_choice = "odd"

    ai_number = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    try:
        toss_number = int(input("Please enter a number for toss : "))
    except:
        print("")
        print("Invalid input")
        print("")
        continue

    add = ai_number + toss_number
    if math.remainder(add, 2) == 0:
        thing = "even"
    else:
        thing = "odd"
    break

while True:
    if toss_choice == thing:
        print("")
        print("You won the toss")
        print("")
        try:
            bat_or_bowl = str(input("Please enter whether you are batting or bowling : "))
            print("")
        except:
            print("")
            print("Invalid input")
            print("")
            continue
        bat_or_bowl.lower()
        if bat_or_bowl != "bat" and bat_or_bowl != "bowl" and bat_or_bowl != "batting" and bat_or_bowl != "bowling":
            print("")
            print("Invalid input")
            print("")
            continue

        if bat_or_bowl == "bat" or bat_or_bowl == "batting":
            bat_or_bowl = "bat"
            bat = 1
        elif bat_or_bowl == "bowl" or bat_or_bowl == "bowling":
            bat_or_bowl = "bowl"
            bat = 2
            
    elif ai_choice == thing:
        ai_bat_or_bowl = random.choice(["bat", "bowl"])
        print("")
        print("You lost the toss, machine chose to : ", ai_bat_or_bowl)
        print("")
        if ai_bat_or_bowl == "bat":
            bat_or_bowl = "bowl"
            bat = 2
        if ai_bat_or_bowl == "bowl":
            bat_or_bowl = "bat"
            bat = 1
    break

while True:
    if bat_or_bowl == "bat":
        if score == 0:
            print("")
            print("You are batting : ")
        ai_play = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        try:
            user_number = int(input("Please enter the number : "))
        except:
            print("Invalid input")
            continue
        
        if user_number not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print("Invalid input")
            continue

        if user_number == ai_play:
            print("out")
            print("")
            if bat == 2 and ai_score > score:
                print("Your score : ", score)
                print("")
                print("You lost by : ", (ai_score - score))
                break
            elif bat == 2 and ai_score == score:
                print("It was a tie")
                break
            else:
                bat_or_bowl = "bowl"
                print("Your score : ", score)
                print("")
                print("Machine target : ", score + 1)
                continue
        elif user_number == 0 and ai_play != 0:
            score += ai_play
        elif user_number != ai_play and user_number != 0:
            score += user_number

        if bat == 2 and score > ai_score:
            print("")
            print("")
            print("Your score : ", score)
            print("You won")
            print("")
            break

        print("Your score : ", score)
        print("")

    elif bat_or_bowl == "bowl":
        if ai_score == 0:
            print("")
            print("You are bowling : ")
        ai_play = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        try:
            user_number = int(input("Please enter the number : "))
        except:
            print("Invalid input")
            continue
        
        if user_number not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print("Invalid input")
            continue

        if user_number == ai_play:
            print("")
            print("out")
            if bat == 1 and ai_score < score:
                print("Machine score : ", ai_score)
                print("")
                print("You won by  : ", (score - ai_score))
                break
            elif bat == 1 and ai_score == score:
                print("It was a tie")
                break
            else:
                print("Machine score : ", ai_score)
                print("")
                bat_or_bowl = "bat"
                print("Your target : ", ai_score + 1)
                continue
        elif ai_play == 0 and user_number != 0:
            ai_score += user_number
        elif user_number != ai_play and ai_play != 0:
            ai_score += ai_play

        if bat == 1 and score < ai_score:
            print("")
            print("")
            print("Machine score : ", ai_score)
            print("You lost")
            print("")
            break

        print("Machine score : ", ai_score)
        print("")

    

            
    

    

