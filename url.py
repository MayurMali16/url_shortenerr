import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("URL SHORTENER")
root.configure(bg="#000")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)


def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)


Label(root, text="My Url Shortener", font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Genarate url shortener", command=urlshortener).pack(pady=8)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text="Copy Url", command=copyurl).pack(pady=5)

root.mainloop()


