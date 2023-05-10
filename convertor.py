import tkinter as tk
from tkinter import messagebox
import requests

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        response = requests.get(url)
        data = response.json()

        conversion_rate = data['rates'][to_currency]

        converted_amount = amount * conversion_rate

        result_label.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}")

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Failed to connect to the currency conversion API.")

window = tk.Tk()
window.title("Currency Converter")

amount_label = tk.Label(window, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10)

amount_entry = tk.Entry(window)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_label = tk.Label(window, text="From Currency:")
from_currency_label.grid(row=1, column=0, padx=10, pady=10)

from_currency_var = tk.StringVar(window)
from_currency_var.set("USD")

from_currency_menu = tk.OptionMenu(window, from_currency_var, "USD", "EUR", "GBP", "INR")
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

to_currency_label = tk.Label(window, text="To Currency:")
to_currency_label.grid(row=2, column=0, padx=10, pady=10)

to_currency_var = tk.StringVar(window)
to_currency_var.set("EUR")

to_currency_menu = tk.OptionMenu(window, to_currency_var, "USD", "EUR", "GBP", "INR")
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
