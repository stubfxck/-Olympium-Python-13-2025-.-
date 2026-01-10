def func(name: str = "Гость") -> str:
    print(f"Привет, {name}!")

user_name = input("Введите ваше имя: ")

if user_name.strip() == "":
    func()
else:
    func(user_name)