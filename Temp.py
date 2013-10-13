from Tkinter import *

root = Tk()
T = Text(root, height=2, width=30, bg='lightgrey', relief='flat')
T.insert(END, "Just a text Widget\nin two lines\n")
T.config(state=DISABLED) # forbid text edition
T.pack()
mainloop()
