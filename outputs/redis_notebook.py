
# # Projet Redis 
# Fait par @ChloéTellier, @OcéaneGuitton, @FlavieThévenard et @AntoineLucas

import redis
import numpy
import scipy
import random
import pprint
import json
import pandas as pd
import seaborn as sns
import time


# ## Connexion

redis_host = "127.0.0.1"
redis_port = 6379

r = redis.Redis(host=redis_host, port=redis_port, db = 0)


# ## Création de notre base de données 

random.seed(444)

# Liste des attributs avec 2 modalités : les ingrédients

saumon = ['Oui', 'Non']
saumon_teriyaki = ['Oui', 'Non']
daurade = ['Oui', 'Non']
thon = ['Oui', 'Non']
crevette = ['Oui', 'Non']
poulet = ['Oui', 'Non']
thon_cuit = ['Oui', 'Non']
foie_gras = ['Oui', 'Non']
tofu = ['Oui', 'Non']
truite = ['Oui', 'Non']
hareng = ['Oui', 'Non']
poulpe = ['Oui', 'Non']
boeuf = ['Oui', 'Non']
chair_de_crabe = ['Oui', 'Non']
oeufs_de_saumon = ['Oui', 'Non']
avocat = ['Oui', 'Non']
fromage = ['Oui', 'Non']
oeuf = ['Oui', 'Non']
gingembre = ['Oui', 'Non']
wasabi = ['Oui', 'Non']
sauce_salee = ['Oui', 'Non']
sauce_sucree = ['Oui', 'Non']
sauce_sucreesalee = ['Oui', 'Non']
mayonnaise_classique = ['Oui', 'Non']
mayonnaise_teriyaki = ['Oui', 'Non']
mayonnaise_japonaise = ['Oui', 'Non']
mayonnaise_spicy = ['Oui', 'Non']
mayonnaise_ponzu = ['Oui', 'Non']
sauce_teriyaki = ['Oui', 'Non']
sauce_satay_aux_cacahuetes = ['Oui', 'Non']
sauce_epicee = ['Oui', 'Non']
mangue = ['Oui', 'Non']
carotte = ['Oui', 'Non']
anis = ['Oui', 'Non']
poivre_rose = ['Oui', 'Non']
cannelle = ['Oui', 'Non']
cardamome = ['Oui', 'Non']
curcuma = ['Oui', 'Non']
feve = ['Oui', 'Non']
edamame = ['Oui', 'Non']
macis = ['Oui', 'Non']
maniguette = ['Oui', 'Non']
paprika = ['Oui', 'Non']
piment = ['Oui', 'Non']
poivre = ['Oui', 'Non']
safran = ['Oui', 'Non']
sumac = ['Oui', 'Non']
persil = ['Oui', 'Non']
herbe_de_provence = ['Oui', 'Non']
sesame = ['Oui', 'Non']
feuilles_de_riz = ['Oui', 'Non']
menthe = ['Oui', 'Non']
coriandre = ['Oui', 'Non']
chou = ['Oui', 'Non']
ciboulette = ['Oui', 'Non']
pomme = ['Oui', 'Non']
celeri_rave = ['Oui', 'Non']
aneth = ['Oui', 'Non']
baies_roses = ['Oui', 'Non']
prune = ['Oui', 'Non']
betterave = ['Oui', 'Non']
noix_de_coco = ['Oui', 'Non']
citron_vert = ['Oui', 'Non']
citron_jaune = ['Oui', 'Non']
dattes = ['Oui', 'Non']
laitue = ['Oui', 'Non']
roquette = ['Oui', 'Non']
concombre = ['Oui', 'Non']
poivrons = ['Oui', 'Non']
asperge = ['Oui', 'Non']
oignons_crus = ['Oui', 'Non']
oignons_caramelises = ['Oui', 'Non']
oignons_frits = ['Oui', 'Non']

# 2**73 = 9.5*(10**21) combinaisons possibles de sushis

sushis = []

tps1 = time.perf_counter()

