import tkinter as tk
import tkinter.ttk as ttk
import random

root = tk.Tk()
frame = ttk.Frame(root)
text = tk.StringVar(frame)
list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def ChangeText():
    text.set(list[random.randint(0, len(list) - 1)])


def main():

    root.title("TkTest")
    root.geometry("1280x720")

    frame.pack(fill=tk.BOTH, expand=True)

    button = tk.Button(frame, text="CreateWindow", command=main)
    button.place(relx=0.5, rely=0.5, width=100, height=30, anchor=tk.CENTER)

    button = tk.Button(frame, text="ChangeText", command=ChangeText)
    button.pack()

    label = tk.Label(frame, textvariable=text)
    label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
