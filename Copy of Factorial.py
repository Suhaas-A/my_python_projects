while True:
    number = input("Please enter the number to find its factorial : ")
    try:
        number = int(number)
    except:
        number = number.lower()
        if number == "end" or number == "break" or number == "b" or number == "e":
            break
        else:
            print("Invalid input")
            continue

    x = (number - 1)
    for i in range(x, 1, (-1)):
        number = number * i

    print("The factorial is : ", number)
    