for i in range(0, 100000):
    saumon_choice = random.choice(saumon)
    saumon_teriyaki_choice = random.choice(saumon_teriyaki)
    daurade_choice = random.choice(daurade)
    thon_choice = random.choice(thon)
    crevette_choice = random.choice(crevette)
    poulet_choice = random.choice(poulet)
    thon_cuit_choice = random.choice(thon_cuit)
    foie_gras_choice = random.choice(foie_gras)
    tofu_choice = random.choice(tofu)
    truite_choice = random.choice(truite)
    hareng_choice = random.choice(hareng)
    poulpe_choice = random.choice(poulpe)
    boeuf_choice = random.choice(boeuf)
    chair_de_crabe_choice = random.choice(chair_de_crabe)
    oeufs_de_saumon_choice = random.choice(oeufs_de_saumon)
    avocat_choice = random.choice(avocat)
    fromage_choice = random.choice(fromage)
    oeuf_choice = random.choice(oeuf)
    gingembre_choice = random.choice(gingembre)
    wasabi_choice = random.choice(wasabi)
    sauce_salee_choice = random.choice(sauce_salee)
    sauce_sucree_choice = random.choice(sauce_sucree)
    sauce_sucreesalee_choice = random.choice(sauce_sucreesalee)
    mayonnaise_classique_choice = random.choice(mayonnaise_classique)
    mayonnaise_teriyaki_choice = random.choice(mayonnaise_teriyaki)
    mayonnaise_japonaise_choice = random.choice(mayonnaise_japonaise)
    mayonnaise_spicy_choice = random.choice(mayonnaise_spicy)
    mayonnaise_ponzu_choice = random.choice(mayonnaise_ponzu)
    sauce_teriyaki_choice = random.choice(sauce_teriyaki)
    sauce_satay_aux_cacahuetes_choice = random.choice(sauce_satay_aux_cacahuetes)
    sauce_epicee_choice = random.choice(sauce_epicee)
    mangue_choice = random.choice(mangue)
    carotte_choice = random.choice(carotte)
    anis_choice = random.choice(anis)
    poivre_rose_choice = random.choice(poivre_rose)
    cannelle_choice = random.choice(cannelle)
    cardamome_choice = random.choice(cardamome)
    curcuma_choice = random.choice(curcuma)
    feve_choice = random.choice(feve)
    edamame_choice = random.choice(edamame)
    macis_choice = random.choice(macis)
    maniguette_choice = random.choice(maniguette)
    paprika_choice = random.choice(paprika)
    piment_choice = random.choice(piment)
    poivre_choice = random.choice(poivre)
    safran_choice = random.choice(safran)
    sumac_choice = random.choice(sumac)
    persil_choice = random.choice(persil)
    herbe_de_provence_choice = random.choice(herbe_de_provence)
    sesame_choice = random.choice(sesame)
    feuilles_de_riz_choice = random.choice(feuilles_de_riz)
    menthe_choice = random.choice(menthe)
    coriandre_choice = random.choice(coriandre)
    chou_choice = random.choice(chou)
    ciboulette_choice = random.choice(ciboulette)
    pomme_choice = random.choice(pomme)
    celeri_rave_choice = random.choice(celeri_rave)
    aneth_choice = random.choice(aneth)
    baies_roses_choice = random.choice(baies_roses)
    prune_choice = random.choice(prune)
    betterave_choice = random.choice(betterave)
    noix_de_coco_choice = random.choice(noix_de_coco)
    citron_vert_choice = random.choice(citron_vert)
    citron_jaune_choice = random.choice(citron_jaune)
    dattes_choice = random.choice(dattes)
    laitue_choice = random.choice(laitue)
    roquette_choice = random.choice(roquette)
    concombre_choice = random.choice(concombre)
    poivrons_choice = random.choice(poivrons)
    asperge_choice = random.choice(asperge)
    oignons_crus_choice = random.choice(oignons_crus)
    oignons_caramelises_choice = random.choice(oignons_caramelises)
    oignons_frits_choice = random.choice(oignons_frits)
    stock = random.randint(10,10000)
    nb_achat = 0
    sushi = {'id':i, 'saumon':saumon_choice, 'saumon_teriyaki':saumon_teriyaki_choice, 'daurade':daurade_choice, 
             'thon':thon_choice, 'crevette':crevette_choice, 'poulet':poulet_choice, 'thon_cuit':thon_cuit_choice, 
             'foie_gras':foie_gras_choice,'tofu':tofu_choice, 'truite':truite_choice, 'hareng':hareng_choice, 
             'poulpe':poulpe_choice, 'boeuf':boeuf_choice, 'chair_de_crabe':chair_de_crabe_choice, 
             'oeufs_de_saumon':oeufs_de_saumon_choice, 'avocat':avocat_choice, 'fromage':fromage_choice, 
             'oeuf':oeuf_choice, 'gingembre':gingembre_choice,'wasabi':wasabi_choice, 'sauce_salee':sauce_salee_choice, 
             'sauce_sucree':sauce_sucree_choice,'sauce_sucreesalee':sauce_sucreesalee_choice, 
             'mayonnaise_classique':mayonnaise_classique_choice, 'mayonnaise_teriyaki':mayonnaise_teriyaki_choice, 
             'mayonnaise_japonaise':mayonnaise_japonaise_choice, 'mayonnaise_spicy':mayonnaise_japonaise_choice, 
             'mayonnaise_ponzu':mayonnaise_ponzu_choice, 'sauce_teriyaki':sauce_teriyaki_choice, 
             'sauce_satay_aux_cacahuetes':sauce_satay_aux_cacahuetes_choice, 'sauce_epicee':sauce_epicee_choice, 
             'mangue': mangue_choice, 'carotte':carotte_choice, 'anis':anis_choice,'poivre_rose':poivre_rose_choice, 
             'cannelle':cannelle_choice, 'cardamome':cardamome_choice, 'curcuma':curcuma_choice, 
             'feve':feve_choice, 'edamame':edamame_choice, 'macis':macis_choice, 'maniguette':maniguette_choice, 
             'paprika':paprika_choice, 'piment':piment_choice, 'poivre':poivre_choice, 'safran':safran_choice, 
             'sumac': sumac_choice, 'persil':persil_choice, 'herbe_de_provence':herbe_de_provence_choice, 
             'sesame':sesame_choice, 'feuilles_de_riz':feuilles_de_riz_choice, 'menthe':menthe_choice, 
             'coriandre':coriandre_choice, 'chou':chou_choice, 'ciboulette':ciboulette_choice, 'pomme':pomme_choice, 
             'celeri_rave':celeri_rave_choice, 'aneth':aneth_choice, 'baies_roses':baies_roses_choice, 
             'prune':prune_choice, 'betterave':betterave_choice, 'noix_de_coco':noix_de_coco_choice, 
             'citron_vert':citron_vert_choice, 'citron_jaune':citron_jaune_choice, 'dattes':dattes_choice, 
             'laitue':laitue_choice, 'roquette':roquette_choice, 'concombre':concombre_choice, 
             'poivrons':poivrons_choice, 'asperge':asperge_choice, 'oignons_crus':oignons_crus_choice, 
             'oignons_caramelises':oignons_caramelises_choice, 'oignons_frits':oignons_frits_choice,'stock':stock, 'nb_achat':nb_achat
            }
    
    sushis.append(sushi)

