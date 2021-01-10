# -*- coding: utf8 -*-

# Modules importés
import time, re, termtables, json, os
# from fonctions import fichier_citations
import networkx as nx
from pprint import pprint


class Auteur():

    def __init__(self, auteur):
        self.auteur = auteur

    def charge_donnees(self, chemin):
        """chargement des donnée"""

        with open(chemin, 'r') as donnees:
            return json.load(donnees)

    def graphe(self, dictionnaire_sommets, dictionnaire_arrets):
        """Creation d'un graphe orienté"""

        graphe = nx.DiGraph()
        # dictionnaire_article = charge_donnees(chemin1)
        liste_sommets = list(dictionnaire_sommets.keys())
        graphe.add_nodes_from(liste_sommets)  # Creation des sommets du graphe

        # dictionnaire_citation = charge_donnees(chemin2)
        liste_arrets = dictionnaire_arrets.values()
        graphe.add_edges_from(list(liste_arrets))  # Creation des arrets du graphe

        return graphe

    def auteurs_cites(self, auteur, dictionnaire_sommets):
        """Cette fonction sort la liste de tous les auteurs cités par un auteur donné """

        # trouver les acticle ecrits par cet auteur
        articles_ecrits = []
        for id_article in list(dictionnaire_sommets.keys()):
            if auteur.title() in dictionnaire_sommets[id_article]:
                articles_ecrits.append(id_article)
        return articles_ecrits

    def articles_cites(self, articles_ecrits, graphe):
        """Cette fonction sort la liste de tous les articles cités par un ensemble d'articles contenus dans une liste"""

        liste_article_cites = []

        for article in articles_ecrits:
            liste_article_cites = list(graphe.successors(article))
        return liste_article_cites

    def auteur_arcticles_cites(self, liste_article_cites, auteur, dictionnaire_sommets):
        """Cette fonction sort la liste de tous les auteurs d'un ensemble d'articles contenus dans une liste"""

        liste_auteurs = []
        for article in liste_article_cites:
            if not auteur in dictionnaire_sommets[article]:
                for nom in dictionnaire_sommets[article]:
                    if nom != "" and nom != " ":
                        liste_auteurs.append(nom)
                        liste_auteurs = list(set(liste_auteurs))
                        # liste_auteurs_tries=liste_auteurs.sort()
        return liste_auteurs

    def fonction_influence(self, auteur, N, nom_fichier_articles, nom_fichier_references, type):

        i = 0
        predecesseurs = Auteur.auteurs_cites(self,auteur, Auteur.charge_donnees(self,nom_fichier_articles))
        liste = list(range(N + 1))
        liste[0] = Auteur.auteurs_cites(self,auteur, Auteur.charge_donnees(self,nom_fichier_articles))
        dico_aut_int_global = {}

        while i < N:
            nv_elemnt = []
            dico_aut_int = {}
            for sommet in liste[i]:
                if type == "predecesseurs":
                    for article in list(Auteur.graphe(self,Auteur.charge_donnees(self,nom_fichier_articles),Auteur.charge_donnees(self,nom_fichier_references)).predecessors(sommet)):
                        predecesseurs.append(article)
                        nv_elemnt.append(article)
                elif type == "successeurs":
                    for article in list(Auteur.graphe(self,Auteur.charge_donnees(self,nom_fichier_articles),
                                                      Auteur.charge_donnees(self,nom_fichier_references)).successors(
                            sommet)):
                        predecesseurs.append(article)
                        nv_elemnt.append(article)
            liste[i + 1] = nv_elemnt
            auteurs_b = []

            for art in nv_elemnt:
                if Auteur.charge_donnees(self,nom_fichier_articles)[art] != []:
                    for aut in Auteur.charge_donnees(self,nom_fichier_articles)[art]:
                        auteurs_b.append(aut)
            # print(auteurs_b)

            for aut1 in auteurs_b:
                nb_apparition = 0
                for aut2 in auteurs_b[auteurs_b.index(aut1):]:
                    if aut1 == aut2:
                        nb_apparition += 1
                # print(aut1, nb_apparition)
                if not aut1 in dico_aut_int.keys():
                    dico_aut_int[aut1] = round((nb_apparition) / (i + 1), 3)
            # print(dico_aut_int)

            for cle in dico_aut_int.keys():
                if not cle in dico_aut_int_global.keys():
                    dico_aut_int_global[cle] = dico_aut_int[cle]
                else:
                    dico_aut_int_global[cle] += dico_aut_int[cle]

            i += 1
        return dico_aut_int_global


