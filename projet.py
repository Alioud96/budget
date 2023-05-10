import sqlite3
# # Creation de la base de donnees de budgetDB

conn = sqlite3.connect('budggetDB.db')
cur = conn.cursor()

conn.commit()

def create_depense():
    req="CREATE TABLE depense(id INTEGER PRIMARY KEY, montant numeric, categorie varchar)"
    cur.execute(req) 
    conn.commit()
create_depense()


def ajouter_depense():
    montant =int(input("veuiller donner votre montant svp "))
    categorie =input("veuiller donner votre type de categorie svp")
    
    req1="INSERT INTO depense(montant, categorie) Values (?,?)"
    cur.execute(req1,(montant, categorie))
    conn.commit() 
    
ajouter_depense() 


def table_revenu():
    req2="CREATE TABLE revenu(id INTEGER PRIMARY KEY, montant numeric, categorie varchar)"
    cur.execute(req2) 
    conn.commit()   
table_revenu()

def ajouter_revenu():
    montant =int(input("veuiller donner votre montant svp "))
    categorie =input("veuiller donner votre type de categorie svp ")
    
    req2="INSERT INTO revenu(montant,categorie) Values (?,?)"
    cur.execute(req2,(montant, categorie))
    conn.commit()

ajouter_revenu()

# calcul du depense total
montant =int(input("veuiller donner votre montant svp "))
categorie =input("veuiller donner votre type de categorie svp ")

# calcul de la somme des attributs des depenses
somme = montant + categorie

# affichage de la somme des depenses
print("La somme de", montant, "et", categorie, "est :", somme)


# calcul du revenu total
montant =int(input("veuiller donner votre montant svp "))
categorie =input("veuiller donner votre type de categorie svp ")

# calcul de la somme des attributs des revenus
somme = montant + categorie

# affichage de la somme des revenus
print("La somme de", montant, "et", categorie, "est :", somme)

# calcul de l'ecart
if total_depense < total_revenu:
    ecart = total_revenu-total_depense
    print("l'ecart entre les depenses et les  revenus est :"+str(ecart)+"fcfa")
elif total_revenu < total_depense:
    ecart = total_depense-total_revenu
    print("l'ecart entre les depenses est :"+str(ecart)+"fcfa")
else:
    print("pas d'ecart entre les depenses et les revenues")

# print("l'ecart entre vos depense et revenus est estimee a :" + str(ecart) + "fcfa")

conn.commit()






























































































































































# calcul du depense total
nourriture =int(input("veuiller donner la categorie de depense nourriture svp "))
transport =int(input("veuiller donner la categorie de depense de transport svp "))


total_depense = nourriture+transport

print("vous avez depensez au total:"+str(total_depense)+"fcfa")
if total_depense > 500000:
  print("Attention vous avez trop depensez ce mois !!!")
else:
 print("votre depense est a la normale")
  
# # valider les modifications

conn.commit()

# calcul du revenu total
categorie revenu =int(input("veuiller donner la categorie de votre revenu svp "))
business =int(input("veuiller donner le revenu de votre business svp "))

total_revenu = categorie revenu + business 

print("la somme de vos revenue est: " +str(total_revenu)+ "fcfa")

#condition sur la revenu

if total_revenu > total_depense:
 print("vous pouvez augmenter vos depenses stp!!")
else:
 print(" vous avez trop depenser cette fois ci !!!") 
conn.commit()

#Calcul de l'ecart
def ecart_budget():
  total_depense = float(input("réecrivez le solde de votre depense:"))
  total_revenu = float(input("réecrivez le solde de votre revenu:"))
  print(total_depense)
  print(total_revenu)
  ecart = total_revenu-total_depense
  print("l'ecart est:", ecart)
  return ecart
ecart_budget()

conn.commit()

# fermer la connexion

conn.close()

