tps2 = time.perf_counter()
print(tps2 - tps1)

with r.pipeline() as pipe: 
    for i in range(len(sushis)):
        name = str("sushi:")+str(i)
        r.hmset(name,sushis[i])

stock_exemple_propre = int(r.hget('sushi:3564','stock').decode())
stock_exemple_bytes = r.hget('sushi:3564','stock')
print("En écriture propre : ",stock_exemple_propre," / ","En écriture Bytes : ",stock_exemple_bytes)

# On définit nos messages d'erreur, que l'on utilisera pour prévenir l'utilisateur selon différents critères 

# Plus de stock pour le sushi désiré
class OutOfStockError(Exception):
    """Notre magasin de sushis n'a plus du tout de stock pour le sushi désiré"""
    
# Stock rempli pour le sushi désiré : stock fixé à 10 000 maximum
class TooMuchStockError(Exception):
    """Notre magasin de sushis n'a plus de place pour stocker le sushi d'intérêt, nous n'avons rien pu ajouter
    au stock"""

# Le client désirait acheter trop de sushis et a fini la fin du stock
class TooMuchDemandError(Exception):
    """Le client souhaitait acheter plus de sushis qu'il n'y en avait de disponibles, il a fini le stock
    et n'a pas eu autant de sushis qu'il l'esperait"""

