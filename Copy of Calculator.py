#must
from tkinter import *
box = Tk()

#code
times = 0
expression = ""
current_number = 0
numbers = []
operators = []
def calculate(value):
    global times
    global expression
    global current_number
    global numbers
    global operators
    if value == 1:
        current_number = (current_number * 10) + int(value)
        expression += str(value)
        writer.config(text=expression)
        times += 1
        
    if value == 2:
        current_number = (current_number * 10) + int(value)
        expression += str(value)
        writer.config(text=expression)
        times += 1
        
    if value == 3:
        current_number = (current_number * 10) + int(value)
        expression += str(value)
        writer.config(text=expression)
        times += 1
        
    if value == 4:
        current_number = (current_number * 10) + int(value)
        expression += str(value)
        writer.config(text=expression)
        times += 1
        
    if value == 5:
        current_number = (current_number * 10) + int(value)
        expression += str(value)
        writer.config(text=expression)
        times += 1
        
    if value == 6:
        current_number = (current_number * 10) + int(value)
        expression += str(value)
        writer.config(text=expression)
        times += 1
        
    if value == 7:
        current_number = (current_number * 10) + int(value)
        expression += str(value)
        writer.config(text=expression)
        times += 1
        
    if value == 8:
        current_number = (current_number * 10) + int(value)
        expression += str(value)
        writer.config(text=expression)
        times += 1
        
    if value == 9:
        current_number = (current_number * 10) + int(value)
        expression += str(value)
        writer.config(text=expression)
        times += 1

    if value == 0:
        current_number = (current_number * 10) + int(value)
        expression += str(value)
        writer.config(text=expression)
        times += 1

    if value == "+":
        times = 0
        numbers.append(current_number)
        operators.append(str(value))
        expression += str(value)
        writer.config(text=expression)
        plus.config(state=DISABLED)
        minus.config(state=DISABLED)
        multiplication.config(state=DISABLED)
        division.config(state=DISABLED)
        current_number = 0

    if value == "-":
        times = 0
        numbers.append(current_number)
        operators.append(str(value))
        expression += str(value)
        writer.config(text=expression)
        plus.config(state=DISABLED)
        minus.config(state=DISABLED)
        multiplication.config(state=DISABLED)
        division.config(state=DISABLED)
        current_number = 0

    if value == "*":
        times = 0
        numbers.append(current_number)
        operators.append(str(value))
        expression += str(value)
        writer.config(text=expression)
        plus.config(state=DISABLED)
        minus.config(state=DISABLED)
        multiplication.config(state=DISABLED)
        division.config(state=DISABLED)
        current_number = 0

    if value == "/":
        times = 0
        numbers.append(current_number)
        operators.append(str(value))
        expression += str(value)
        writer.config(text=expression)
        plus.config(state=DISABLED)
        minus.config(state=DISABLED)
        multiplication.config(state=DISABLED)
        division.config(state=DISABLED)
        current_number = 0

    if times > 0:
        plus.config(state=NORMAL)
        minus.config(state=NORMAL)
        multiplication.config(state=NORMAL)
        division.config(state=NORMAL)

def operate():
    global numbers
    global current_number
    global operators
    global expression
    numbers.append(current_number)

    while True:
    
        for sign_div in operators:
            if sign_div == "/":
                i = operators.index('/')
                a = numbers[i]
                b = numbers[(i + 1)]
                output = a / b
                operators.remove('/')
                numbers.remove(a)
                numbers.remove(b)
                numbers.insert(i, output)

        for sign_mul in operators:
            if sign_mul == "*":
                i = operators.index('*')
                a = numbers[i]
                b = numbers[(i + 1)]
                output = a * b
                operators.remove('*')
                numbers.remove(a)
                numbers.remove(b)
                numbers.insert(i, output)

        for sign_min in operators:
            if sign_min == "-":
                i = operators.index('-')
                a = numbers[i]
                b = numbers[(i + 1)]
                output = a - b
                operators.remove('-')
                numbers.remove(a)
                numbers.remove(b)
                numbers.insert(i, output)

        for sign_add in operators:
            if sign_add == "+":
                i = operators.index('+')
                a = numbers[i]
                b = numbers[(i + 1)]
                output = a + b
                operators.remove('+')
                numbers.remove(a)
                numbers.remove(b)
                numbers.insert(i, output)

        if len(operators) == 0:
            writer.config(text=numbers[0])
            current_number = numbers[0]
            expression = str(numbers[0])
            numbers = []
            break

