# como criar uma janela?
import tkinter as tk

root = tk.Tk()       #root é a janela pai do app

root.title("Exemplo Tk")
root.configure(background="white")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("300x300+50+50")

# como exibir texto em um rótulo? Rótulos são 
# widgets mais básicos. Usados para exibir texto ou
# imagens ->

tk.Label(root, text="Estou aprendendo Tkinter.").pack()
tk.Label(root, text="- Ana Caroline").pack() 

# .pack é um metodo gerenciador de geometria usado 
# para empacotar ou colocar o widget na janela 
# atual 

# Display an image

image = tk.PhotoImage(file="/home/ana/codigos/Python/RAD/dc35faebb3d69c42d81fe341183a5b64.gif")
tk.Label(root, image=image).pack()


root.mainloop()