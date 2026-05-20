import tkinter as tk

window = tk.Tk()

window.geometry("400x300")

button1 = tk.Button(window, text="Нажмите здесь")
button1.pack(expand=True)

window.title("Окно")

window.mainloop()