from tkinter import *
from bs4 import BeautifulSoup
import requests

url = "https://halykbank.ge/en/individuals/currency"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

soup = doc.find_all("td")

dolari = float(soup[2].text)
euro = float(soup[4].text)
pound = float(soup[8].text)

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
