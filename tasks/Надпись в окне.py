import tkinter as tk

window = tk.Tk()

window.title("Пустое окно")

label = tk.Label(window, text="Добро пожаловать!")

label.pack(expand=True)

window.mainloop()