from fonctions import fichier_citations
import networkx as nx
from pprint import pprint
import time


from pprint import pprint
import time

tmps1 = time.time()



#chargement des donnée
import json
from pprint import  pprint

chemin1="./ArcticleAuteur.json"
chemin2="./CitationsArticles.json"

#telechargement de des données
def charge_donnees(chemin):
    with open(chemin,'r') as donnees:
        return json.load(donnees)

#creation du graphe
graphe = nx.DiGraph() #graphe orietée


#Creation des sommets du graphe
dictionnaire_article=charge_donnees(chemin1)
liste_articles=list(dictionnaire_article.keys())
graphe.add_nodes_from(liste_articles) #sommet du graphe


#Creation des arrets du graphe
dictionnaire_citation=charge_donnees(chemin2)
liste_arrets=dictionnaire_citation.values()
#pprint(liste_arrets)
graphe.add_edges_from(list(liste_arrets)) #arrets du graphe

#sort la liste de tous les auteurs cités par un auteur donné

def auteurs_cites(auteur):

    #trouver les acticle ecrits par cet auteur
    articles_ecrits = []
    for id_article in list(dictionnaire_article.keys()):
        if auteur in dictionnaire_article[id_article]:
            articles_ecrits.append(id_article)
    return articles_ecrits



    #trouver les articles cités par les articles trouvés precedement
def articles_cites(articles_ecrits):
    liste_article_cites=[]
    for article in articles_ecrits:
        liste_article_cites=list(graphe.successors(article))
    return liste_article_cites


    #donner les auteurs des articles cité
def auteur_arcticles_cites(liste_article_cites):
    liste_auteurs=[]
    for article in liste_article_cites:
        for nom in dictionnaire_article[article]:
            liste_auteurs.append(nom)
            liste_auteurs=list(set(liste_auteurs))
            #liste_auteurs_tries=liste_auteurs.sort()
    return liste_auteurs

def resultat(auteur):
    articles_ecrits=auteurs_cites( auteur)
    liste_article_cites=articles_cites(articles_ecrits)
    resultats=auteur_arcticles_cites(liste_article_cites)
    return resultats
    #pprint(resultats)



def influence(auteur, N):
    i = 0
    predecesseurs = auteurs_cites(auteur)
    liste = list(range(N + 1))
    liste[i] = auteurs_cites(auteur)
    dico_aut_int_global = {}

    while i < N:
        sommets = predecesseurs
        nv_elemnt = []
        dico_aut_int = {}
        #print(f"niveau {i + 1}  ####################################")
        for sommet in liste[i]:
            for article in list(graphe.predecessors(sommet)):
                predecesseurs.append(article)
                nv_elemnt.append(article)
        liste[i + 1] = nv_elemnt
       # print(f"niveaunv:{i + 1}", nv_elemnt)
        auteurs_a = []
        auteurs_b = []

        for art in nv_elemnt:
            if dictionnaire_article[art] != []:
                for aut in dictionnaire_article[art]:
                    auteurs_b.append(aut)
        #print(auteurs_b)

        for aut1 in auteurs_b:
            nb_apparition = 0
            for aut2 in auteurs_b[auteurs_b.index(aut1):]:
                if aut1 == aut2:
                    nb_apparition += 1
            # print(aut1, nb_apparition)
            if not aut1 in dico_aut_int.keys():
                dico_aut_int[aut1] = round((nb_apparition) / (i + 1), 3)
        #print(dico_aut_int)

        for cle in dico_aut_int.keys():
            if not cle in dico_aut_int_global.keys():
                dico_aut_int_global[cle] = dico_aut_int[cle]
            else:
                dico_aut_int_global[cle] += dico_aut_int[cle]
        i += 1

    print("RESULTAT")
    print(f"Le nombre d'auteur influencés par {auteur} avec une profondeur au plus {N} est : {len(dico_aut_int_global.keys())}")

    intensite=list(dico_aut_int_global.values())
    somme=0
    liste_valeur=[]
    for valeur in intensite:
        somme+=valeur
        liste_valeur.append(valeur) #

    print(f"La plus grande intensité d'influence est : {max(liste_valeur)}")
    print(f"La plus etite intensité d'influence est : {min(liste_valeur)}")
    if len(dico_aut_int_global.keys())==0:
        print(f"L'intensité moyenne est : 0")
    else:
        print(f"L'intensité moyenne est : {round(somme / len(dico_aut_int_global.keys()))}")

    from operator import itemgetter, attrgetter
    #pprint(dico_aut_int_global)
    #pprint(sorted(dico_aut_int_global, key=itemgetter(1), reverse=True))
    pprint(sorted(dico_aut_int_global.items(), key=lambda t: t[1], reverse=True))
















tmps2 = time.time() - tmps1                                                #On capte le temps d'execution du programme

print("Recherche effectuée avec succès")
print("Temps d'execution = %f" % tmps2)


