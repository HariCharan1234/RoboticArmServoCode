#importing tkinter and initialising the window
import tkinter as tk
import RoboticArmController as rac
import time as tm

#conn = 0
conn = rac.connect(ip) #fill in the IP Adress of the host (microcontroller for the arm)

cp = tk.Tk()

#Setting the Label widgets in the window
tk.Label(cp, text = "Outer Arm Angle").grid(row = 0, column = 0)
tk.Label(cp, text = "Inner Arm Angle").grid(row = 1, column = 0)

#Setting the Entry widgets in the window
oaa = tk.Entry(cp)
iaa = tk.Entry(cp)

oaa.insert(0, "90")
iaa.insert(0, "90")

oaa.grid(row = 0, column = 1)
iaa.grid(row = 1, column = 1)

def oaincrement():
    oang = int(oaa.get())
    oaa.delete(0, tk.END)
    oaa.insert(0, str(oang + 5))

def iaincrement():
    inang = int(iaa.get())
    iaa.delete(0, tk.END)
    iaa.insert(0, str(inang + 5))

def oadecrement():
    oang = int(oaa.get())
    oaa.delete(0, tk.END)
    oaa.insert(0, str(oang - 5))

def iadecrement():
    inang = int(iaa.get())
    iaa.delete(0, tk.END)
    iaa.insert(0, str(inang - 5))

def transmit():
    conn.commandang("up", int(oaa.get()))
    tm.sleep(0.02)
    conn.commandang("down", int(iaa.get()))

def eer():
    conn.eer()

def eee():
    conn.eee()

#Setting the button widgets in the window
ioaa = tk.Button(cp, text = "+", command = oaincrement)
doaa = tk.Button(cp, text = "-", command = oadecrement)
iiaa = tk.Button(cp, text = "+", command = iaincrement)
diaa = tk.Button(cp, text = "-", command = iadecrement)
EER = tk.Button(cp, text = "EER", command = eer)
EEE = tk.Button(cp, text = "EEE", command = eee)
angtran = tk.Button(cp, text = "Confirm", command = transmit)

ioaa.grid(row = 0, column = 2)
doaa.grid(row = 0, column = 3)
iiaa.grid(row = 1, column = 2)
diaa.grid(row = 1, column = 3)
EER.grid(row = 3, column = 0)
EEE.grid(row = 3, column = 3)
angtran.grid(row = 5, column = 1)

    
cp.mainloop()
