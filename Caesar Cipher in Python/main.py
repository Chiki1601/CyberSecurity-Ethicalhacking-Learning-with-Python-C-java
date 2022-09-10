from tkinter import *
import tkinter as tk
# Create an instance of tkinter frame or window
window=Tk()
# Set the size of the tkinter windowdow
window.geometry("700x350")
window.title("Pooja Patel")#give title to the window
Label(window, text="Message Encryption Decryption",bg='dark blue',fg='white', font=('Calibri 15')).pack()# a lable
text=tk.StringVar()
key=tk.IntVar()
alphabets="abcdefghijklmnopqrstuvwxyz"

def encryption():
    t=text.get()
    k=key.get()
    en=""   

    for letter in t:
        new_position=(alphabets.find(letter)+k)%len(alphabets)
        en+=alphabets[new_position]

    Label(window,text="Encryption is:",font=('Calibri 12')).pack()
    Label(window,text=en,font=('Calibri 12'),bg='red').pack()

def decryption():
    t=text.get()
    k=key.get()
    de=""   

    for letter in t:
        new_position=(alphabets.find(letter)-k)%len(alphabets)
        de+=alphabets[new_position]

    Label(window,text="Decryption is:",font=('Calibri 12')).pack()
    Label(window,text=de,font=('Calibri 12'),bg='red').pack()

Label(window, text="Enter the letter to be encrypted:", font=('Calibri 12')).pack()# a lable
Entry(window,textvariable=text).pack()
Label(window, text="Enter the key:", font=('Calibri 12')).pack()# a lable
Entry(window,textvariable=key).pack()

Button(window,text="ENCRYPT",bg='pink',command=encryption).pack()
Button(window,text="DECRYPT",bg='pink',command=decryption).pack()

window.mainloop()