if __name__ == "__main__":

    from sys import argv

    tmps1 = time.time()

    nb_arguments = len(argv)





    if nb_arguments > 3:
        if argv[1] == 'cite':
            if __name__ == "__main__":

                nom_auteur = ""
                for i in range(2, nb_arguments):
                    nom_auteur += " " + argv[i]

                auteur = nom_auteur.strip()
                nom_fichier_articles = "./articles.json"
                nom_fichier_references = "./references.json"
                Auteur = Auteur(auteur)

                dictionnaire_sommets = Auteur.charge_donnees(nom_fichier_articles)
                dictionnaire_arrets = Auteur.charge_donnees(nom_fichier_references)
                articles_ecrits = Auteur.auteurs_cites(auteur, dictionnaire_sommets)

                liste_article_cites = Auteur.articles_cites(articles_ecrits,
                                                            Auteur.graphe(dictionnaire_sommets, dictionnaire_arrets))
                resultats = Auteur.auteur_arcticles_cites(liste_article_cites, auteur, dictionnaire_sommets)

                # return resultats
                print("  ")
                print("############### RESULTATS ########################")
                print("  ")
                tmps2 = time.time() - tmps1  # On capte le temps d'execution du programme
                print("Recherche effectuée avec succès")
                print("Temps d'execution = %f" % tmps2)
                print("  ")
                print(f"    {auteur} a cité {len(resultats)} auteurs")
                print("  ")

                resultats_tries = sorted(resultats, reverse=False)

                if "" in resultats_tries:
                    print(resultats_tries[resultats_tries.index("")])
                resultat_final = []
                for i in range(len(resultats_tries)):
                    resultat_final.append([i + 1, resultats_tries[i]])

                header = [" ", "NOM AUTEUR"]
                if len(resultat_final) > 0:
                    termtables.print(sorted(resultat_final, key=lambda t: t[0], reverse=False), header)

    if nb_arguments > 3:
        if argv[1] == 'influence_par':
            if __name__ == "__main__":

                nom_auteur = ""
                for i in range(2, nb_arguments - 1):
                    nom_auteur += " " + argv[i]

                auteur = nom_auteur.strip()
                N = int(argv[nb_arguments - 1])

                nom_fichier_articles = "./articles.json"
                nom_fichier_references = "./references.json"
                Auteur = Auteur(auteur)

                dictionnaire_sommets = Auteur.charge_donnees(nom_fichier_articles)

                auteurs_cites = Auteur.auteurs_cites(auteur, Auteur.charge_donnees(nom_fichier_articles))

                dico_aut_int_global = Auteur.fonction_influence(auteur, N, nom_fichier_articles, nom_fichier_references,
                                                                "predecesseurs")

                print("  ")
                print("###################################### RESULTATS ######################################")
                print("  ")
                tmps2 = time.time() - tmps1  # On capte le temps d'execution du programme
                print("Recherche effectuée avec succès")
                print("Temps d'execution = %f" % tmps2)
                print("  ")
                print("#######################################################################################")
                print(f"    Le nombre d'auteurs influencés par {auteur} avec une profondeur au plus {N} est :,"
                      f" {len(dico_aut_int_global.keys())}")

                if len(dico_aut_int_global.keys()) > 0:

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
                    # pprint(sorted(dico_aut_int_global.items(), key=lambda t: t[1], reverse=True))

                    # pprint(sorted(dico_aut_int_global.items(), key=lambda t: t[1], reverse=True))
                    print("    ")

                    # dico_aut_int_global["NOM AUTEUR"]="INTENSITE"

                    header = ["NOM AUTEUR", "INTENSITE"]
                    affichage = []
                    for cle in dico_aut_int_global.keys():
                        affichage.append([cle, dico_aut_int_global[cle]])

                    # termtables.print([["NOM AUTEUR", "INTENSITE"]])

                    termtables.print(sorted(affichage, key=lambda t: t[1], reverse=True), header)

                else:
                    print(" ")
                    print(f"    Rien à afficher pour : {auteur}")

    if nb_arguments > 3:
        if argv[1] == 'influence':
            if __name__ == "__main__":

                nom_auteur = ""
                for i in range(2, nb_arguments - 1):
                    nom_auteur += " " + argv[i]

                auteur = nom_auteur.strip()
                N = int(argv[nb_arguments - 1])

                nom_fichier_articles = "./articles.json"
                nom_fichier_references = "./references.json"
                Auteur = Auteur(auteur)

                dictionnaire_sommets = Auteur.charge_donnees(nom_fichier_articles)

                auteurs_cites = Auteur.auteurs_cites(auteur, Auteur.charge_donnees(nom_fichier_articles))

                dico_aut_int_global = Auteur.fonction_influence(auteur, N, nom_fichier_articles, nom_fichier_references,
                                                                "successeurs")

                print("  ")
                print("###################################### RESULTATS ######################################")
                print("  ")
                tmps2 = time.time() - tmps1  # On capte le temps d'execution du programme
                print("Recherche effectuée avec succès")
                print("Temps d'execution = %f" % tmps2)
                print("  ")
                print("#######################################################################################")
                print(f"    Le nombre d'auteurs qui influencent {auteur} avec une profondeur au plus {N} est :,"
                      f" {len(dico_aut_int_global.keys())}")

                if len(dico_aut_int_global.keys()) > 0:

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
                    # pprint(sorted(dico_aut_int_global.items(), key=lambda t: t[1], reverse=True))

                    # pprint(sorted(dico_aut_int_global.items(), key=lambda t: t[1], reverse=True))
                    print("    ")

                    # dico_aut_int_global["NOM AUTEUR"]="INTENSITE"

                    header = ["NOM AUTEUR", "INTENSITE"]
                    affichage = []
                    for cle in dico_aut_int_global.keys():
                        affichage.append([cle, dico_aut_int_global[cle]])

                    # termtables.print([["NOM AUTEUR", "INTENSITE"]])

                    termtables.print(sorted(affichage, key=lambda t: t[1], reverse=True), header)

                else:
                    print(" ")
                    print(f"    Rien à afficher pour : {auteur}")

    # def communautes(auteur, N):
    if nb_arguments > 3:
        if argv[1] == 'communautes':

            nom_auteur = ""
            for i in range(2, nb_arguments - 1):
                nom_auteur += " " + argv[i]

            auteur = nom_auteur.strip()
            N = int(argv[nb_arguments - 1])
            nom_fichier_articles = "./articles.json"
            nom_fichier_references = "./references.json"
            Auteur = Auteur(auteur)


            dico_influence_par =Auteur.fonction_influence(auteur, N, nom_fichier_articles, nom_fichier_references,"predecesseurs")
            dico_influence = Auteur.fonction_influence(auteur, N, nom_fichier_articles, nom_fichier_references,"successeurs")

            liste_communaute = []
            # print(dico_influence_par.keys())

            for auteur_a in dico_influence_par.keys():
                for auteur_b in dico_influence.keys():
                    if re.sub(" ", "", re.sub("  ", "", auteur_a.upper())) == re.sub(" ", "", re.sub("  ", "",
                                                                                                     auteur_b.upper())) and re.sub(
                        " ", "", re.sub("  ", "", auteur_a.upper())) != "":
                        # if auteur_a == auteur_b:
                        re.sub(" ", "", re.sub("  ", "", auteur_a.upper()))
                        liste_communaute.append(auteur_b)

            liste_triee = sorted(liste_communaute, key=lambda t: t[0], reverse=False)
            liste_finale = []
            for i in range(len(liste_triee)):
                liste_finale.append([i + 1, liste_triee[i]])

            print("  ")
            print("###################################### RESULTATS ######################################")
            print("  ")
            tmps2 = time.time() - tmps1  # On capte le temps d'execution du programme
            print("Recherche effectuée avec succès")
            print("Temps d'execution = %f" % tmps2)
            print("  ")
            print("#######################################################################################")
            print(f"    La communauté de  {auteur} avec une profondeur au plus {N} comporte :,"
                  f" {len(liste_communaute)} auteurs")

            if len(liste_finale) > 0:

                header = [" ", "NOM AUTEUR"]
                termtables.print(sorted(liste_finale, key=lambda t: t[0], reverse=False), header)
            else:
                print(" ")
                print(f"    Rien à afficher pour : {auteur}")