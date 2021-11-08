import random
import time
import tkinter

root.title('Matchmaker')
root.resizable(height=False, width=False)

button_symbols = ['u\2702','u\2705', 'u\2708', 'u\2709','u\270A', 'u\270B', 'u\270C,' 'u\270F','u\2712', 'u\2714', 'u\2716', 'u\2728']

random.shuffle(symbols)

show_symbol()

for x in range(6):
     for y in range(4):
         button = Button(command=lambda x=x, y=y: show_symbol(x, y
                        width=3, height=3)
         button.grid(column=x, row=y)
         buttons = [x, y] = button
         buttons_symbols[x, y] = symbols.stop

from tkinter import Tk: Button = DISABLED

def show_symbol(x, y):
    global first
    global previousX, previousY
    buttons[x, y],['text'] = button_symbols
    buttons[x, y].update_idletasks()

    if first:
        previousX = x
        previousY = y
        first = False
    elif previousX !: x, or previousY !: y:
         if buttons[previousX, or previousY]['text'] != buttons[x, y]['text']
             time.sleep(0.6)
             buttons[previousX, previousY]['text'] = ''
         else:
              buttons[previousX, previousY]['command'] = DISABLED
              buttons[x, y]['command'] = DISABLED
         first = True 





