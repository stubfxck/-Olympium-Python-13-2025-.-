import tkinter as tk

def say_hello():
    name = entry.get()

    if name:
        print(f"Привет, {name}!")
    else:
        print("Привет, гость!")

window = tk.Tk()

window.geometry("400x300")

label = tk.Label(window, text="Введите имя:")
entry = tk.Entry(window, width=30)
button = tk.Button(window, text="Поздороваться", command=say_hello)

label.pack(pady=10)
entry.pack(pady=5)
button.pack(pady=10)

window.mainloop()