import sqlite3

# # Creation de la base de donnees de budgetDB

conn = sqlite3.connect('budggetDB.db')
cur = conn.cursor()

conn.commit()

def create_depense():
    req="CREATE TABLE depense(id INTEGER PRIMARY KEY, habillement numeric, loyer numeric, nourriture numeric, transport numeric)"
    cur.execute(req) 
    conn.commit()
create_depense()


def ajouter_depense():
    habillement =int(input("veuiller donner la depense de votre habillement svp "))
    loyer =int(input("veuiller donner la depense de votre loyer "))
    nourriture =int(input("veuiller donner la depense de votre nourriture "))
    transport =int(input("veuiller donner la depense de votre transport "))
    
    req1="INSERT INTO depense(habillement, loyer, nourriture, transport) Values (?,?,?,?)"
    cur.execute(req1,(habillement, loyer, nourriture, transport))
    conn.commit() 
    
ajouter_depense() 



def table_revenu():
    req2="CREATE TABLE revenu(id INTEGER PRIMARY KEY, salaire numeric, business numeric, pension numeric, allocation numeric, categorie)"
    cur.execute(req2) 
    conn.commit()
    
table_revenu()

def ajout_revenu(salaire, business, pension, allocation, categorie):
    salaire = 200000
    business = 3000
    pension = 2000
    allocation = 30000
    categorie = 1200
    conn.execute("INSERT INTO revenu (salaire, business, pension, allocation, categorie) \
                  VALUES (?, ?, ?, ?, ?)", (salaire, business, pension, allocation, categorie))
    conn.commit()

ajout_revenu(salaire=200000, business=3000, pension=2000, allocation=30000, categorie=1200)

 
# calcul du depense total

habillement = int(input("donner la depense de habillement"))
loyer= int(input("donner la depense du loyer"))
nourriture= int(input("donner la depense de la nourriture"))
transport=int(input("donner la depense pour le transport")) 

total_depense = habillement+loyer+nourriture+transport

print("vous avez depensez au total:"+str(total_depense)+"fcfa")
if total_depense > 500000:
  print("Attention vous avez trop depensez ce mois !!!")
else:
 print("votre depense est a la normale")
  
# # valider les modifications

conn.commit()

# calcul du revenu total

salaire = int(input("donner le revenu de votre salaire "))
business= int(input("donner le revenu de votre business "))
pension= int(input("donner le revenu de votre pension "))
allocation=int(input("donner le revenu de votre allocation "))
categorie=int(input("donner le revenu de votre categorie "))

total_revenu = salaire+business+pension+allocation+categorie

print("la somme de vos revenue est: " +str(total_revenu)+ "fcfa")

#condition sur la revenu

if total_revenu > total_depense:
 print("vous pouvez augmenter vos depenses stp!!")
else:
 print(" vous avez trop depenser cette fois ci !!!") 
conn.commit()


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

# fermer la connexion

conn.close()