import customtkinter as ctk
from tkinter import messagebox

root = ctk.CTk()
root.geometry("400x500")
root.title("Calculatrice")

affichage_count = []

affichage = ctk.CTkEntry(root, width=380, height=50, font=("Arial", 24))
affichage.pack(pady=20)

un = ctk.CTkButton(root, width=100, height=50, text="1", command=lambda: ajouter_chiffre("1"))
un.place(x=10, y=200)

deux = ctk.CTkButton(root, width=100, height=50, text="2", command=lambda: ajouter_chiffre("2"))
deux.place(x=111, y=200)

trois = ctk.CTkButton(root, width=100, height=50, text="3", command=lambda: ajouter_chiffre("3"))
trois.place(x=212, y=200)

retour = ctk.CTkButton(root, width=75, height=50, text="Retour", command=lambda: affichage.delete(0, ctk.END))
retour.place(x=313, y=200)

quatre = ctk.CTkButton(root, width=100, height=50, text="4", command=lambda: ajouter_chiffre("4"))
quatre.place(x=10, y=251)

cinq = ctk.CTkButton(root, width=100, height=50, text="5", command=lambda: ajouter_chiffre("5"))
cinq.place(x=111, y=251)

six = ctk.CTkButton(root, width=100, height=50, text="6", command=lambda: ajouter_chiffre("6"))
six.place(x=212, y=251)

x = ctk.CTkButton(root, width=75, height=50, text="X", command=lambda: ajouter_operation("X"))
x.place(x=313, y=251)

sept = ctk.CTkButton(root, width=100, height=50, text="7", command=lambda: ajouter_chiffre("7"))
sept.place(x=10, y=302)

huit = ctk.CTkButton(root, width=100, height=50, text="8", command=lambda: ajouter_chiffre("8"))
huit.place(x=111, y=302)

neuf = ctk.CTkButton(root, width=100, height=50, text="9", command=lambda: ajouter_chiffre("9"))
neuf.place(x=212, y=302)

diviser = ctk.CTkButton(root, width=75, height=50, text="/", command=lambda: ajouter_operation("/"))
diviser.place(x=313, y=302)

zero = ctk.CTkButton(root, width=100, height=50, text="0", command=lambda: ajouter_chiffre("0"))
zero.place(x=10, y=353)

virguyle = ctk.CTkButton(root, width=100, height=50, text=",", command=lambda: ajouter_chiffre(","))
virguyle.place(x=111, y=353)

plus = ctk.CTkButton(root, width=100, height=50, text="+", command=lambda: ajouter_operation("+"))
plus.place(x=212, y=353)

moins = ctk.CTkButton(root, width=75, height=50, text="-", command=lambda: ajouter_operation("-"))
moins.place(x=313, y=353)

egal = ctk.CTkButton(root, width=380, height=50, text="=", command=lambda: egal())
egal.place(x=10, y=404)



def ajouter_chiffre(chiffre):
    affichage.insert(ctk.END, chiffre)

def ajouter_operation(operation):
    affichage.insert(ctk.END, operation)

def egal():
    affichage_value = affichage.get()
    affichage_count.append(affichage_value)
    try:
        result = eval(affichage_value.replace("X", "*").replace(",", "."))
        affichage.delete(0, ctk.END)
        affichage.insert(ctk.END, str(result))
    except Exception as e:
        affichage.delete(0, ctk.END)
        affichage.insert(ctk.END, "Erreur")

root.mainloop()

