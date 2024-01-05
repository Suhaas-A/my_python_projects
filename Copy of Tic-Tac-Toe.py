#must
from tkinter import *
from tkinter import messagebox
box = Tk()

turn = "x"
box1 = ""
box2 = ""
box3 = ""
box4 = ""
box5 = ""
box6 = ""
box7 = ""
box8 = ""
box9 = ""

#code
def clear():
    global turn
    global box1
    global box2
    global box3
    global box4
    global box5
    global box6
    global box7
    global box8
    global box9
    turn = "x"
    box1 = ""
    box2 = ""
    box3 = ""
    box4 = ""
    box5 = ""
    box6 = ""
    box7 = ""
    box8 = ""
    box9 = ""
    button1.config(text="", state=NORMAL)
    button2.config(text="", state=NORMAL)
    button3.config(text="", state=NORMAL)
    button4.config(text="", state=NORMAL)
    button5.config(text="", state=NORMAL)
    button6.config(text="", state=NORMAL)
    button7.config(text="", state=NORMAL)
    button8.config(text="", state=NORMAL)
    button9.config(text="", state=NORMAL)

def write(button):
    global turn
    global box1
    global box2
    global box3
    global box4
    global box5
    global box6
    global box7
    global box8
    global box9
    if button == 1:
        if turn == "x":
            button1.config(text="X", state=DISABLED)
            box1 = "x"
            turn = "o"
        elif turn == "o":
            button1.config(text="O", state=DISABLED)
            box1 = "o"
            turn = "x"

    if button == 2:
        if turn == "x":
            button2.config(text="X", state=DISABLED)
            box2 = "x"
            turn = "o"
        elif turn == "o":
            button2.config(text="O", state=DISABLED)
            box2 = "o"
            turn = "x"

    if button == 3:
        if turn == "x":
            button3.config(text="X", state=DISABLED)
            box3 = "x"
            turn = "o"
        elif turn == "o":
            button3.config(text="O", state=DISABLED)
            box3 = "o"
            turn = "x"

    if button == 4:
        if turn == "x":
            button4.config(text="X", state=DISABLED)
            box4 = "x"
            turn = "o"
        elif turn == "o":
            button4.config(text="O", state=DISABLED)
            box4 = "o"
            turn = "x"

    if button == 5:
        if turn == "x":
            button5.config(text="X", state=DISABLED)
            box5 = "x"
            turn = "o"
        elif turn == "o":
            button5.config(text="O", state=DISABLED)
            box5 = "o"
            turn = "x"

    if button == 6:
        if turn == "x":
            button6.config(text="X", state=DISABLED)
            box6 = "x"
            turn = "o"
        elif turn == "o":
            button6.config(text="O", state=DISABLED)
            box6 = "o"
            turn = "x"

    if button == 7:
        if turn == "x":
            button7.config(text="X", state=DISABLED)
            box7 = "x"
            turn = "o"
        elif turn == "o":
            button7.config(text="O", state=DISABLED)
            box7 = "o"
            turn = "x"

    if button == 8:
        if turn == "x":
            button8.config(text="X", state=DISABLED)
            box8 = "x"
            turn = "o"
        elif turn == "o":
            button8.config(text="O", state=DISABLED)
            box8 = "o"
            turn = "x"

    if button == 9:
        if turn == "x":
            button9.config(text="X", state=DISABLED)
            box9 = "x"
            turn = "o"
        elif turn == "o":
            button9.config(text="O", state=DISABLED)
            box9 = "o"
            turn = "x"
    if (box1 == "x" and box2 == "x" and box3 == "x") or (box4 == "x" and box5 == "x" and box6 == "x") or (box7 == "x" and box8 == "x" and box9 == "x"):
        print('x wins')
        messagebox.showinfo("Result","X wins")
    elif (box1 == "x" and box4 == "x" and box7 == "x") or (box2 == "x" and box5 == "x" and box8 == "x") or (box3 == "x" and box6 == "x" and box9 == "x"):
        print('x wins')
        messagebox.showinfo("Result","X wins")
    elif (box1 == "x" and box5 == "x" and box9 == "x") or (box3 == "x" and box5 == "x" and box7 == "x"):
        print('x wins')
        messagebox.showinfo("Result","X wins")
    elif (box1 == "o" and box2 == "o" and box3 == "o") or (box4 == "o" and box5 == "o" and box6 == "o") or (box7 == "o" and box8 == "o" and box9 == "o"):
        print('o wins')
        messagebox.showinfo("Result","O wins")
    elif (box1 == "o" and box4 == "o" and box7 == "o") or (box2 == "o" and box5 == "o" and box8 == "o") or (box3 == "o" and box6 == "o" and box9 == "o"):
        print('o wins')
        messagebox.showinfo("Result","O wins")
    elif (box1 == "o" and box5 == "o" and box9 == "o") or (box3 == "o" and box5 == "o" and box7 == "o"):
        print('o wins')
        messagebox.showinfo("Result","O wins")


button1 = Button(box, command=lambda:write(1), height=5, width=10, bg="cyan", fg="green")
button2 = Button(box, command=lambda:write(2), height=5, width=10, bg="cyan", fg="green")
button3 = Button(box, command=lambda:write(3), height=5, width=10, bg="cyan", fg="green")
button4 = Button(box, command=lambda:write(4), height=5, width=10, bg="cyan", fg="green")
button5 = Button(box, command=lambda:write(5), height=5, width=10, bg="cyan", fg="green")
button6 = Button(box, command=lambda:write(6), height=5, width=10, bg="cyan", fg="green")
button7 = Button(box, command=lambda:write(7), height=5, width=10, bg="cyan", fg="green")
button8 = Button(box, command=lambda:write(8), height=5, width=10, bg="cyan", fg="green")
button9 = Button(box, command=lambda:write(9), height=5, width=10, bg="cyan", fg="green")

label = Label(text="TIC-TAC-TOE")

buttonc = Button(box, command=clear, height=18, width=15, text="clear", bg="lime")

button1.place(x=100, y=100)
button2.place(x=200, y=100)
button3.place(x=300, y=100)
button4.place(x=100, y=200)
button5.place(x=200, y=200)
button6.place(x=300, y=200)
button7.place(x=100, y=300)
button8.place(x=200, y=300)
button9.place(x=300, y=300)
buttonc.place(x=500, y=100)
label.place(x=200, y=40)

box.mainloop()
