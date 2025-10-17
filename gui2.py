import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Widgets Demo")
root.configure(background="pink")

widgets = [
    tk.Label,    # apenas um rótulo, não interativo
    tk.Checkbutton, # Uma caixa de seleção
    ttk.Combobox, # uma caixa de listagem suspensa
    tk.Entry,   # digite uma linha de texto
    tk.Button,  # Um botão
    tk.Radiobutton, #um conjunto de alternância, comapenas um item ativo
    tk.Scale,   # um controle deslizante
    tk.Spinbox, # um girador inteiro
]

for widget in widgets:
    try:
        widget = widget(root, text=widget.__name__)
    except tk.TclError:
        widget = widget(root)
    widget.pack(padx=5, pady=5, fill="x")





root.mainloop()