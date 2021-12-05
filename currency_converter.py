from tkinter import *
from bs4 import BeautifulSoup
import requests

url ="https://halykbank.ge/en/individuals/currency"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

soup = doc.find_all("td")

dolar = soup[1].text
euro = soup[4].text
pound = soup[8].text


k = float(input("Lari: "))
print(float(dolar)*k)
print(float(euro)*k)
print(float(pound)*k)
#########################
gui = Tk(className='Currency Converter')

gui.geometry("300x300")

dolari = 3


def converter_doll(dolari, lari):
    dolari = dolari
    lari = lari
    return dolari * lari


lari_input = Entry(gui, width=20)
lari_input.pack()

dolari_text = Label(gui, text ="dolari ="+str(dolari))
dolari_text.pack()

answer = Label(gui, text="asnwer")
answer.pack()


def button_command():
    lari = lari_input.get()
    print(lari)
    converted = int(lari) * dolari
    answer.config(text=converted)

    return None


Button(gui, text="Convert", command=button_command).pack()

gui.mainloop()
