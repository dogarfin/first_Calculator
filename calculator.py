#! /usr/bin/env python3

import tkinter as tk

def click(key):
    global memory
    if key == '=':
        if '/' in entry.get() and '.' not in entry.get():
            entry.insert(tk.END, ".0")
        string1 = "-+0123456789."
        if entry.get()[0] not in string1:
            entry.insert(tk.END, "First char not in " + string1)
        try:
            result = eval(entry.get())
            entry.insert(tk.END, " = " + str(result))
        except:
            entry.insert(tk.END, "--> Error!")
    elif key == 'C':
        entry.delete(0, tk.END)
    elif key == '->M':
        memory = entry.get()
        if '=' in memory:
            ix = memory.find('=')
            memory = memory[ix+2:]
        root.title('M=' + memory)
    elif key == 'M->':
        entry.insert(tk.END, memory)
    elif key == 'neg':
        if '=' in entry.get():
            entry.delete(0, tk.END)
        try:
            if entry.get()[0] == '-':
                entry.delete(0)
            else:
                entry.insert(0,'-')
        except IndexError:
            pass
    else:
        if '=' in entry.get():
            entry.delete(0, tk.END)
        entry.insert(tk.END, key)

root = tk.Tk()
root.title("Calculator")

btn_list = [
'7','8','9','*','C',
'4','5','6','/','M->',
'1','2','3','-','->M',
'0','.','=','+','neg']

r = 1
c = 0
for b in btn_list:
    rel = 'ridge'
    cmd = lambda x=b: click(x)
    tk.Button(root,text=b,width=5,relief=rel,command=cmd).grid(row=r,column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

entry = tk.Entry(root, width=33, bg='yellow')
entry.grid(row=0,column=0,columnspan=5)

root.mainloop()



