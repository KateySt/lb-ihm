import tkinter as tk

# Функція для обробки натискання кнопки
def on_button_click(message):
    label.config(text=message)

# Створення основного вікна
root = tk.Tk()
root.title("HMI-інтерфейс")

# Створення мітки
label = tk.Label(root, text="Натисніть кнопку", font=("Arial", 14))
label.pack(pady=10)

# Створення кнопок
button1 = tk.Button(root, text="Кнопка 1", command=lambda: on_button_click("Ви натиснули кнопку 1"))
button1.pack(pady=5)

button2 = tk.Button(root, text="Кнопка 2", command=lambda: on_button_click("Ви натиснули кнопку 2"))
button2.pack(pady=5)

button3 = tk.Button(root, text="Кнопка 3", command=lambda: on_button_click("Ви натиснули кнопку 3"))
button3.pack(pady=5)

# Запуск головного циклу
root.mainloop()
