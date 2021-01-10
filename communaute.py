# -*- coding: utf8 -*-

import os, time, termtables, re
from sys import argv

# class Main():

# def condition(self):
statut = "desactivé"
nb_arguments = len(argv)

if argv[0] == "communaute.py":
    if nb_arguments == 1:
        from aide import Aide

        Aide=Aide()
        Aide.f1()



    if nb_arguments == 2:
        if argv[1] == 'init':
            os.system("initialisation.py")


        else:
            if argv[1] == 'aide':
                # statut = 'aide activée'
                if __name__ == "__main__":
                    from aide import Aide

                    Aide=Aide()
                    Aide.f1()

            else:
                if argv[1] == 'cite':
                    from aide import Aide

                    Aide = Aide()
                    Aide.f4()


                else:
                    if argv[1] == 'influence':
                        from aide import Aide
                        Aide = Aide()
                        Aide.f5()

                    else:
                        if argv[1] == 'communautes':
                            from aide import Aide
                            Aide = Aide()
                            Aide.f7()

                        else:
                            if argv[1] == 'influence_par':
                                from aide import Aide
                                Aide = Aide()
                                Aide.f6()


                            else:
                                from aide import Aide

                                Aide = Aide()
                                Aide.f10()
    if nb_arguments == 3:
        if argv[1] == 'init':
            from aide import Aide
            Aide = Aide()
            Aide.f3()




        elif argv[1] == 'aide':
            from aide import Aide
            Aide = Aide()
            Aide.f2()

        elif argv[1] == 'cite':
            if __name__ == "__main__":
                from auteur import resultat
                auteur = argv[2]
                resultat(auteur.strip().tilte())



        elif argv[1] == 'communautes':
            from aide import Aide
            Aide = Aide()
            Aide.f8()


        else:
            if argv[1] == 'influence_par':
                from aide import Aide
                Aide = Aide()
                Aide.f6()


            else:
                from aide import Aide
                Aide = Aide()
                Aide.f9()



    if nb_arguments > 3:
        if argv[1] == 'influence_par':
            tmps1 = time.time()
            from auteur import Auteur



            nom_auteur = ""
            for i in range(2, nb_arguments - 1):
                nom_auteur += " " + argv[i]

            auteur = nom_auteur.strip()

            try:
                int(argv[nb_arguments-1])
                N = int(argv[nb_arguments - 1])

                nom_fichier_articles = "./articles.json"
                nom_fichier_references = "./references.json"
                Auteur = Auteur(auteur)

                dictionnaire_sommets = Auteur.charge_donnees(nom_fichier_articles)

                auteurs_cites = Auteur.auteurs_cites(auteur, Auteur.charge_donnees(nom_fichier_articles))

                dico_aut_int_global = Auteur.fonction_influence(auteur, N, nom_fichier_articles,
                                                                nom_fichier_references,
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
                    print(
                        "#######################################################################################")
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
            except ValueError:
                print("Veillez entrer la profondeur: la profondeur doit etre un entier naturel")



    if nb_arguments > 3:
        if argv[1] == 'influence':
            tmps1 = time.time()
            from auteur import Auteur

            nom_auteur = ""
            for i in range(2, nb_arguments - 1):
                nom_auteur += " " + argv[i]

            auteur = nom_auteur.strip()

            try:
                int(argv[nb_arguments-1])
                N = int(argv[nb_arguments - 1])


                nom_fichier_articles = "./articles.json"
                nom_fichier_references = "./references.json"
                Auteur = Auteur(auteur)

                dictionnaire_sommets = Auteur.charge_donnees(nom_fichier_articles)

                auteurs_cites = Auteur.auteurs_cites(auteur, Auteur.charge_donnees(nom_fichier_articles))

                dico_aut_int_global = Auteur.fonction_influence(auteur, N, nom_fichier_articles,
                                                                nom_fichier_references,
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
                        print(f"    L'intensité moyenne est : {round(somme / len(dico_aut_int_global.keys()),3)}")
                    print(
                        "#######################################################################################")
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
            except ValueError:
                print("Veillez entrer la profondeur: la profondeur doit etre un entier naturel")



    if nb_arguments > 3:
        if argv[1] == 'communautes':
            if __name__ == "__main__":
                tmps1 = time.time()
                from auteur import Auteur


                nom_auteur = ""
                for i in range(2, nb_arguments - 1):
                    nom_auteur += " " + argv[i]
                auteur = nom_auteur.strip()

                try:
                    int(argv[nb_arguments - 1])
                    N = int(argv[nb_arguments - 1])
                    nom_fichier_articles = "./articles.json"
                    nom_fichier_references = "./references.json"
                    Auteur = Auteur(auteur)

                    dico_influence_par = Auteur.fonction_influence(auteur, N, nom_fichier_articles,
                                                                   nom_fichier_references, "predecesseurs")
                    dico_influence = Auteur.fonction_influence(auteur, N, nom_fichier_articles, nom_fichier_references,
                                                               "successeurs")

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
                except ValueError:
                    print("Veillez entrer la profondeur: la profondeur doit etre un entier naturel")



    if nb_arguments > 3:
        if argv[1] == 'cite':
            if __name__ == "__main__":
                from auteur import Auteur

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
                                                                        Auteur.graphe(dictionnaire_sommets,
                                                                                      dictionnaire_arrets))
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