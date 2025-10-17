import tkinter as tk

root = tk.Tk()
root.title("Tkinter Label")
root.geometry("200x80")

label = tk.Label(root, text="Oi!", font=("Helvetica", 30))
label.pack(expand=True)