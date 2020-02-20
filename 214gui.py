import tkinter as tk

root = tk.Tk()
root.wm_geometry("150x200")
root.title("Authorization")

blue = tk.Canvas(height = 100, width = 100, background="blue")
blue.grid(row=0, column=0)

red = tk.Canvas(height = 100, width = 100, background="red")
red.grid(row=1, column=0)

green = tk.Canvas(height = 100, width = 50, background="green")
green.grid(row=0, column=1)

yellow = tk.Canvas(height = 100, width = 50, background="yellow")
yellow.grid(row=1, column=1)

root.mainloop()