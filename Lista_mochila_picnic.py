from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("500x500")

label1 = Label(root)
label2 = Label(root)

List1 = ["Botella","lonchera","tarjeta de identificación","chocolates","chips","boletos","pañuelo"]
label1["text"] = "Elementos_de_la_lista:  " + str(List1)

def bag_contents():
    
    random_list = random.sample(range(0,7),1)
    label2["text"] = "Colocar elemento número " + str(random_list) + "  en la mochila"
    
      
label1.place(relx=0.5,rely = 0.4, anchor = CENTER)

btn = Button(root, text="¿Qué elemento poner en la mochila?",command = bag_contents,bg="orange",fg="white")
btn.place(relx=0.5,rely = 0.5, anchor = CENTER)
    

label2.place(relx=0.5,rely = 0.6, anchor = CENTER)


root.mainloop()
