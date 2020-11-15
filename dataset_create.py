## Création du JDD sushis

import random
import time
random.seed(444)

# Attributs avec plus de 2 modalités
type = ['sushi', 'sashimi', 'maki']
prix = [4.5, 4.8, 5, 5.2, 5.5, 5.8, 6, 6.4, 6.5, 6.7, 7, 7.5, 8, 8.8, 9.2]
stock_magasin1 = [0, 20, 30, 40, 50, 100, 200, 300, 500, 800]
stock_magasin2 = [0, 20, 30, 40, 50, 100, 200, 300, 500, 800]
stock_magasin3 = [0, 20, 30, 40, 50, 100, 200, 300, 500, 800]
stock_magasin4 = [0, 20, 30, 40, 50, 100, 200, 300, 500, 800]
stock_magasin5 = [0, 20, 30, 40, 50, 100, 200, 300, 500, 800]

# Attributs avec 2 modalités : les ingrédients
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

3 * 15 * 10**5 * 2**72
# 21 250 649 172 913 403 461 632 000 000 = 2 * 10**28 combinaisons possibles

# Création du JDD
sushis = []

tps1 = time.clock()

for i in range(0, 1000000):
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
    type_choice = random.choice(type)
    prix_choice = random.choice(prix)
    stock_magasin1_choice = random.choice(stock_magasin1)
    stock_magasin2_choice = random.choice(stock_magasin2)
    stock_magasin3_choice = random.choice(stock_magasin3)
    stock_magasin4_choice = random.choice(stock_magasin4)
    stock_magasin5_choice = random.choice(stock_magasin5)
    sushi = {'id':i, 'saumon':saumon_choice, 'saumon_teriyaki':saumon_teriyaki_choice, 'daurade':daurade_choice, 'thon':thon_choice, 'crevette':crevette_choice, 'poulet':poulet_choice, 'thon_cuit':thon_cuit_choice, 'foie_gras':foie_gras_choice, 'tofu':tofu_choice, 'truite':truite_choice, 'hareng':hareng_choice, 'poulpe':poulpe_choice, 'boeuf':boeuf_choice, 'chair_de_crabe':chair_de_crabe_choice, 'oeufs_de_saumon':oeufs_de_saumon_choice, 'avocat':avocat_choice, 'fromage':fromage_choice, 'oeuf':oeuf_choice, 'gingembre':gingembre_choice, 'wasabi':wasabi_choice, 'sauce_salee':sauce_salee_choice, 'sauce_sucree':sauce_sucree_choice, 'sauce_sucreesalee':sauce_sucreesalee_choice, 'mayonnaise_classique':mayonnaise_classique_choice, 'mayonnaise_teriyaki':mayonnaise_teriyaki_choice, 'mayonnaise_japonaise':mayonnaise_japonaise_choice, 'mayonnaise_spicy':mayonnaise_japonaise_choice, 'mayonnaise_ponzu':mayonnaise_ponzu_choice, 'sauce_teriyaki':sauce_teriyaki_choice, 'sauce_satay_aux_cacahuetes':sauce_satay_aux_cacahuetes_choice, 'sauce_epicee':sauce_epicee_choice, 'mangue': mangue_choice, 'carotte':carotte_choice, 'anis':anis_choice, 'poivre_rose':poivre_rose_choice, 'cannelle':cannelle_choice, 'cardamome':cardamome_choice, 'curcuma':curcuma_choice, 'feve':feve_choice, 'edamame':edamame_choice, 'macis':macis_choice, 'maniguette':maniguette_choice, 'paprika':paprika_choice, 'piment':piment_choice, 'poivre':poivre_choice, 'safran':safran_choice, 'sumac': sumac_choice, 'persil':persil_choice, 'herbe_de_provence':herbe_de_provence_choice, 'sesame':sesame_choice, 'feuilles_de_riz':feuilles_de_riz_choice, 'menthe':menthe_choice, 'coriandre':coriandre_choice, 'chou':chou_choice, 'ciboulette':ciboulette_choice, 'pomme':pomme_choice, 'celeri_rave':celeri_rave_choice, 'aneth':aneth_choice, 'baies_roses':baies_roses_choice, 'prune':prune_choice, 'betterave':betterave_choice, 'noix_de_coco':noix_de_coco_choice, 'citron_vert':citron_vert_choice, 'citron_jaune':citron_jaune_choice, 'dattes':dattes_choice, 'laitue':laitue_choice, 'roquette':roquette_choice, 'concombre':concombre_choice, 'poivrons':poivrons_choice, 'asperge':asperge_choice, 'oignons_crus':oignons_crus_choice, 'oignons_caramelises':oignons_caramelises_choice, 'oignons_frits':oignons_frits_choice, 'type':type_choice, 'prix':prix_choice, 'stock_magasin1':stock_magasin1_choice, 'stock_magasin2':stock_magasin2_choice, 'stock_magasin3':stock_magasin3_choice, 'stock_magasin4':stock_magasin4_choice, 'stock_magasin5':stock_magasin5_choice}
    sushis.append(sushi)

tps2 = time.clock()
print(tps2 - tps1)
# 103 secondes pour 1 million de sushis différents
