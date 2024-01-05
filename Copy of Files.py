from tkinter import *
box = Tk()

global count
global file
global add_button
global multiply
global del_multiply

count = 0
del_multiply = 0
multiply = 0

file = open('Good.txt', 'r')

for line in file:
    count += 1

file.close()

header = Frame(box, highlightbackground="black", highlightthickness=3, height=110, width=1517)
header.place(x=10, y=10)

body = Frame(box, highlightbackground="black", highlightthickness=3, height=653, width=1517)
body.place(x=10, y=130)

header_text = Label(header, text="CONTACT LIST", font=(40))
header_text.place(x=667, y=40)

contacts = Label(body, text="", font=(20))
contacts.place(x=15, y=50)

def add():
    def add_contact():
        global file
        global count
        global ordinate
        global add_button
        global multiply
        global delete_button
        global del_multiply

        multiply = 0

        file = open('Good.txt', 'r')
        for a in file:
            multiply += 1

        file.close()
        
        name = str(new_name.get())
        phone = str(new_phone.get())
        
        file = open('Good.txt', 'a')
        if multiply == 0 or del_multiply > 0:
            del_multiply = 0
            to_write = (str(name) + ' : ' + str(phone))
        elif multiply > 0:
            to_write = ("\n" + str(name) + ' : ' + str(phone))
        file.write(to_write)
        file.close()
        file = open('Good.txt', 'r')
        contacts.config(text=(file.read()))
        file.close()
        add_box.destroy()
        add_button.place(x=15, y=(((multiply * 22) + 82)))
        delete_button.place(x=200, y=(((multiply * 22) + 82)))
        
    add_box = Toplevel(box)
    add_box.geometry("300x300")
    new_name = Entry(add_box, width=30)
    new_name.place(x=10, y=10)
    label_name = Label(add_box, text="add name", height=1)
    label_name.place(x=200, y=10)
    new_phone = Entry(add_box, width=30)
    new_phone.place(x=10, y=50)
    label_phone = Label(add_box, text="add phone number", height=1)
    label_phone.place(x=200, y=50)
    new_submit = Button(add_box, text="Submit", height=1, command=add_contact)
    new_submit.place(x=100, y=100)
    add_box.mainloop()

def delete():
    def delete_contact():
        global add_button
        global file
        global del_multiply
        global each_contact

        del_multiply = 0
        
        file = open("Good.txt", 'r')
        for b in file:
            del_multiply += 1
        file.close()
        file = open("Good.txt" , 'r')
        each_contact = {}
        del_name = str(delete_name.get())
        del_counts = 0
        for values in file:
            splitted = values.split(" : ")
            to_append = splitted[0]
            each_contact[to_append] = splitted[1]
            if to_append == del_name:
                to_remove = to_append
        file.close()
        each_contact.pop(to_remove)
        file = open('Good.txt', 'w')
        file.write("")
        file.close()
        file = open('Good.txt', 'a')
        for k,w in each_contact.items():
            if del_counts == 0:
                file.write(str(k) + " : " + str(w))
            else:
                file.write("\n" + str(k) + " : " + str(w))
        file.close()
        file = open('Good.txt' , 'r')
        contacts.config(text=(file.read()))
        file.close()
        delete_box.destroy()
        add_button.place(x=15, y=(((del_multiply - 1) * 22) + 82))
        delete_button.place(x=200, y=(((del_multiply - 1) * 22) + 82))
        
    delete_box = Toplevel(box)
    delete_box.geometry("300x300")
    del_label_name = Label(delete_box, text="delete name", height=1)
    del_label_name.place(x=200, y=10)
    delete_name = Entry(delete_box, width=30)
    delete_name.place(x=10, y=10)
    delete_submit = Button(delete_box, text="Submit", height=1, command=delete_contact)
    delete_submit.place(x=100, y=60)

file = open('Good.txt', 'r')

add_button = Button(body, text="Add a new contact", height=2, width=15, command=add)
add_button.place(x=15, y=((count * 22) + 60))

delete_button = Button(body, text="Delete a contact", height=2, width=16, command=delete)
delete_button.place(x=200, y=((count * 22) + 60))

contents = file.read()

contacts.config(text=contents)

file.close()

def go():
    search_entry = str(search.get())
    get_contacts = {}
    file = open("Good.txt", "r")
    for one_contact in file:
        search_splitted = one_contact.split(" : ")
        get_contacts[search_splitted[0]] = search_splitted[1]
    for e,f in get_contacts.items():
        if e == search_entry:
            got_it_name = e
            got_it_phone = f
            search_output = ((str(e) + " : " + str(f)))
    search_box = Toplevel(box)
    try:
        show_search_label = Label(search_box, text=search_output)
    except:
        show_search_label = Label(search_box, text="Nothing Found")
    show_search_label.place(x=10, y=10)
    file.close()

search_label = Label(body, text="search:", font=(20))
search_label.place(x=15, y=10)

search = Entry(body, width=30)
search.place(x=90, y=16)

search_button = Button(body, text="GO", command=go)
search_button.place(x=290, y=16)

box.mainloop()
