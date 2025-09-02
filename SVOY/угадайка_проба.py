import tkinter as tk
from tkinter import messagebox, END
from random import choice

from pygame.event import clear


# Функция для проверки интуиции
def check_guess():
    try:
        user_input = int(entry.get())
        if user_input not in s:
            messagebox.showinfo("Информация", "Выход за пределы допустимых значений!")
            return
        if 0 <= user_input <= 10:
            w = choice(s)
            label_result.config(text=f"Случайное число: {w}")
            if w == user_input:
                messagebox.showinfo("Поздравляем!", "КРАСАВЧЕГ УГАДАЛ!!! Конец игры.")
                root.quit()  # Закрываем приложение
            elif w != user_input:
                w = entry.delete(0,last=None)
        else:
            messagebox.showinfo("СДАЛСЯ!!", "КОНЕЦ ИГРЫ")
            root.quit()  # Закрываем приложение
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целое число от 0 до 10.")


# Создаем главное окно
root = tk.Tk()
root.title("Проверь свою интуицию")
root.geometry("400x200")
# Настраиваем элементы интерфейса
label_instruction = tk.Label(root, text="Введите цифру от 0 до 10:")
label_instruction.pack()

entry = tk.Entry(root)
entry.pack()

button_check = tk.Button(
    root, text="Small Button", command=check_guess, width=20, height=5
)
button_check.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack()

# Список возможных чисел
s = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Запускаем главный цикл приложения
root.mainloop()

"""Как это работает:
Импортируем библиотеки:

tkinter для создания графического интерфейса.
messagebox для отображения сообщений пользователю.
choice из модуля random для выбора случайного числа.
Создаем главное окно:

Устанавливаем заголовок окна.
Добавляем элементы интерфейса:

Метка для инструкции.
Поле ввода для ввода числа.
Кнопка для проверки введенного числа.
Метка для отображения результата.
Функция check_guess:

Проверяет введенное число.
Если число в пределах от 0 до 10, выбирает случайное число и сравнивает его с введенным.
Отображает сообщения о результате.
Запускаем главный цикл приложения:

root.mainloop() удерживает окно открытым.
Как использовать:
Скопируйте код в файл с расширением .py (например, intuition_game.py).
Запустите файл из командной строки: python intuition_game.py.
Вводите числа в графическом интерфейсе и проверяйте свою интуицию!"""