# Nous avons restocké au maximum les 10 000 sushis
class NoPlaceAvailableError(Exception):
    """Notre magasin n'a pas assez de place pour stocker tous les sushis que l'on souhaitait,
    seuls certains ont pu être ajoutés au stock"""

def buyitem(r, sushi_id,count):

    with r.pipeline() as pipe:
        
        while True:

            pipe.watch(sushi_id)
            nleft = int(r.hget(sushi_id,'stock').decode())
            # On utilise le int et decode pour convertir l'output bytes de Redis en nombre int
            
            # On réalise l'opération d'achat normalement s'il y a assez de sushis en stock
            if nleft > count :
                pipe.multi() # On débute l'enregistrement des étapes qu'on veux réaliser sur le serveur redis
                pipe.hincrby(sushi_id, 'stock', -count) # Le stock diminue ...
                pipe.hincrby(sushi_id, 'nb_achat', count) # ... Et le nombre de sushis achetés augmente
                pipe.execute() # On transfert l'ensemble des étapes réalisée depuis multi sur notre serveur Redis
                break
            
            # Si le nombre de sushis n'est pas suffisant pour satisfaire la demande, on achète tout ce qu'il reste
            elif nleft < count and nleft > 0:
                pipe.multi()
                pipe.hset(sushi_id,'stock',0)
                pipe.hincrby(sushi_id,'nb_achat',nleft)
                pipe.execute()
                
                raise TooMuchDemandError(f'Désolé, vous avez acheté tout les {sushi_id} restants mais il n''y en avait pas autant que vous le vouliez')

            # S'il n'y a plus du tout de ce type de sushis ...
            else:
                pipe.unwatch()
                raise OutOfStockError(f"Sorry, {sushi_id} is out of stock!")

    return None


buyitem(r,"sushi:5",60)
r.hmget("sushi:5","stock","nb_achat")

# Re-exécutez la cellule précédente : on a modifié les valeurs de stock et de la quantité d'achat sur notre database.

def restock(r,sushi_id,stock_count):
    
    with r.pipeline() as pipe:
        
        while True:
        
            pipe.watch(sushi_id)
            nleft_restock = int(r.hget(sushi_id,'stock').decode())

            # S'il y a suffisamment de places pour stocker les sushis, on achète le nombre demandé
            if nleft_restock + stock_count < 10000:
                pipe.multi()
                pipe.hincrby(sushi_id, 'stock', stock_count) # On modifie le stock sur notre database Redis
                pipe.execute()
                break
            
            # S'il n'y a pas suffisamment de place pour stocker tous les nouveaux sushis, on achète seulement ce que l'on peut
            elif nleft_restock < 10000 and nleft_restock + stock_count > 10000:
                pipe.multi()
                pipe.hset(sushi_id,'stock',10000)
                pipe.execute()                
                raise NoPlaceAvailableError(f"Désolé, nous avons déjà remis le stock de {sushi_id} au maximum")

            # Si le stock est déjà plein, cela ne sert à rien d'acheter davantage de sushis !
            # (et de toute façon on ne peut pas les stocker)
            else:
                pipe.unwatch()
                raise TooMuchStockError(f"Sorry, {sushi_id} is already full of stock!")
            
    return None


# Testons maintenant cette fonction : et si on augmentait le stock du sushi 9 de 400 ?

restock(r,'sushi:9', 400)
r.hmget("sushi:9",'stock','nb_achat')


# En répétant la cellule précédente plusieurs fois, on augmente la quantité stockée du sushi 9 comme précédemment.

