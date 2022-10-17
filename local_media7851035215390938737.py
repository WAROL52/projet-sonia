from tkinter import *

window = Tk()
window.title("Calcul de la masse des ingrédients")
window .geometry( '450x400' )

label = Label(window, text="Masse de la crème :", font = ( "Arial Bold" , 15 ))
label.grid(column=0, row=0)

label2 = Label(window, font = ( "Arial Bold" , 15 ))
label2.grid(column=0, row=4)

label3 = Label(window, text="", font = ( "Arial Bold" , 15 ))
label3.grid(column=0, row=5)

label4 = Label(window, text="", font = ( "Arial Bold" , 15 ))
label4.grid(column=0, row=6)

label5 = Label(window, text="", font = ( "Arial Bold" , 15 ))
label5.grid(column=0, row=7)

label6 = Label(window, text="", font = ( "Arial Bold" , 15 ))
label6.grid(column=0, row=8)

label7 = Label(window, text="", font = ( "Arial Bold" , 15 ))
label7.grid(column=0, row=9)

label8 = Label(window, text="", font = ( "Arial Bold" , 15 ))
label8.grid(column=0, row=10)

label9 = Label(window, text="", font = ( "Arial Bold" , 15 ))
label9.grid(column=0, row=11)

label10 = Label(window, text="", font = ( "Arial Bold" , 15 ))
label10.grid(column=0, row=12)

saisie = Entry(window, width=10, bg='grey')
saisie.grid(column=1, row=0)

def click():
    masse_creme = float(saisie.get())
    masse_eau_distille = (masse_creme*58)/100   
    masse_beurre_cacao = (masse_creme*20)/100
    masse_huile_cactus = (masse_creme*6)/100
    masse_cire_emulsifiante = (masse_creme*5.5)/100
    masse_glycerine = (masse_creme*4)/100
    masse_vitamineE = (masse_creme*0.32)/100
    masse_cosgard = (masse_creme*0.6)/100 
    masse_arome_cacao = (masse_creme*2.5)/100 
    masse_acide_citrique = (masse_creme*0.04)/100 
    resultat = [ masse_eau_distille,masse_beurre_cacao] 
    label2.configure(text=("masse_eau_distille:",masse_eau_distille))
    label3.configure(text=("masse_beurre_cacao:",masse_beurre_cacao))
    label4.configure(text=("masse_huile_cactus:",masse_huile_cactus))
    label5.configure(text=("masse_cire_emulsifiante:",masse_cire_emulsifiante))
    label6.configure(text=("masse_glycerine:",masse_glycerine))
    label7.configure(text=("masse_vitamineE:",masse_vitamineE))
    label8.configure(text=("masse_cosgard:",masse_cosgard))
    label9.configure(text=("masse_arome_cacao:",masse_arome_cacao))
    label10.configure(text=("masse_acide_citrique:",masse_acide_citrique))
saisie.focus()

bouton = Button( window , text = "Calculer", command=click )
bouton.grid(column=0, row=1)


window.mainloop()