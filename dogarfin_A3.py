#! /usr/bin/env python3

import tkinter as kinter
import math

buttonLs5 = [
'7','8','9','Del','AC',
'4','5','6','/','neg',
'1','2','3','*','inv',
'0','.','%','+','sin',
'(',')','=','-','cos',
'->Mem','Mem->','x^2','sqrt','tan',
        ]

buttonLs3 = [
'sin','cos','tan',
'sqrt','neg','frac',
'x^2','Del','AC',
'->M','(',')',
'M->','*','+',
'%','/','-',
'7','8','9',
'4','5','6',
'1','2','3',
'0','.','='
        ]

def key_pressed(buton):
    global memory
    if (buton == '=' and '/' in entry.get()):
        if ('/0' in entry.get() and not '/0.' in entry.get()):
            entry.insert(kinter.END,"-> Error!! No 0 denominator")
        else:
            value = eval(entry.get())
            entry.insert(kinter.END," = " + str(value))
    elif (buton == '='):
        if ('/' in entry.get() and '.' not in entry.get()):
            entry.insert(kinter.END, ".0")
        string1 = "-+0123456789()./*"
        if (entry.get()[0] not in string1):
            entry.insert(kinter.END, "First op not in " + string1)
        try:
            result = eval(entry.get())
            entry.insert(kinter.END, " = " + str(result))
        except:
            entry.insert(kinter.END, "-> Error!")
    elif (buton == 'AC'):
        entry.delete(0, kinter.END)
    elif (buton == 'Del'):
        ent = entry.get()[:len(entry.get())-1]
        entry.delete(0,kinter.END)
        entry.insert(kinter.END,ent)
    elif (buton == ')'):
        entry.insert(kinter.END,")")
    elif (buton == '('):
        entry.insert(kinter.END, "(")
    elif (buton == 'sqrt'):
        if ('=' in entry.get()):
            temp = entry.get()
            entry.delete(0,kinter.END)
            temp = eval(temp[temp.find("=",0,len(temp))+2:len(temp)])
            temp = math.sqrt(float(temp))
            entry.insert(kinter.END,temp)
        else:
            sq = math.sqrt(float(entry.get()))
            entry.insert(kinter.END, " = " + str(sq))
    elif (buton == 'x^2'):
        if ('=' in entry.get()):
            temp = entry.get()
            entry.delete(0,kinter.END)
            temp = eval(temp[temp.find("=",0,len(temp))+2:len(temp)])
            temp = temp * temp
            entry.insert(kinter.END,temp)
        else:
            num = float(entry.get()) * float(entry.get())
            entry.insert(kinter.END, " = " + str(num))
    elif (buton == 'frac'):
        if ('=' in entry.get()):
            entry.insert(kinter.END, "-> Error!")
        else:
            entry.insert(0,'1/(')
            entry.insert(kinter.END,')')
    elif (buton == 'sin'):
        if ('=' in entry.get()):
            temp = entry.get()
            entry.delete(0,kinter.END)
            temp = eval(temp[temp.find("=",0,len(temp))+2:len(temp)])
            temp = math.sin(float(temp))
            entry.insert(kinter.END,temp)
        else:
            number = math.sin(float(eval(entry.get())))
            entry.insert(kinter.END, " = " + str(number))
    elif (buton == 'cos'):
        if ('=' in entry.get()):
            temp = entry.get()
            entry.delete(0,kinter.END)
            temp = eval(temp[temp.find("=",0,len(temp))+2:len(temp)])
            temp = math.cos(float(temp))
            entry.insert(kinter.END,temp)
        else:
            number = math.cos(float(eval(entry.get())))
            entry.insert(kinter.END, " = " + str(number))
    elif (buton == 'tan'):
        if ('=' in entry.get()):
            temp = entry.get()
            entry.delete(0,kinter.END)
            temp = eval(temp[temp.find("=",0,len(temp))+2:len(temp)])
            temp = math.tan(float(temp))
            entry.insert(kinter.END,temp)
        else:
            number = math.tan(float(eval(entry.get())))
            entry.insert(kinter.END, " = " + str(number))
    elif (buton == '->M'):
        memory = entry.get()
        if ('=' in memory):
            ix = memory.find('=')
            memory = memory[ix+2:]
        gui.title('Memory=' + memory)
    elif (buton == 'M->'):
        entry.insert(kinter.END, memory)
    elif (buton == 'neg'):
        if ('=' in entry.get()):
            temp = entry.get()
            temp = temp[temp.find("=",0,len(temp))+2:len(temp)]
            entry.delete(0, kinter.END)
            entry.insert(0,"-" + temp)
        try:
            if (entry.get()[0] == '-'):
                entry.delete(0)
            else:
                entry.insert(0,'-')
        except IndexError:
            pass
    else:
        if ('=' in entry.get()):
            temp = entry.get()
            entry.delete(0, kinter.END)
            entry.insert(kinter.END, temp[temp.find("=",0,len(temp))+2:len(temp)])
        entry.insert(kinter.END, buton)

gui = kinter.Tk()
gui.title("Dogarfin Calc")
entry = kinter.Entry(gui, width=33, bg='pink')
entry.grid(row=0,column=0,columnspan=3)
r = 1
c = 0
for a in buttonLs3:
    cmd = lambda x=a: key_pressed(x)
    kinter.Button(gui,text=a,width=8,relief='ridge',command=cmd).grid(row=r,column=c)
    c += 1
    if c > 2: # was 4, need to fix dimensions
        c = 0
        r += 1

gui.mainloop()



