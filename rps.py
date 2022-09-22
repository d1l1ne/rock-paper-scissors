import tkinter as tk
from tkinter import ttk
import random
from PIL import ImageTk, Image

menu_size='400x400'
game_size='960x540'
OptionList=["Best of 9", "Best of 11", "Best of 21", "Up to 99"]


root = tk.Tk()
root.geometry(menu_size)
root.title('Rock, Paper, Scissors')
root.resizable(False, False)

selected_mode=tk.StringVar()

s = ttk.Style()
s.configure('mainb.TButton', font=('Tahoma', 18))
s.configure('secb.TButton', font=('Tahoma', 16))
s.configure('thib.TButton', font=('Tahoma', 13))
s.configure("t1.TMenubutton", font=('Tahoma', 14))

new_game = ttk.Button(root, text='NEW GAME', style='mainb.TButton')
set_count=ttk.OptionMenu(root, selected_mode, OptionList[0], *OptionList, style='t1.TMenubutton')

new_game.place(relheight=0.2, relwidth=0.4, rely=0.3, relx=0.3)
set_count.place(relheight=0.08, relwidth=0.4, rely=0.55, relx=0.3)


def menu_start():

    global game_size
    gamemode = selected_mode.get()
    pl_score = 0
    pc_score = 0
    pc_rock = ImageTk.PhotoImage(Image.open("./pictures/rockpc.png"))
    pc_paper = ImageTk.PhotoImage(Image.open("./pictures/paperpc.png"))
    pc_scissors = ImageTk.PhotoImage(Image.open("./pictures/scissorspc.png"))
    pl_rock = ImageTk.PhotoImage(Image.open("./pictures/rockplayer.png"))
    pl_paper = ImageTk.PhotoImage(Image.open("./pictures/paperplayer.png"))
    pl_scissors = ImageTk.PhotoImage(Image.open("./pictures/scissorsplayer.png"))
    q_mark = ImageTk.PhotoImage(Image.open("./pictures/qmark.png"))
    rock_i = ImageTk.PhotoImage(Image.open("./pictures/rockicon.png"))
    paper_i = ImageTk.PhotoImage(Image.open("./pictures/papericon.png"))
    scissors_i = ImageTk.PhotoImage(Image.open("./pictures/scissorsicon.png"))

    root.withdraw()
    pc_pick=0
    pl_pick=0
    game_win = tk.Toplevel(root)
    game_win.geometry(game_size)
    game_win.title(f'Score 0-0. {gamemode}')
    game_win.resizable(False, False)
    score_title = ttk.Label(game_win, text='Score:', font=('Tahoma', 32))
    score_label = ttk.Label(game_win, text=f'{pl_score} : {pc_score}', font=('Tahoma', 24, 'bold'))
    result_label = ttk.Label(game_win, text=' ', font=('Tahoma', 32))
    pc_image = ttk.Label(game_win)
    pl_image = ttk.Label(game_win)
    pc_image.configure(image=q_mark)
    pc_image.image=q_mark
    pl_image.configure(image=q_mark)
    pl_image.image=q_mark
    pc_title = ttk.Label(game_win, text='PC:', font=('Tahoma', 24, 'bold'))
    pl_title = ttk.Label(game_win, text='YOU:', font=('Tahoma', 24, 'bold'))
    mode_title = ttk.Label(game_win, text=gamemode, font=('Tahoma', 16))
    rock_button = ttk.Button(game_win, image=rock_i)
    rock_button.image=rock_i
    paper_button = ttk.Button(game_win, image=paper_i)
    paper_button.image=paper_i
    scissors_button = ttk.Button(game_win, image=scissors_i)
    scissors_button.image=scissors_i
    back_button = ttk.Button(game_win, text='Menu', style='secb.TButton')
    playagain_button = ttk.Button(game_win, text='Play again', style='mainb.TButton')
    close_button = ttk.Button(game_win, text='Back to menu', style='thib.TButton')
    overall_label = ttk.Label(game_win, font = ('Tahoma', 28))


    score_title.place(relx=0.44, rely=0.05)
    score_label.place(relx=0.464, rely=0.17)
    result_label.place(relx=0.405, rely=0.65)
    pc_image.place(relx=0.65, rely=0.3)
    pl_image.place(relx=0.09, rely=0.3)
    pc_title.place(relx=0.755, rely=0.21) 
    pl_title.place(relx=0.18, rely=0.21)
    mode_title.place(relx=0.455, rely=0.25)
    rock_button.place(relwidth=0.057, relheight=0.1, relx=0.1, rely=0.8)
    paper_button.place(relwidth=0.057, relheight=0.1, relx=0.190, rely=0.8)
    scissors_button.place(relwidth=0.057, relheight=0.1, relx=0.280, rely=0.8)
    close_button.place(relwidth=0.12, relheight=0.07, relx=0.72, rely=0.81)

    


    if (selected_mode.get()=='Best of 9'):

        gm=5 

    elif (selected_mode.get()=='Best of 11'):
        
        gm=6

    elif (selected_mode.get()=='Best of 21'):
            
        gm=11

    elif (selected_mode.get()=='Up to 99'):

        gm=99

    def close_game():

        root.deiconify()
        game_win.destroy()

    def play_again():

        game_win.destroy()
        menu_start()

    def game_over(score_a, score_b):

        rock_button.place_forget()
        paper_button.place_forget()
        scissors_button.place_forget()
        result_label.place_forget()
        close_button.place_forget()

        if score_a>score_b:
            overall_label['text'] = 'C o n g r a t u l a t i o n s,   y o u   w o n!'
        else:
            overall_label['text'] = 'B e t t e r   l u c k   n e x t   t i m e!  : )'

        overall_label.place(relx=0.144, rely=0.82)
        back_button.place(relwidth=0.14, relheight=0.08, relx=0.43, rely=0.62)
        playagain_button.place(relwidth=0.22, relheight=0.12, relx=0.39, rely=0.46)


    def game_rock(): 
        
        nonlocal pl_score, pc_score, pl_pick, pc_pick

        pl_pick = 0
        pl_image.configure(image=pl_rock)
        pl_image.image=pl_rock
        pc_pick = random.randint(0, 2)
            
        if pc_pick==0:

            pc_image.configure(image=pc_rock)
            pc_image.image=pc_rock
            result_label['text']='Game tied'

        elif pc_pick==1:

            pc_image.configure(image=pc_paper)
            pc_image.image=pc_paper
            result_label['text']='You lost!'
            pc_score+=1

        else:

                pc_image.configure(image=pc_scissors)
                pc_image.image=pc_scissors
                result_label['text']='You won!'
                pl_score+=1

        score_label['text'] = f'{pl_score} : {pc_score}'

        if pl_score>9 and pc_score<=9:

            score_label.place_forget()
            score_label.place(relx=0.443, rely=0.17)

        if pl_score>9 and pc_score>9:

            score_label.place_forget()
            score_label.place(relx=0.44, rely=0.17)


        if pl_score==gm or pc_score==gm:

            game_over(pl_score, pc_score)

    def game_paper(): 

        nonlocal pl_score, pc_score, pl_pick, pc_pick

        pl_pick = 0
        pl_image.configure(image=pl_paper)
        pl_image.image=pl_paper
        pc_pick = random.randint(0, 2)
            
        if pc_pick==1:

            pc_image.configure(image=pc_paper)
            pc_image.image=pc_paper
            result_label['text']='Game tied'

        elif pc_pick==2:

            pc_image.configure(image=pc_scissors)
            pc_image.image=pc_scissors
            result_label['text']='You lost!'
            pc_score+=1

        else:

            pc_image.configure(image=pc_rock)
            pc_image.image=pc_rock
            result_label['text']='You won!'
            pl_score+=1

        score_label['text'] = f'{pl_score} : {pc_score}'

        if pl_score>9 and pc_score<=9:

            score_label.place_forget()
            score_label.place(relx=0.443, rely=0.17)

        if pl_score>9 and pc_score>9:

            score_label.place_forget()
            score_label.place(relx=0.44, rely=0.17)

        if pl_score==gm or pc_score==gm:

            game_over(pl_score, pc_score)


    def game_scissors(): 
        
        nonlocal pl_score, pc_score, pl_pick, pc_pick

        pl_pick = 0
        pl_image.configure(image=pl_scissors)
        pl_image.image=pl_scissors
        pc_pick = random.randint(0, 2)
                
        if pc_pick==2:

            pc_image.configure(image=pc_scissors)
            pc_image.image=pc_scissors
            result_label['text']='Game tied'

        elif pc_pick==0:

            pc_image.configure(image=pc_rock)
            pc_image.image=pc_rock
            result_label['text']='You lost!'
            pc_score+=1

        else:

            pc_image.configure(image=pc_paper)
            pc_image.image=pc_paper
            result_label['text']='You won!'
            pl_score+=1

        score_label['text'] = f'{pl_score} : {pc_score}'

        if pl_score>9 and pc_score<=9:

            score_label.place_forget()
            score_label.place(relx=0.443, rely=0.17)

        if pl_score>9 and pc_score>9:

            score_label.place_forget()
            score_label.place(relx=0.44, rely=0.17)

        if pl_score==gm or pc_score==gm:

            game_over(pl_score, pc_score)


    rock_button['command'] = lambda: game_rock()
    paper_button['command'] = lambda: game_paper()
    scissors_button['command'] = lambda: game_scissors()
    close_button['command'] = lambda: close_game()
    playagain_button['command'] = lambda: play_again()
    back_button['command'] = lambda: close_game()

new_game['command'] = lambda: menu_start()


root.mainloop()