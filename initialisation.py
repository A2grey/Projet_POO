
# -*- coding: utf8 -*-

#Importation des modules
import os, sys, csv
import os.path
from os import getcwd, chdir, mkdir

from  fonctions import * #recherche_ligne_auteurs, liste_auteurs, remplissage_baseArcticle
import time






class Initialisation:
    #statut=
    #if statut=="activé"
    tmps1 = time.time()  # On capte le temps au debut

    #1-creation du fichier texte des citations

    bdd = "./CitationsArticles.json"
    with open(bdd, 'w', encoding='utf-8') as data:
        data.write(json.dumps(Dictionnaire_citations()))

    #fichier_citations()


    #2-creation du fichier texte des articles sous format json
    #def fichier_arcticle(self):
    #Parametres
    chemin_initial = "./hep-th-abs"
    bdd = "./ArcticleAuteur.json"
    dictionnaire = {}


    liste_chemin=recherche_chemin(chemin_initial)                         #liste des chemins des fichiers abs dans le dossier initial
    for chemin in liste_chemin:
        ligne_des_auteurs = recherche_ligne_auteurs(chemin)               # constitution de la liste des auteurs pour chaque fichier
        liste_des_auteurs=liste_auteurs(ligne_des_auteurs)
        dictionnaire=dictionnaire_par_article(liste_des_auteurs, chemin, dictionnaire)     #ajout de l'info de l'artcile( id et auteurs) sous forme de dico au notre dictionnaire des articles
        #print(dictionnaire.keys())
    with open(bdd, 'w', encoding='utf-8') as data:
        data.write(json.dumps(dictionnaire))                              #enregistrement du dictionnaire sous format json

    tmps2 = time.time() - tmps1  # On capte le temps d'execution du programme
    print("Temps d'execution = %f" % tmps2)
    print("Initialisation reussie")

def Dictionnaire_article():
    Dictionnaire_article=Initialisation.dictionnaire
    return Dictionnaire_article



