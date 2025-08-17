import tkinter as tk
from random import choice

import tk

root = tk.Tk()
root.title('проверка интуиции')

numbers = (0,1,2,4,5,3,6,7,8,9,10)

def check_guess():
    try:
        user_input = int(entry.get())
        if user_input < 0 or user_input > 10:
            result.config(text = 'введите число от 0 до 10')
        else:
            computer_choice = choice(numbers)
            guess_label.config(text = f'компьютер выбрал {computer_choice}')

        if user_input == computer_choice:
            result.config(text = 'МОЛОДЕЦ УГАДАЛ! КОНЕЦ ИГРЫ.')
            entry.config(state = 'disable')
        else:
            result.config(text = 'попробуй еще раз')
    except ValueError:
        result.config(text = 'ошибка, введи целое число')

entry = tk.Entry(root, width=10) entry.pack(pady=10)

button = tk.Button(root, text='угадать', command=check_guess) button.pack(pady=5)

rezult_label = tk.Label(root,text='',font=('Arial',12))
rezult_label.pack(pady=10)

guess_label = tk.Label(root,text='',font=('Arial',12))
guess_label.pack(pady=10)

root.mainloop()










