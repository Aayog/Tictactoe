##Made by Aayog Koirala
from Tkinter import*
name = {}
def button(row,col,i):
    name[i] = Button(frame, text=" ", command = lambda:checker(name[i]) )
    name[i].grid(row = row, column = col,sticky = N+E+W+S )
def printWin(toPrint):
    label_1 = Label(frame, text = toPrint)
    label_1.grid(row=10,column =0,sticky = N+E+W+S)

    button_1 = Button(frame,text = "Play Again",command = lambda : new_game())
    button_1.grid(row=11,column=0,sticky = N+E+W+S)

    button_2 = Button(frame,text = "Quit",command = lambda: quit_1())
    button_2.grid(row=11,column=1,sticky = N+E+W+S)
def quit_1():
    root.destroy()
def new_game():
    root.destroy()
    main()
def checker(button):
    global user
    buttonX =button
    if user == "X" and buttonX['text'] == " ":
        buttonX['text'] = "X"
        user = user_reverse(user)
    elif  buttonX['text'] == " " and  user == "O":
        buttonX['text'] = "O"
        user = user_reverse(user)
    label_name = Label(root,text = user + "'s turn")
    label_name.grid(row = 0,column = 0)
    try:

        if (name[1]['text'] == 'X' and name[2]['text']== 'X' and name[3]['text']=='X') or  (name[4]['text'] == 'X' and name[5]['text']== 'X' and name[6]['text']=='X') or  (name[7]['text'] == 'X' and name[8]['text']== 'X' and name[9]['text']=='X') or  (name[1]['text'] == 'X' and name[4]['text']== 'X' and name[7]['text']=='X') or  (name[2]['text'] == 'X' and name[5]['text']== 'X' and name[8]['text']=='X') or  (name[3]['text'] == 'X' and name[6]['text']== 'X' and name[9]['text']=='X') or  (name[1]['text'] == 'X' and name[5]['text']== 'X' and name[9]['text']=='X') or  (name[3]['text'] == 'X' and name[5]['text']== 'X' and name[7]['text']=='X'):
            printWin("X wins!")
        if (name[1]['text'] == 'O' and name[2]['text']== 'O' and name[3]['text']=='O') or  (name[4]['text'] == 'O' and name[5]['text']== 'O' and name[6]['text']=='O') or  (name[7]['text'] == 'O' and name[8]['text']== 'O' and name[9]['text']=='O') or  (name[1]['text'] == 'O' and name[4]['text']== 'O' and name[7]['text']=='O') or  (name[2]['text'] == 'O' and name[5]['text']== 'O' and name[8]['text']=='O') or  (name[3]['text'] == 'O' and name[6]['text']== 'O' and name[9]['text']=='O') or  (name[1]['text'] == 'O' and name[5]['text']== 'O' and name[9]['text']=='O') or  (name[3]['text'] == 'O' and name[5]['text']== 'O' and name[7]['text']=='O'):
            printWin("O wins!")
        if name[1]['text'] != ' ' and  name[2]['text'] != ' ' and  name[3]['text'] != ' ' and  name[4]['text'] != ' ' and  name[5]['text'] != ' ' and  name[6]['text'] != ' ' and  name[7]['text'] != ' ' and  name[8]['text'] != ' ' and  name[9]['text'] != ' ':
            printWin("Draw!")
    except:
        pass
def sleep(t=2):
    time.sleep(t)
def user_reverse(usr):
    if usr == "X":
        return "O"
    return "X"
def main():
    global root, frame,button_1,user
    root = Tk()
    root.wm_title('TicTacToe')
    root.geometry('240x180')
    user = "X"
    label_name = Label(root,text = user + "'s turn")
    label_name.grid(row = 0,column = 0)
    frame = Frame(root)
    frame.grid(row = 1,column = 0)
    button_1 = ['button{}'.format(x) for x in range(1,10)]
    buttons = StringVar()
    r = c =0
    count=1
    for i in button_1:
        button(r,c,count)
        c += 1
        if c == 3:
            r+=1
            c = 0
        count +=1
    root.mainloop()
if __name__=="__main__":
    main()
