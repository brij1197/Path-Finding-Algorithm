from tkinter import messagebox
from tkinter import *

def _dialogBox(msg):
    window=Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    messagebox.showinfo('Info',msg)

    window.deiconify()
    window.destroy()
    window.quit()