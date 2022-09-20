import tkinter as tk
from tkinter import ttk
import random


root = tk.Tk()

root.geometry('300x130')
root.title('Rock, Paper, Scissors')
root.resizable(False, False)


radio_var=tk.IntVar()
x = 0
y = 0

rock_button = ttk.Radiobutton(root, text='Rock', variable=radio_var, value=0)
paper_button = ttk.Radiobutton(root, text='Paper', variable=radio_var, value=1)
scissors_button = ttk.Radiobutton(root, text='Scissors', variable=radio_var, value=2)
ready_button = ttk.Button(root, text='Ready!')
score_label = ttk.Label(root, text='Choose your destiny', font=('arial', 10, 'bold'))
newgame_button = ttk.Button(root, text='New game')
game_label = ttk.Label(root, text=' ', font=('arial', 10, 'bold'))
pc_pick = ttk.Label(root, text=' ', font=('arial', 8, 'bold'))


score_label.place(relx=0.05, rely=0.05)
rock_button.place(relx=0.05, rely=0.2)
paper_button.place(relx=0.05, rely=0.35)
scissors_button.place(relx=0.05, rely=0.5)
ready_button.place(relx=0.05, rely=0.65)
newgame_button.place(relx=0.7, rely= 0.05)
game_label.place(relx=0.72, rely = 0.4)
pc_pick.place(relx=0.72, rely=0.6)

def game():
    
    global x, y, radio_var
    if x<99 and y<99:
    
        pc=random.randint(0,2)
        radio_var1 = radio_var.get()
        
        if pc==0:
            pc_pick['text']='PC: Rock'
        elif pc==1:
            pc_pick['text']='PC: Paper'
        else:
            pc_pick['text']='PC: Scissors'

        if radio_var1==0 and pc==1:
            y+=1
            game_label['text'] = 'You lost!'

        elif radio_var1==0 and pc==2:
            x+=1
            game_label['text'] = 'You won!'

        elif radio_var1==0 and pc==0:
            game_label['text'] = 'Game tied'

        elif radio_var1==1 and pc==2:
            y+=1
            game_label['text'] = 'You lost!'

        elif radio_var1==1 and pc==0:
            x+=1
            game_label['text'] = 'You won!'

        elif radio_var1==1 and pc==1:
            game_label['text'] = 'Game tied'

        elif radio_var1==2 and pc==0:
            y+=1
            game_label['text'] = 'You lost!'

        elif radio_var1==2 and pc==1:
            x+=1
            game_label['text'] = 'You won!'

        elif radio_var1==2 and pc==2:
            game_label['text'] = 'Game tied'
            
        score_label['text'] = f'Score: {x}:{y}'

    elif x==99 and y<99:

        game_label['text']='Max score'
        pc_pick['text']='You won! :)'

    elif x<99 and y==99:

        game_label['text']='Max score'
        pc_pick['text']='You lost :('

def new_game():

    global x, y
    x = 0
    y = 0
    score_label['text'] = 'Choose your destiny'
    game_label['text'] = ' '

newgame_button['command'] = new_game
ready_button['command'] = game
ready_button.bind_all('<Return>', lambda event:game())


root.mainloop()