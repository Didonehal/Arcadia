import os
#from flappy import game1
#from run import game2
#from TicTacToe import game
from tkinter import *

root = Tk()
w = Label(root, text='WELCOME TO ARCADIA', font = ('cooper black', '36'), fg = "dark blue")
w.pack()
w1 = Label(root, text='Your go to app for arcade games', font = ('monotype corsiva', '28'), fg = "black")
w1.pack()
frame = Frame(root)
frame.pack()
button1 = Button(frame, text = 'Pacman', fg ='red', width = 14, font = ('calibri','24'), command = lambda: os.system('python run.py'))
button1.pack( side = TOP, pady = 5 )
button2 = Button(frame, text = 'Flappy Bird', fg='brown',width = 14, font = ('calibri','24'), command = lambda: os.system('python flappy.py'))
button2.pack( side = TOP, pady = 5 )
button3 = Button(frame, text ='Tic Tac Toe', fg ='blue',width = 14, font = ('calibri','24'), command = lambda: os.system('python TicTacToe.py'))
button3.pack( side = TOP, pady = 5 )
button4 = Button(frame, text ='Quit', fg ='blue', width = 14, font = ('calibri','24'), command = lambda: root.destroy())
button4.pack( side = TOP, pady = 5 )
root.mainloop()