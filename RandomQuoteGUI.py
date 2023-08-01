import tkinter as tk
import RandomCall as QuoteGenFunc

window = tk.Tk()
window.wm_title('Random Quote Generator')

def generate_random_quote(quote):
    quote_generated = QuoteGenFunc.generate_random_quote(quote)
    quote_output["text"] = quote_generated


quote_output = tk.Label(text='')


random_quote_button = tk.Button(
    text="Generate a Random Quote",
    width=25,
    height=5,
    bg="black",
    fg="yellow",
    command=lambda: generate_random_quote(''))


random_quote_button.pack()
quote_output.pack()
window.mainloop()