def item_info():
    
    info_get = [] # Tableau qui contiendra les données récupérées
    
    for i in range(len(sushis)):
        name = str("sushi:")+str(i)
        stock = int(r.hget(name,'stock').decode())
        nb_achat = int(r.hget(name,'nb_achat').decode())
        info_add = [stock, nb_achat]               
        info_get.append(info_add)
        
    # On convertit notre liste de liste en dataframe
    item_df = pd.DataFrame(info_get,
                        columns=['stock','nb_achat'],
                        index = [str("sushi:")+str(i) for i in range(len(sushis))])
    
    return(item_df)

liste_sushi = item_info()
liste_sushi


# La fonction `item_ingredients`, elle, permet de récupérer les ingrédients de nos différents types de sushis (73 variables donc, correspondant à l'absence ou à la présence de chacun des ingrédients). Ces informations seront ensuite stockées dans un dataframe Pandas.

def item_ingredient():
    
    ingredient_get = []
    
    for i in range(len(sushis)):
        
        name = str("sushi:")+str(i)
        ingredient_add = []
        
        name_ingredient = ['saumon', 'saumon_teriyaki', 'daurade', 'thon', 'crevette', 
                                            'poulet', 'thon_cuit', 'foie_gras', 'tofu', 'truite', 'hareng', 
                                            'poulpe', 'boeuf', 'chair_de_crabe', 'oeufs_de_saumon', 'avocat', 
                                            'fromage', 'oeuf', 'gingembre', 'wasabi', 'sauce_salee', 
                                            'sauce_sucree', 'sauce_sucreesalee', 'mayonnaise_classique', 
                                            'mayonnaise_teriyaki', 'mayonnaise_japonaise', 'mayonnaise_spicy', 
                                            'mayonnaise_ponzu', 'sauce_teriyaki', 'sauce_satay_aux_cacahuetes',
                                            'sauce_epicee', 'mangue', 'carotte', 'anis', 'poivre_rose', 
                                            'cannelle', 'cardamome', 'curcuma', 'feve', 'edamame', 'macis', 
                                            'maniguette', 'paprika', 'piment', 'poivre', 'safran', 'sumac', 
                                            'persil', 'herbe_de_provence', 'sesame', 'feuilles_de_riz', 
                                            'menthe', 'coriandre', 'chou', 'ciboulette', 'pomme', 
                                            'celeri_rave', 'aneth', 'baies_roses', 'prune', 'betterave', 
                                            'noix_de_coco', 'citron_vert', 'citron_jaune', 'dattes', 
                                            'laitue', 'roquette', 'concombre', 'poivrons', 'asperge', 
                                            'oignons_crus', 'oignons_caramelises', 'oignons_frits']

        # La boucle permet de rentrer l'ensemble des ingrédients dans le tableau
        for i in range(len(name_ingredient)):
            ingredient = r.hget(name, name_ingredient[i]).decode() # On récupère les infos depuis la database Redis
            ingredient_add.append(ingredient)
        
        ingredient_get.append(ingredient_add)
        
    ingredient_df = pd.DataFrame(ingredient_get,
                        columns=name_ingredient,
                        index = [str("sushi:")+str(i) for i in range(len(sushis))])
    
    return(ingredient_df)

ingredient_df = item_ingredient()
ingredient_df


def sushi_interet(r,liste_ingredients,ingredient_df):
        
    sushi_interessant = [] # Liste qui stockera les numéros de tous les sushis contenant tous les ingrédients de liste_ingredients
    for j in range(len(ingredient_df)): # On prend tous les sushis successivement ...
        if all(ingredient_df.iloc[j][liste_ingredients]=="Oui"): # ... et on regarde s'ils contiennent tous les ingrédients demandés
            sushi_interessant.append(j)
            
    phrase = "Vous pourriez apprécier les sushis suivants : "
    for i in range(len(sushi_interessant)):
        phrase += "sushi:"+str(sushi_interessant[i])+" "

    print(phrase)
    return(sushi_interessant)


liste_ingredients = ['saumon', 'avocat', 'thon', 'roquette', 'cannelle', 'cardamome', 'curcuma',
                     'feve', 'edamame', 'paprika', 'piment', 'poivre', 'safran']
sushi_interet(r,liste_ingredients,ingredient_df)
