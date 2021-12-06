from tkinter import *
from bs4 import BeautifulSoup
import requests

url = "https://www.tbcbank.ge/web/en/exchange-rates"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

soup = doc.find_all("div",{"class","currRate"})

dolari = float(soup[1].text)
euro = float(soup[3].text)
pound = float(soup[5].text)

gui = Tk(className='CURRENCY')
gui.geometry("250x150")
gui.option_add('*Font', 'monospace')
gui.configure(bg='#01c26e')
gui.resizable(False, False)

lari_input = Entry(gui, width=5)
lari_input.pack()

dolari_text = Label(gui, text="USD = " + str(dolari))
dolari_text.pack()

answer = Label(gui, text="0.00")
answer.pack()


def button_command():
    lari = lari_input.get()
    converted = float(lari) / dolari
    answer.config(text=round(converted, 2))

    return None


Button(gui, text="Convert", command=button_command).pack()

gui.mainloop()
