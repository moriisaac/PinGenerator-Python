import random
import tkinter as tk

def generate_pin():
    number = int(entry.get())
    trial = random.randint(0, 9999)

    while trial != number:
        trial = random.randint(0, 9999)
        result_label.config(text=str(trial))
        root.update()

    result_label.config(text="Your Pin is " + str(number))

root = tk.Tk()
root.title("Pin Generator")

entry = tk.Entry(root)
entry.pack()

generate_button = tk.Button(root, text="Generate Pin", command=generate_pin)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
