while True:
    import random

    rps = ['rock', 'paper', 'scissor']

    inp = str(input("Please enter the item : "))
    inp = inp.lower()

    ai = random.choice(rps)

    if inp == "rock" or inp == "r" or inp =="1":
        inp = "rock"
    elif inp == "scissor" or inp == "s" or inp =="2":
        inp = "scissor"
    elif inp == "paper" or inp == "p" or inp =="3":
        inp = "paper"
    elif inp == "end" or inp == "e" or inp == "break" or inp == "b" or inp == "stop" or inp == "s" or inp == "blast":
        print("")
        break
    else:
        print("invalid input")
        print("")
        continue
    
    if inp == ai:
        print("Tie")
    elif (inp == "rock" and ai == "paper") or (inp == "scissor" and ai == "rock") or (inp == "paper" and ai == "scissor"):
        print("You Lost")
    elif (inp == "rock" and ai == "scissor") or (inp == "scissor" and ai == "paper") or (inp == "paper" and ai == "rock"):
        print("You Won")
    print("")
