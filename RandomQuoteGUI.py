import tkinter as tk
# import RandomCall as QuoteGenFunc
import RandomClient as RequestClientQuote

window = tk.Tk()
window.wm_title('Random Quote Generator')
# windowClient = RequestClientQuote()


def generate_random_quote():

    quote_generated = RequestClientQuote.get_quote()
    quote_output["text"] = quote_generated


quote_output = tk.Label(text='')


# random_quote_button = tk.Button(
#     text="Generate a Random Quote",
#     width=25,
#     height=5,
#     bg="black",
#     fg="yellow",
#     command=lambda: print(message))
random_quote_button = tk.Button(
    text="Generate a Random Quote",
    width=25,
    height=5,
    bg="black",
    fg="yellow",
    command=lambda: generate_random_quote())


random_quote_button.pack()
quote_output.pack()
window.mainloop()
