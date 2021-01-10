
# -*- coding: utf8 -*-

#Importation des modules
import os, sys, csv, os.path, re, json, pathlib, time
from os import getcwd, chdir, mkdir, path
from fnmatch import fnmatch
from sys import argv







class Initialisation():
    """ Cette classe fait le traitement des fichiers. elle recupere les auteurs et l'identifiant des articles
    Les aueteurs sont classés dans un fichier jeson dont les clés sont les identifiants des articles; Quant
    aux articles ils sont également dans un fichier jeson mais les clés sont les identifiant de l'article
    l'ayant cité.

    """

    #def __init__(self):

        #self.chemin =chemin
        #self.article=nom_fichier_articles
        #self.reference=nom_fichier_references


    def creer_fichier_json(self,nom_fichier, dictionnaire):
        """creation du fichier texte des citations"""

        #dossier = path.dirname(__file__)
        dossier =os.path.dirname(os.path.abspath(__file__)) #chemin absolu du fichier en cours d'execution
        bdd = path.join(dossier, nom_fichier)
        with open(bdd, 'w', encoding='utf-8') as donnees:
            donnees.write(json.dumps(dictionnaire))
        return bdd






    def recherche_chemin(self):
        """Cette fonction renvoit le chemin relatif de tous les fichiers abs de .\hep-th-abs"""

        liste_chemin = []
        chemin = ".\hep-th-abs"
        #chemin1 = os.path.dirname(os.path.abspath(__file__))
        for path, dirs, files in os.walk(chemin):
            for dossier in dirs:
                nv_chemin = os.path.normpath(os.path.join(chemin,dossier))  # on concatene le chemin avec le dossier et on normalise le nouveau chemin obtenu
                # print(nv_chemin)
                for path, dirs, files in os.walk(nv_chemin):
                    for fichiers in files:
                        # compteur+=1
                        data = []
                        nv_chemin2 = os.path.normpath(os.path.join(nv_chemin,fichiers))  # on concatene le nouveau chemin avec le fichier et on normalise le nouveau chemin obtenu
                        if os.path.isfile(nv_chemin2):  # verification de l'existence du fichier
                            liste_chemin.append(nv_chemin2)
        return liste_chemin



    def recherche_ligne_auteurs(self, chemin):
        """ Cette fonction retourne dans un article donné les lignes où se trouve le nom des auteur"""


        if os.path.isfile(chemin):
            with open(chemin, 'r', encoding="cp1252") as f:
                data = f.read()
                # print(f.encoding)
                if "Authors" in data:
                    first = data.split("Authors:", 1)[1]  ###On prend ce qui suit Auteurs
                    second = first.split("Comments:", 1)[0]  ###On prend tout ce qui vient avant Comments

                    second = second.split("\n")
                    second = second[0] + "," + second[1]
                    ligne_des_auteurs = second

                elif "Author" in data:
                    first = data.split("Author:", 1)[1]  ###On prend ce qui suit Auteurs
                    second = first.split("Comments:", 1)[0]  ###On prend tout ce qui vient avant Comments

                    second = second.split("\n")
                    second = second[0] + "," + second[1]
                    ligne_des_auteurs = second
                # print(chemin)

                return ligne_des_auteurs


    def liste_auteurs(self, ligne_des_auteurs):
        """  Cette fonction traite la ligne des auteurs de facon à n'avoir que les noms des auteurs en supprimant tous les caracteres indesirables.
          Elle gèrer les abreviations et supprime les les "And", "and", "et" qu'on pourrait rencontrer dans la phrase."""

        # ce code enleve tous les mots à l'interieur d'une parenthèse ainsi que les parenthèses elles meme.
        p = re.compile(r'\([^)]*\)')
        nv_phrase = re.sub(p, '', ligne_des_auteurs)

        p = re.compile(r'\([^)]*')
        nv_phrase = re.sub(p, '', nv_phrase)

        if ")" in nv_phrase:  # On remplace d'eventuelles parentheses ouverte par rien ""
            nv_phrase = nv_phrase.replace(")", "")

        if ", and " in nv_phrase:  # On remplace les "and et "And" par des virgules
            nv_phrase = nv_phrase.replace(", and ", ", ")

        if " and " or " And " in nv_phrase:  # On remplace les "and et "And" par des virgules
            nv_phrase = nv_phrase.replace(" and ", ", ")
            nv_phrase = nv_phrase.replace(" And ", ", ")

        # p = re.compile(r' ,')
        # nv_phrase = re.sub(p, '', nv_phrase)

        if ":" in nv_phrase:  # On suppprime les deux points ":"
            nv_phrase = nv_phrase.replace(":", "")

        if "Authors" or "authors" or "Author" or "author" in nv_phrase:  ##On supprime les "Authors" or "Authors:" or"Author:" or "Author" en les remplacant par rien ""
            nv_phrase = nv_phrase.replace("Authors", "")
            nv_phrase = nv_phrase.replace("authors", "")
            nv_phrase = nv_phrase.replace("Author", "")
            nv_phrase = nv_phrase.replace("author", "")

        if "." in nv_phrase:  # Gestion des noms ecrits sous form: "A.A. Bordon" sans espace entre les deux A.
            nv_phrase = nv_phrase.replace(".", ". ")

        nv_phrase = nv_phrase.replace("  ", " ")
        nv_phrase = nv_phrase.replace(". -", ".-")
        nv_phrase = nv_phrase.title()  # Les premieres lettre des nom en majuscule

        liste_des_auteurs_non = nv_phrase.split(',')  # On decoupe la ligne comportant le nom des auteurs en mot
        liste_des_auteurs = []
        for nom in liste_des_auteurs_non:  # On enleve les espaces en debut et en fin de chaque nom
            if nom != "":
                nv_nom = nom.strip()
                liste_des_auteurs.append(nv_nom)
        return liste_des_auteurs

    def dictionnaire_par_article(self, liste_des_auteurs, chemin, dictionnaire):
        """Cette fonction cree un dictionnaire"""

        nom_fichier = os.path.basename(chemin)  # on prend le dernier element du chemin, il s'agit du fichier avec son extension ".abs"
        id_fichier = nom_fichier[0:len(nom_fichier) - 4]  # on retire l'extension ".abs"
        dictionnaire[id_fichier] = liste_des_auteurs
        return dictionnaire



    def Dictionnaire_citations(self):
        root = "../"
        pattern = "*hep-th-citations"
        Dictionnaire_citation = {}
        i = 0
        for path, subdirs, files in os.walk(root):
            for name in files:
                if fnmatch(name, pattern):

                    chemin_fichier_citations = os.path.join(path, name)
                    with open(chemin_fichier_citations, "r", encoding="utf-8") as citation:
                        cle = 1
                        for lignes in citation:
                            # liste=[]
                            # liste.append(lignes[9:15])
                            Dictionnaire_citation[cle] = [lignes[0:7], lignes[8:15]]
                            cle += 1
                    return Dictionnaire_citation


if __name__=="__main__":

    tmps1 = time.time()                                                                      # On capte le temps au debut



    #Variables
    chemin="./hep-th-abs"
    dictionnaire = {}



    a=Initialisation()
    liste_chemin = a.recherche_chemin()                                                     # liste des chemins des fichiers abs dans le dossier initial




    for chemin in liste_chemin:
        ligne_des_auteurs = a.recherche_ligne_auteurs(chemin)                               # constitution de la liste des auteurs pour chaque fichier
        liste_des_auteurs = a.liste_auteurs(ligne_des_auteurs)
        dictionnaire = a.dictionnaire_par_article(liste_des_auteurs, chemin, dictionnaire)  # ajout de l'info de l'artcile( id et auteurs) sous forme de dico au notre dictionnaire des articles
    a.creer_fichier_json("articles.json", dictionnaire)
    a.creer_fichier_json("references.json", a.Dictionnaire_citations())

    tmps2 = time.time() - tmps1                                                             # On capte le temps d'execution du programme
    print("Initialisation effectuée avec succès")
    print("Temps d'execution = %f" % tmps2)










