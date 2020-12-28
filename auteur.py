from fonctions import fichier_citations
import networkx as nx
from pprint import pprint
import time


from pprint import pprint
import time

tmps1 = time.time()



#chargement des donnÃ©e
import json
from pprint import  pprint

chemin1="C:\Projet programmation\ArcticleAuteur.json"
chemin2="C:\Projet programmation\CitationsArticles.json"

#telechargement de des donnÃ©es
def charge_donnees(chemin):
    with open(chemin,'r') as donnees:
        return json.load(donnees)

#creation du graphe
graphe = nx.DiGraph() #graphe orietÃ©e


#Creation des sommets du graphe
dictionnaire_article=charge_donnees(chemin1)
liste_articles=list(dictionnaire_article.keys())
graphe.add_nodes_from(liste_articles) #sommet du graphe


#Creation des arrets du graphe
dictionnaire_citation=charge_donnees(chemin2)
liste_arrets=dictionnaire_citation.values()
#pprint(liste_arrets)
graphe.add_edges_from(list(liste_arrets)) #arrets du graphe

#sort la liste de tous les auteurs citÃ©s par un auteur donnÃ©

def auteurs_cites(auteur):

    #trouver les acticle ecrits par cet auteur
    articles_ecrits = []
    for id_article in list(dictionnaire_article.keys()):
        if auteur in dictionnaire_article[id_article]:
            articles_ecrits.append(id_article)
    return articles_ecrits



    #trouver les articles citÃ©s par les articles trouvÃ©s precedement
def articles_cites(articles_ecrits):
    liste_article_cites=[]
    for article in articles_ecrits:
        liste_article_cites=list(graphe.successors(article))
    return liste_article_cites


    #donner les auteurs des articles citÃ©
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
    #return resultats
    print("  ")
    print("############### RESULTATS ########################")
    print("  ")
    print(f"    {auteur} a citÃ© {len(resultats)} auteurs")
    print("  ")

    pprint(resultats)






def fonction_influence(auteur, N, type):

    i = 0
    predecesseurs = auteurs_cites(auteur)
    liste = list(range(N + 1))
    liste[i] = auteurs_cites(auteur)
    dico_aut_int_global = {}

    while i < N:
        nv_elemnt = []
        dico_aut_int = {}
        for sommet in liste[i]:
            if type=="predecesseurs":
                for article in list(graphe.predecessors(sommet)):
                    predecesseurs.append(article)
                    nv_elemnt.append(article)
            elif type=="successeurs":
                for article in list(graphe.successors(sommet)):
                    predecesseurs.append(article)
                    nv_elemnt.append(article)
        liste[i + 1] = nv_elemnt
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
    return dico_aut_int_global






def influence_par(auteur,N):
    dico_aut_int_global=fonction_influence(auteur, N, "predecesseurs")
    print("  ")
    print("###################################### RESULTATS ######################################")
    print("  ")
    print("#######################################################################################")
    print(f"    Le nombre d'auteurs influencés par {auteur} avec une profondeur au plus {N} est : {len(dico_aut_int_global.keys())}")

    intensite = list(dico_aut_int_global.values())
    somme = 0
    liste_valeur = []
    for valeur in intensite:
        somme += valeur
        liste_valeur.append(valeur)  #

    print(f"    La plus grande intensité d'influence est : {max(liste_valeur)}")
    print(f"    La plus petite intensité d'influence est : {min(liste_valeur)}")
    if len(dico_aut_int_global.keys()) == 0:
        print(f"    L'intensité moyenne est : 0")
    else:
        print(f"    L'intensité moyenne est : {round(somme / len(dico_aut_int_global.keys()), 3)}")
    print("#######################################################################################")
    print("  ")
    pprint(sorted(dico_aut_int_global.items(), key=lambda t: t[1], reverse=True))



def influence(auteur,N):
    dico_aut_int_global=fonction_influence(auteur, N, "successeurs")
    print("  ")
    print("###################################### RESULTATS ######################################")
    print("  ")
    print("#######################################################################################")
    print(f"    Le nombre d'auteurs qui influencent {auteur} avec une profondeur au plus {N} est : {len(dico_aut_int_global.keys())}")

    intensite = list(dico_aut_int_global.values())
    somme = 0
    liste_valeur = []
    for valeur in intensite:
        somme += valeur
        liste_valeur.append(valeur)

    print(f"    La plus grande intensité d'influence est : {max(liste_valeur)}")
    print(f"    La plus petite intensité d'influence est : {min(liste_valeur)}")
    if len(dico_aut_int_global.keys()) == 0:
        print(f"    L'intensité moyenne est : 0")
    else:
        print(f"    L'intensité moyenne est : {round(somme / len(dico_aut_int_global.keys()), 3)}")
    print("#######################################################################################")
    print("  ")
    pprint(sorted(dico_aut_int_global.items(), key=lambda t: t[1], reverse=True))




def communautes(auteur, N):
    dico_influence_par=fonction_influence(auteur, N, "predecesseurs")
    dico_influence=fonction_influence(auteur, N, "successeurs")
    liste_communaute=[]
    #print(dico_influence_par.keys())

    for auteur_a in dico_influence_par.keys():
        for auteur_b in dico_influence.keys():
            if auteur_a==auteur_b:
                liste_communaute.append(auteur_b)
    print("  ")
    print("###################################### RESULTATS ######################################")
    print("  ")
    print("#######################################################################################")
    pprint(liste_communaute)





tmps2 = time.time() - tmps1                                                #On capte le temps d'execution du programme

print("Recherche effectuée avec succès")
print("Temps d'execution = %f" % tmps2)


