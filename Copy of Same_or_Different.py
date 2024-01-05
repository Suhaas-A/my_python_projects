import random

while True:
    user_value = str(input("Enter same or different : "))
    user_value = user_value.lower()

    if user_value == "same" or user_value == "s" or user_value == "0":
        user_value = "same"
    elif user_value == "different" or user_value == "d" or user_value == "1":
        user_value = "different"
    elif user_value == "break" or user_value == "end" or user_value == "blast" or user_value == "e" or user_value == "b":
        break
    else:
        print("Invalid input")
        continue

    user_side = str(input("Enter open or close : "))
    user_side = user_side.lower()
    
    if user_side == "open" or user_side == "o" or user_side == "0":
        user_side = "open"
    elif user_side == "close" or user_side == "c" or user_side == "1":
        user_side = "close"
    else:
        print("Invalid input")
        continue

    ai_side = random.choice(["open", "close"])
    
    if (user_value == "same" and ai_side == user_side) or (user_value == "different" and ai_side != user_side):
        print("You won")
    elif (user_value == "different" and ai_side == user_side) or (user_value == "same" and ai_side != user_side):
        print("Machine won")
                    
