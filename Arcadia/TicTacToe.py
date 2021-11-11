from tkinter import *

root = Tk()

root.title("TIC TAC TOE") # Title

text = Entry(root, font = ("calibri", 35))
text.pack(fill = X, padx = 10, pady = 10, ipadx = 10, ipady = 10) # Text

board = ["-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"] # Board

# Functions
player = 'X'
button =[]
stop_game = False
stop_game_tie = False

def Turn(): # Printing Turn
    text.delete(0, END)
    text.insert(0, "{}'S TURN".format(player))

def Exit():
    root.destroy()
    exit()

def Game_Over(): # Chech if game is over
    Check_Winner()

    if stop_game == True:
        Hplayer()
        text.delete(0, END)
        text.insert(0, "'{}' WINNER".format(player))

    else:
        Check_Tie()

    if stop_game_tie == True:
        text.delete(0, END)
        text.insert(0, "TIE MATCH")

def Check_Winner(): # Check if there is a winner
    global stop_game
    
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        stop_game = True

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        stop_game = True

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        stop_game = True

def Check_Tie(): # Check if it is a tie match
    global stop_game_tie

    if "-" not in board:
        stop_game_tie = True


def Hplayer(): # Managing Turn
    global player

    if player == "X":
        player = "O"
    
    else:
        player = "X"

def Add_Text(pos, play): # Add Text
    global button

    if pos not in button and stop_game == False and stop_game_tie == False and pos != 9:
        Turn()
        
        if play == 'X':
            def_buttons[pos].configure(text = play, fg = "RED")
            board[pos] = player
            button.append(pos)
        else:
            def_buttons[pos].configure(text = play, fg = "BLUE")
            board[pos] = player
            button.append(pos)
        Hplayer()
        Turn()
        Game_Over()

# GRID
def New_Match(): # New Match Button Function
    global board
    global player
    global button
    global stop_game
    global stop_game_tie

    button_1.configure(text = "")
    button_2.configure(text = "")
    button_3.configure(text = "")
    button_4.configure(text = "")
    button_5.configure(text = "")
    button_6.configure(text = "")
    button_7.configure(text = "")
    button_8.configure(text = "")
    button_9.configure(text = "")
    board = ["-", "-", "-",
             "-", "-", "-",
            "-", "-", "-"]
    player = "X"
    button = []
    stop_game = False
    stop_game_tie = False
    Turn()

# Buttons

Turn()

frame = Frame(root)
frame.pack(side = TOP, anchor = NW)

frame1 = Frame(frame)
frame1.pack()

button_1 = Button(frame1, text = "", width = 6, height = 2, command = lambda:Add_Text(0, player), font = ('Helvetica', '26'))
button_1.pack(side = LEFT)

button_2 = Button(frame1, text = "", width = 6, height = 2, command = lambda:Add_Text(1, player), font = ('Helvetica', '26'))
button_2.pack(side = LEFT)

button_3 = Button(frame1, text = "", width = 6, height = 2, command = lambda:Add_Text(2, player), font = ('Helvetica', '26'))
button_3.pack(side = LEFT)

frame2 = Frame(frame)
frame2.pack()

button_4 = Button(frame2, text = "", width = 6, height = 2, command = lambda:Add_Text(3, player), font = ('Helvetica', '26'))
button_4.pack(side = LEFT)

button_5 = Button(frame2, text = "", width = 6, height = 2, command = lambda:Add_Text(4, player), font = ('Helvetica', '26'))
button_5.pack(side = LEFT)

button_6 = Button(frame2, text = "", width = 6, height = 2, command = lambda:Add_Text(5, player), font = ('Helvetica', '26'))
button_6.pack(side = LEFT)

frame3 = Frame(frame)
frame3.pack()

button_7 = Button(frame3, text = "", width = 6, height = 2, command = lambda:Add_Text(6, player), font = ('Helvetica', '26'))
button_7.pack(side = LEFT)

button_8 = Button(frame3, text = "", width = 6, height = 2, command = lambda:Add_Text(7, player), font = ('Helvetica', '26'))
button_8.pack(side = LEFT)

button_9 = Button(frame3, text = "", width = 6, height = 2, command = lambda:Add_Text(8, player), font = ('Helvetica', '26'))
button_9.pack(side = LEFT)

frame4 = Frame(frame)
frame4.pack()

button_clear = Button(frame4, text = "NEW MATCH", width = 20, height = 2, command = lambda:New_Match(), font = ('Helvetica', '17'))
button_clear.pack(side = LEFT)

exit_button = Button(frame4, text = "EXIT", width = 20, height = 2, command = lambda:Exit(), font = ('Helvetica', '17'))
exit_button.pack(side = LEFT)

def_buttons = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

root.mainloop()