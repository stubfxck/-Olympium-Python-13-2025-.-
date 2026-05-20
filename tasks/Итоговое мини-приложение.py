import tkinter as tk

def label_changer():
    name = entry.get()
    if name:
        label.config(text=f"Здравствуйте, {name}!")

window = tk.Tk()

window.geometry("400x300")

label = tk.Label(window, text="Введите ваше имя")
entry = tk.Entry(window, width=30)
button = tk.Button(window, text="Поздороваться", command=label_changer)

label.pack(pady=10)
entry.pack(pady=10)
button.pack(pady=20)

window.mainloop()