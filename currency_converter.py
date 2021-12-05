from tkinter import *

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
