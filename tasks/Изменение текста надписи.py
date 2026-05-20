import tkinter as tk

def changer():
    label.config(text="Текст изменен!")

window = tk.Tk()

window.geometry("400x300")

label = tk.Label(window, text="Текст")

button = tk.Button(window, text="Изменить текст", command=changer)

label.pack(pady=20)
button.pack(pady=10)

window.mainloop()