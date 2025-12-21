import tkinter as tk

counter = 0

root = tk.Tk()
root.title("Python TKinter Test App")
root.geometry("600x400")

frame = tk.Frame(root)
frame.grid()

label = tk.Label(frame, text="Welcome", width=20).grid(column=0, row=0)


def on_button_click():
    global counter
    global label
    counter = counter + 1
    label.config(text=f"Button was clicked: {counter} times")


tk.Button(root, text="Click Me!", command=on_button_click, width=20).grid(
    column=1, row=0
)

tk.Button(root, text="Quit", command=root.destroy, width=20).grid(column=2, row=0)


def main():
    root.mainloop()


if __name__ == "__main__":
    main()
