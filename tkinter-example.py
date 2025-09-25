import tkinter as tk

counter = 0

root = tk.Tk()
root.title("Python TKinter Test App")
root.geometry("400x300")

label = tk.Label(root, text="Welcome")
# label.pack(pady=10)
label.grid()


def on_button_click():
    global counter
    counter = counter + 1
    label.config(text=f"Button was clicked: {counter} times")


button = tk.Button(root, text="Press Me", command=on_button_click)
# button.pack(pady=10)
button.grid(column=1, row=0)


def main():
    root.mainloop()


if __name__ == "__main__":
    main()
