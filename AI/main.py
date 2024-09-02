from tkinter import *
from PIL import ImageTk, Image
import record as rec

window=Tk()
window.title("Security Camera")
window.iconphoto(False, PhotoImage(file='cam.png'))
window.geometry("500x500")

mainFrame = Frame(window, width=500, height=500)

label_title = Label(mainFrame, text="Security Camera", font=("Arial", 20))
label_title.grid(pady=(10,10), column=2)

icon1=Image.open("cam.png")
icon1=icon1.resize((100,100), Image.LANCZOS)
icon1=ImageTk.PhotoImage(icon1)
label_icon1 = Label(mainFrame, image=icon1)
label_icon1.grid(pady=(10,10), column=2)

btn1=Button(mainFrame, text="Start Live Video", font=("Arial", 20), width=20, height=2, command=rec.record)
btn1.grid(pady=(10,10), column=2)

btn2=Button(mainFrame, text="Exit", font=("Arial", 20), width=10, height=2, command=window.quit)
btn2.grid(pady=(10,10), column=2)


mainFrame.pack()
window.mainloop()
