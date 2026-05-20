import tkinter as tk

def hello_or_bye(x=None):
    if x == 1:
        print("Привет!")
    else:
        print("Пока!")


window = tk.Tk()

window.geometry("400x100")
buttons = [
    tk.Button(window, text="Привет", command=lambda: hello_or_bye(1)),
    tk.Button(window, text="Пока", command=hello_or_bye)
]

for button in buttons:
    button.pack(pady=10)

window.mainloop()