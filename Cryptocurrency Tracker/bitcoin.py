from tkinter import font
from typing import ChainMap
import tkinter as tk
from datetime import datetime, time

import requests

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text = str(price) + " $")
    labelTime.config(text = "Updated: " + time)

    canvas.after(1000, trackBitcoin)

canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Bitcoin Price Tracker")

f1 = ("raleway", 24, "bold")
f2 = ("raleway", 22, "bold")
f3 = ("raleway", 18, "normal")

label = tk.Label(canvas, text = "Bitcoin Price", font = f1)
label.pack(pady = 20)

labelPrice = tk.Label(canvas, font = f2)
labelPrice.pack(pady = 20)

labelTime = tk.Label(canvas, font = f3)
labelTime.pack(pady = 20)

trackBitcoin()

canvas.mainloop()


