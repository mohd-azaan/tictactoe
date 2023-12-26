from tkinter import Tk, Button, Label, Frame, messagebox ,Entry ,StringVar
from random import choice

def set_placeholder(entry_widget, default_text):
    entry_widget.insert(0, default_text)
    entry_widget.config(fg="grey")
    entry_widget.bind("<FocusIn>", lambda e: on_entry_click(entry_widget, default_text))
    entry_widget.bind("<FocusOut>", lambda e: on_focus_out(entry_widget, default_text))

def on_entry_click(entry_widget, default_text):
    if entry_widget.get() == default_text:
        entry_widget.delete(0, "end")
        entry_widget.config(fg="black")
        
def on_focus_out(entry_widget, default_text):
    if not entry_widget.get():
        entry_widget.insert(0, default_text)
        entry_widget.config(fg="grey")

def changeOnHover(button, colorOnHover, colorOnLeave):
        button.bind('<Enter>', func=lambda e: button.config(background=colorOnHover))
        button.bind('<Leave>', func=lambda e: button.config(background=colorOnLeave))

player1_point = 0
player2_point = 0

def main():
    player_1_name = player_1_name_var.get()  # Fetch the value of Player 1's name
    player_2_name = player_2_name_var.get()  # Fetch the value of Player 2's name

    home_win.withdraw()
    root = Tk()
    global player2_point,player1_point
    root.geometry("400x500+300+200")
    root.title("Tic Tac Toe")
    root.config(bg="white")
    root.resizable(False,False)

    xox = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]

    
    # xox = x if xox == o else o
    # xox=choice(xoro)
    print(xox)

    player_1 = []
    player_2 = []

    labelxox = Label(root, text="Tic Tac Toe", font="serif 30 bold", fg="#3ea4c1",bg="white")
    labelxox.pack(pady=20)
    versus_label = Label(root, text=f"{player_1_name.title()} : {player1_point}\n{player_2_name.title()} : {player2_point}", font="serif 12 ", fg="black",bg="white")
    versus_label.pack()
    
    frame = Frame(root, width=263, height=260, bg="#333333")
    frame.place(x=75,y=200)


    winning_list=[[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6] ]
    def rematch():
        a=messagebox.askyesno("Re match ?","Do you want to play again ?")
        if a == True:
            root.destroy()
            main()
        else :
            exit()
    def disable_all_buttons():
        for button in buttons:
            button.config(state="disabled")


    def check_win(player_1, player_2):
        global player2_point,player1_point

        for i in winning_list:
            if i[0] in player_1 and i[1] in player_1 and i[2] in player_1:
                win_label=Label(root,text=f"Congratulations! {player_1_name.title()} point !",bg="white",font="helvetice 16")
                win_label.pack()
                player1_point+=1
                disable_all_buttons()
                rematch()
                return

            elif i[0] in player_2 and i[1] in player_2 and i[2] in player_2:
                win_label=Label(root,text=f"Congratulations! {player_2_name.title()} point !",bg="white",font="helvetice 16")
                win_label.pack()
                player2_point+=1
                disable_all_buttons()
                
                rematch()
                return

            # Check for draw condition
            elif (len(player_1) + len(player_2) == 9) and not any(all(cell in player_1 for cell in combo) or all(cell in player_2 for cell in combo) for combo in winning_list):
                draw_label=Label(root,text="It's a draw!",bg="white",font="helvetice 16")
                draw_label.pack()
                disable_all_buttons()
                rematch()
    

    
                
    b1 = Button(frame, text="", bg="white", fg="Black", width=11, height=5, relief="flat", command=lambda: on_click(0))
    b1.place(x=0, y=0)
    b2 = Button(frame, text="", bg="white", fg="Black", width=11, height=5, relief="flat", command=lambda: on_click(1))
    b2.place(x=88, y=0)
    b3 = Button(frame, text="", bg="white", fg="Black", width=11, height=5, relief="flat", command=lambda: on_click(2))
    b3.place(x=176, y=0)
    b4 = Button(frame, text="", bg="white", fg="Black", width=11, height=5, relief="flat", command=lambda: on_click(3))
    b4.place(x=0, y=87)
    b5 = Button(frame, text="", bg="white", fg="Black", width=11, height=5, relief="flat", command=lambda: on_click(4))
    b5.place(x=88, y=87)
    b6 = Button(frame, text="", bg="white", fg="Black", width=11, height=5, relief="flat", command=lambda: on_click(5))
    b6.place(x=176, y=87)
    b7 = Button(frame, text="", bg="white", fg="Black", width=11, height=5, relief="flat", command=lambda: on_click(6))
    b7.place(x=0, y=174)
    b8 = Button(frame, text="", bg="white", fg="Black", width=11, height=5, relief="flat", command=lambda: on_click(7))
    b8.place(x=88, y=174)
    b9 = Button(frame, text="", bg="white", fg="Black", width=11, height=5, relief="flat", command=lambda: on_click(8))
    b9.place(x=176, y=174)

    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    def on_click(i):
        button = buttons[i]
        if xox[0] == "X":
            button.config(text="X")
            player_1.append(i)
        else:
            button.config(text="O")
            player_2.append(i)
        del xox[0]
        button.config(state="disabled")
        check_win(player_1, player_2)
        
    for button in buttons:
        changeOnHover(button, "lightgrey", "white")

    root.mainloop()

home_win=Tk()    

home_win.geometry("400x500+300+200")
home_win.title("Tic Tac Toe")
home_win.config(bg="white")
home_win.resizable(False,False)

labelxox = Label(home_win, text="Tic Tac Toe", font="serif 30 bold", fg="#3ea4c1",bg="white")
labelxox.pack(pady=20)

global frame_start
global player_1_name_entry, player_2_name_entry

frame_start = Frame(home_win, width=263, height=260, bg="white")
frame_start.place(x=108, y=130)
        
player_1_name_var= StringVar()
player_2_name_var= StringVar()

player_1_name_entry = Entry(frame_start,textvariable=player_1_name_var, width=30, relief="flat",font=("Times New Roman", 11))
player_1_name_entry.place(x=10, y=0)
ask_line=Frame(frame_start, width=185, height=1.5, bg="black")
ask_line.place(x=10, y=20)
set_placeholder(player_1_name_entry, "Enter Player 1 Name")

player_2_name_entry = Entry(frame_start,textvariable=player_2_name_var, width=30, relief="flat",font=("Times New Roman", 11))
player_2_name_entry.place(x=10, y=50)
ask_line=Frame(frame_start, width=185, height=1.5, bg="black")
ask_line.place(x=10, y=70)
set_placeholder(player_2_name_entry, "Enter Player 2 Name")

start_button = Button(frame_start,font="comicsans 13 ", bg="#3ec4c7",relief="flat",text="Start Game", command= main)
start_button.place(x=51, y=100)

changeOnHover(start_button,"#3ea4a1","#3ec4c7")


home_win.mainloop()