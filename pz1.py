import tkinter as tk

def on_button_click(message):
    label.config(text=message)

root = tk.Tk()
root.title("HMI-інтерфейс")

label = tk.Label(root, text="Натисніть кнопку", font=("Arial", 14))
label.pack(pady=10)

button1 = tk.Button(root, text="Кнопка 1", command=lambda: on_button_click("Ви натиснули кнопку 1"))
button1.pack(pady=5)

button2 = tk.Button(root, text="Кнопка 2", command=lambda: on_button_click("Ви натиснули кнопку 2"))
button2.pack(pady=5)

button3 = tk.Button(root, text="Кнопка 3", command=lambda: on_button_click("Ви натиснули кнопку 3"))
button3.pack(pady=5)

root.mainloop()
