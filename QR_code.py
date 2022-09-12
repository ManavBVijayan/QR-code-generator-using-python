from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
root=Tk()
def gen():
    link_name=name_entry.get()
    link=link_entry.get()
    file_name=link_name + '.png'
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,450,window=image_label)


canvas=Canvas(root,width=400,height=600 )
canvas.pack()
can_label=Label(root,text='OR CODE GENERATOR',fg='black',font=('Arial',20))
canvas.create_window(200,50,window=can_label)

name_label=Label(root,text='Link name')
link_label=Label(root,text='Link')
canvas.create_window(200,100,window=name_label)
canvas.create_window(200,160,window=link_label)

name_entry=Entry(root)
link_entry=Entry(root)
canvas.create_window(200,120,window=name_entry)
canvas.create_window(200,180,window=link_entry)

button=Button(text='Generate QR code',command=gen)
canvas.create_window(200,220,window=button)

root.mainloop()


