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
##################################################




gui = Tk(className='Currency Converter')

gui.geometry("300x300")



label_lari = Label(gui, text = "lari")
label_lari.pack()

label_dollar = Label(gui, text = "dollar")

gui.mainloop() 
