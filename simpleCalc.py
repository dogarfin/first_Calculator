#! /usr/bin/env python3

from tkinter import Tk, StringVar

class Calculator:
    def __init__(self, state):
        self.state = state

    def ac(self):
        self.state.set('')

    def state_num(self, num):
        self.state.set('%s%d' % (self.state.get(), num))

#Main Window Setup:
#Root setup
root = Tk()
root.title("Generic Calculator")

EnteredSetup = StringVar('')
calc = Calculator(EnteredSetup)

#Parent frame setup
mainframe = ttk.Frame(root, padding="8")
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Button setup
root.Button(mainframe, text="AC", command=calc.ac).grid(
        column=5, row=4)
root.Button(mainframe, text="1", command=lambda: calc.state_num(1)).grid(
        column=1, row=6)
root.Button(mainframe, text="0", command=lambda: calc.state_num(0)).grid(
        column=1, row=7)

#Label Setup:
root.Label(mainframe, textvariable=EnteredSetup).grid(
        column=1,row=1,columnspan=5)

root.mainloop()
