import tkinter as tk 
import random




WIDTH = 400
HEIGHT = 400
hauteur_case = HEIGHT // 9
largeur_case = WIDTH // 9


racine = tk.Tk()
racine.title("sudoku")

canvas = tk.Canvas(racine,bg="white",height=HEIGHT,width=WIDTH)


 


def grille():
    
   
    
    r = random.randint(1,3)                      
    t = random.randint(4,6)
    z = random.randint(7,9)
    
    
    matrice = [[random.randint(1,9)for i in range(9)]for j in range(9)]
    
   
    
    
    # creation de la grille
    
    for i in range(9):
        for j in range(9):
            
            
            
            carre = canvas.create_rectangle((i*largeur_case,j*hauteur_case),((i+1)*largeur_case,(j+1)*hauteur_case),outline="maroon1")
            
            if matrice[i][j] == 1:    
                canvas.create_text((i*largeur_case)+20,(j*hauteur_case)+20,text=matrice[i][j],fill="black")
                
            elif matrice[i][j] == 3:    
                canvas.create_text((i*largeur_case)+20,(j*hauteur_case)+20,text=matrice[i][j],fill="black")
                
            elif matrice[i][j] == 6:    
                canvas.create_text((i*largeur_case)+20,(j*hauteur_case)+20,text=matrice[i][j],fill="black")
                
            elif matrice[i][j] == 9:    
                canvas.create_text((i*largeur_case)+20,(j*hauteur_case)+20,text=matrice[i][j],fill="black")
                
            # epaisseur sur les lignes
            
            if (i*largeur_case) == largeur_case*3 and (j*hauteur_case) == hauteur_case * 3:
                
                canvas.create_line((0,hauteur_case*3),(WIDTH,hauteur_case*3),fill="maroon1",width=5)
                
            if (i*largeur_case) == largeur_case*6 and (j*hauteur_case) == hauteur_case * 6:
                
                canvas.create_line((0,hauteur_case*6),(WIDTH,hauteur_case*6),fill="maroon1",width=5)    
      
        
                
            # epaisseur sur les colonnes
            
            if (i*largeur_case) == largeur_case*3 and (j*hauteur_case) == hauteur_case * 3:
                
                canvas.create_line((largeur_case*3,0),(largeur_case*3,HEIGHT),fill="maroon1",width=5)
                
            if (i*largeur_case) == largeur_case*6 and (j*hauteur_case) == hauteur_case * 6:
                
                canvas.create_line((largeur_case*6,0),(largeur_case*6,HEIGHT),fill="maroon1",width=5)
                
          

                    




entry = tk.Entry(racine)
bouton_play = tk.Button(racine,text="START",font=("helvetica",10),width=10,relief="groove")



entry.grid(column=4,row=0)

bouton_play.grid(column=0,row=2,columnspan=10)
canvas.grid(column=1,row=0)


grille()


racine.mainloop()