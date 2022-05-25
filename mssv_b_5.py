import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mssv_b_4
import mssv_b_3

def initGUI():
    def checkDeCode(str=""):
        n=mssv_b_3.decode_morse(str)
        for i in n:
            if i=="#":
                return False
        return True
    def save():
        if v.get()==1:
            rs=mssv_b_4.wEncode(entry1.get())
            if rs==True:
                messagebox.showinfo(message="Da ghi thong tin encode")
            else:
                messagebox.showerror(title="that bai",message="Sai thong tin hoac du lieu khong hop le")
        if v.get()==2:

            if checkDeCode(entry1.get())==True:
                mssv_b_4.wDecode(entry1.get())
                messagebox.showinfo(message="Da ghi thong tin Decode")
            else:
                messagebox.showerror(title="that bai",message="Sai thong tin hoac du lieu khong hop le")
    def clear():
        filePath.set("text.txt")
        v.set(1)

    def quit():
        exit()

    main = Tk()
    main.title("MSSV - Thực hành Python - Nhóm 3")
    canvas1 = tk.Canvas(main, width=400, height=200)
    canvas1.pack()

    label1 = tk.Label(main, text='Encode/Decode Morse')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(220, 25, window=label1)

    labelFilePath = tk.Label(main, text='Type Path File:')
    labelFilePath.config(font=('helvetica', 10))
    canvas1.create_window(100, 80, window=labelFilePath)

    filePath = tk.StringVar()
    filePath.set("text.txt")
    entry1 = tk.Entry(main, width=30, textvariable=filePath)
    canvas1.create_window(280, 80, window=entry1)

    v = tk.IntVar()
    v.set(1)
    radioEncode = tk.Radiobutton(main, width=40, text="Encode", variable=v, value=1)
    radioDecode = tk.Radiobutton(main, width=40, text="Decode", variable=v, value=2)
    canvas1.create_window(220, 120, window=radioEncode)
    canvas1.create_window(220, 140, window=radioDecode)

    buttonSave = tk.Button(text='Save', width=10, command=save)
    canvas1.create_window(100, 180, window=buttonSave)

    buttonClear = tk.Button(text='Clear', width=10, command=clear)
    canvas1.create_window(200, 180, window=buttonClear)

    buttonQuit = tk.Button(text='Quit', width=10, command=quit)
    canvas1.create_window(300, 180, window=buttonQuit)

    main.mainloop()

initGUI()
