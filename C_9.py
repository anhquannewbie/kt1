"""
Thông tin người dùng được nhập từ giao diện bao gồm:
Mã sinh viên
Mã lớp
Họ và tên

Hãy tạo giao diện dùng Tkinter nhập thông tin từ dữ liệu phía trên và 3 nút
Lưu: Lưu trữ thông tin từ thông tin nhập vào
Làm lại: Xóa các dữ liệu hiện có trên form
Thoát: Thoát chương trình
Dữ liệu khi bấm vào nút “Lưu” sẽ được lưu trữ vào tập tin data.json
"""

from tkinter import *


import json
import tkinter

app = Tk()
app.title('User')

IdStudent = tkinter.StringVar()
IdClass = tkinter.StringVar()
name = tkinter.StringVar()


# label cua app

idStudent = Label(app, text = 'Ma sinh vien ')
idStudent.grid(column=0, row=0)

idClass = Label(app, text = 'Ma lop ')
idClass.grid(column=0, row=1)

Name = Label(app, text = "Ho va Ten: ")
Name.grid(column=0, row=2)

# nhap xuat thong tin 
input_idStudent = Entry(app, textvariable=IdStudent)
input_idStudent.grid(column=1, row=0)

input_idClass = Entry(app, textvariable=IdClass)
input_idClass.grid(column=1, row=1)

input_Name = Entry(app, textvariable=name)
input_Name.grid(column=1, row=2)

# Button 


data = []
def ExitApp():
    quit()

def Reset():
    IdClass.set("")
    IdStudent.set("")
    name.set("")

name_file = 'data.json'

with open(name_file, 'r') as rf:
    data = json.load(rf)
print(data)

def Save():

    data.append({
        'id': IdStudent.get(),
        'idclass': IdClass.get(),
        'name': name.get()
    })
    with open(name_file, 'w') as wf:
        json.dump(data, wf)
    print(data)


save = Button(app, text = '  Save  ', command=Save)
save.grid(column=0, row=3)

reset = Button(app, text = 'Reset', command=Reset)
reset.grid(column=1, row=3)

exit = Button(app, text = '  Exit  ', command=ExitApp)
exit.grid(column=2, row=3)


app.mainloop()