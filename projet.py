
import sqlite3

# # Creation de la base de donnees de budgetDB

conn = sqlite3.connect('budggetDB.db')
cur = conn.cursor()

conn.commit()


# Création de la table "depenses"
conn.execute('''CREATE TABLE depenses
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             categorie_depense numeric,
             nourriture numeric,
             transport);''')
                         
             
 # Insertion de données dans la table "depenses"
conn.execute("INSERT INTO depenses (categorie_depense) VALUES ('nourriture')")
conn.execute("INSERT INTO depenses (categorie_depense) VALUES ('transport')")

# Enregistrement des modifications
conn.commit()

# Exécution d'une requête pour récupérer les données insérées
cursor = conn.execute("SELECT id, categorie_depense FROM depenses")
for row in cursor:
    print(f"id = {row[0]}, categorie_depense = {row[1]}")

# Fermeture de la connexion à la base de données
conn.close()

def table_revenu():
    req2="CREATE TABLE revenu(id INTEGER PRIMARY KEY, categorie revenu, business numeric )"
    cur.execute(req2) 
    conn.commit()
    
table_revenu()


def ajouter_revenu():
    categorie revenu =int(input("veuiller donner la categorie de votre revenu svp "))
    business =int(input("veuiller donner le revenu de votre business svp "))
    
    req2="INSERT INTO revenu(categorie revenu,bussiness) Values (?,?)"
    cur.execute(req2,(categorie revenu,business))
    conn.commit() 
    
ajouter_categorie() 


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

















