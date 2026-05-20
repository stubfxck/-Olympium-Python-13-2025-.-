import tkinter as tk

def say_hello():
    print("Здравствуйте!!")

window = tk.Tk()

window.title("Окошк")

window.geometry("400x300")

button1 = tk.Button(window, text="Поздороваться", command=say_hello)
button1.pack(expand=True)

window.mainloop()