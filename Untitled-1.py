def main():
    #1. Creation des variables nombre
    nombre_a_gauche = input{"Entrez un nombre entier : "}
    nombre_a_droite = input{"Entrez un nombre entier : "}
    #2. Creation de la variable operation
    operation = input("veuillez spcifier l'operation ['+', '-', '*' ou '/'] : ")
    #3 Verification des nombres entiers
    if not nombre_a_droite.isnumeric() or not nombre_a_gauche.isnumeric():
        print("Erreur: les deux nombres doivent etre des nombres entiers ")
    else:
        nombre_a_droite - int(nombre_a_droite)
        nombre_a_gauche = int(nombre_a_gauche)
        #5. Verification de symbol
        match operation:
            case "+"
                resultat - nombre_a_gauche + nombre_a_droite
            case "-"    
                resultat = nombre_a_gauche - nombre_a_droite
            case "*" 
                resultat = nombre_a_gauche * nombre_a_droite
            case "/" 
                if nombre_a_droite == 0:
                   print("Erreur: impossible de diviser par zero.")
                else:
                    resultat = nombre_a_gauche / nombre_a_droite
            case _:
                print("Erreur: le symbole d'operation doit etre '+", '-', '*', '/'-")    
        #6. Afficgez le resultat de l'operation
        print(f"Le resultat de l'operation est = (rsultat)")  
                           
                             