def clear(func):
    if func == "clear":
        global numbers
        global operators
        global current_number
        global times
        global expression
        numbers = []
        operators = []
        current_number = 0
        times = 0
        expression = ""
        writer.config(text=expression)
    elif func == "clear_one":
        if (expression[(len(expression) - 1)] == "+") or (expression[(len(expression) - 1)] == "-") or (expression[(len(expression) - 1)] == "*") or (expression[(len(expression) - 1)] == "/"):
            current_number = numbers[(len(numbers) - 1)]
            times = len(str(current_number))
            plus.config(state=NORMAL)
            minus.config(state=NORMAL)
            multiplication.config(state=NORMAL)
            division.config(state=NORMAL)
            numbers.pop(len(numbers) - 1)
            operators.pop(len(operators) - 1)
        else:
            current_number = int(current_number)
            last_index = len(str(current_number)) - 1
            last_number = str(current_number)[last_index]
            current_number = (current_number - int(last_number)) / 10
            current_number = int(current_number)
        expression = expression[0 : ((len(expression)) - 1)]
        writer.config(text=expression)


writer = Label(box, text=expression, width=100, height=3, bg="cyan", font=(1000, 15, "bold"))
number1 = Button(box, text="1", command=lambda:calculate(1), height=10, width=20)
number2 = Button(box, text="2", command=lambda:calculate(2), height=10, width=20)
number3 = Button(box, text="3", command=lambda:calculate(3), height=10, width=20)
number4 = Button(box, text="4", command=lambda:calculate(4), height=10, width=20)
number5 = Button(box, text="5", command=lambda:calculate(5), height=10, width=20)
number6 = Button(box, text="6", command=lambda:calculate(6), height=10, width=20)
number7 = Button(box, text="7", command=lambda:calculate(7), height=10, width=20)
number8 = Button(box, text="8", command=lambda:calculate(8), height=10, width=20)
number9 = Button(box, text="9", command=lambda:calculate(9), height=10, width=20)
number0 = Button(box, text="0", command=lambda:calculate(0), height=10, width=20)
plus = Button(box, text="+", command=lambda:calculate("+"), height=10, width=20)
minus = Button(box, text="-", command=lambda:calculate("-"), height=10, width=20)
multiplication = Button(box, text="*", command=lambda:calculate("*"), height=10, width=20)
division = Button(box, text="/", command=lambda:calculate("/"), height=10, width=20)
equal = Button(box, text="=", command=operate, height=10, width=20)
clear_all = Button(box, text="C", command=lambda:clear("clear"), height=10, width=20)
clear_one = Button(box, text="CE", command=lambda:clear("clear_one"), height=10, width=20)

writer.place(x=10, y=10)
number1.place(x=10, y=100)
number2.place(x=210, y=100)
number3.place(x=410, y=100)
number4.place(x=10, y=300)
number5.place(x=210, y=300)
number6.place(x=410, y=300)
number7.place(x=10, y=500)
number8.place(x=210, y=500)
number9.place(x=410, y=500)
plus.place(x=610, y=100)
minus.place(x=610, y=300)
multiplication.place(x=610, y=500)
division.place(x=810, y=100)
equal.place(x=810, y=300)
number0.place(x=810, y=500)
clear_all.place(x=1010, y=100)
clear_one.place(x=1010, y=300)
box.mainloop()
