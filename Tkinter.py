from tkinter import*

def was_clicked():
    print("a button was clicked.")
def change_to_blue():
    root.configure(bg=azul)

def change_to_red():
    root.configure(bg=vermelho)

def change_to_green():
    root.configure(bg=verde)

def change_to_black():
    root.configure(bg=preto)
azul= "#0087ff"
vermelho= "#ff0000"
verde= "#00ff00"
preto= "#000000"

root = Tk()
root.title("Janela")
root.geometry("500x300+200+200")
root.wm_resizable(width=False, height=False)

button1 = Button(root, text="azul", command= change_to_blue, font="Time 20 bold")
button1.place(width=80, height=30, x=0, y=0)
button2 = Button(root, text="vermelho", command= change_to_red, font="Time 20 bold")
button2.place(width=80, height=30, x=500-80, y=0)
button3 = Button(root, text="verde", command= change_to_green, font="Time 20 bold")
button3.place(width=80, height=30, x=0, y=300-30)
button4 = Button(root, text="preto", command= change_to_black, font="Time 20 bold")
button4.place(width=80, height=30, x=500-80, y=300-30)

root.mainloop()