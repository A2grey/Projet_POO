# -*- coding: utf8 -*-

import os, csv, re
import os.path
import  pathlib
from os import path
import json
from fnmatch import fnmatch

from os import getcwd, chdir, mkdir

#Fonction de recherche des document abs et retournant les chemin.
def recherche_chemin(chemin_initial):
	liste_chemin=[]
	chemin = "./hep-th-abs"
	for path, dirs, files in os.walk(chemin_initial):
		for dossier in dirs:
			nv_chemin = os.path.normpath(os.path.join(chemin, dossier))  # on concatene le chemin avec le dossier et on normalise le nouveau chemin obtenu
			# print(nv_chemin)
			for path, dirs, files in os.walk(nv_chemin):
				for fichiers in files:
					# compteur+=1
					data = []
					nv_chemin2 = os.path.normpath(os.path.join(nv_chemin,fichiers))  # on concatene le nouveau chemin avec le fichier et on normalise le nouveau chemin obtenu
					if os.path.isfile(nv_chemin2):  # verification de l'existence du fichier
						liste_chemin.append(nv_chemin2)
	return liste_chemin





#Cette fonction retourne la ligne où se trouve le mot "Authors" ou "Author"
def recherche_ligne_auteurs(chemin):
	if os.path.isfile(chemin):
		with open(chemin,'r', encoding="cp1252") as f:
			#print(f.encoding)
			for ligne_auteurs in f:
				if "Authors"in ligne_auteurs:
					return ligne_auteurs
				elif "Author"in ligne_auteurs:
					return ligne_auteurs




#Cette fonction transforme une phrase en liste de mot, gèrer les abreviations, et supprime les les "And", "and", "et" qu'on pourrait rencontrer dans la phrase
def liste_auteurs(ligne_des_auteurs):
	#print(phrase)

	#ce code enleve tous les mots à l'interieur d'une parenthèse ainsi que les parenthèses elles meme.
	p = re.compile(r'\([^)]*\)')
	nv_phrase = re.sub(p, '', ligne_des_auteurs)

	p = re.compile(r'\([^)]*')
	nv_phrase = re.sub(p, '', nv_phrase)

	if ")" in nv_phrase: #On remplace d'eventuelles parentheses ouverte par rien ""
		nv_phrase = nv_phrase.replace(")", "")

	if ", and " in nv_phrase: #On remplace les "and et "And" par des virgules
		nv_phrase = nv_phrase.replace(", and ", ", ")

	if " and " or " And " in nv_phrase: #On remplace les "and et "And" par des virgules
		nv_phrase = nv_phrase.replace(" and ", ", ")
		nv_phrase = nv_phrase.replace(" And ", ", ")

		#p = re.compile(r' ,')
		#nv_phrase = re.sub(p, '', nv_phrase)



	if ":" in nv_phrase:  #  On suppprime les deux points ":"
		nv_phrase = nv_phrase.replace(":", "")


	if "Authors" or "authors" or "Author" or "author" in nv_phrase: ##On supprime les "Authors" or "Authors:" or"Author:" or "Author" en les remplacant par rien ""
		nv_phrase = nv_phrase.replace("Authors", "")
		nv_phrase = nv_phrase.replace("authors", "")
		nv_phrase = nv_phrase.replace("Author", "")
		nv_phrase = nv_phrase.replace("author", "")



	liste_des_auteurs_non = nv_phrase.split(',') #On decoupe la ligne comportant le nom des auteurs en mot
	liste_des_auteurs=[]
	for nom in liste_des_auteurs_non: #On enleve les espaces en debut et en fin de chaque nom
		nv_nom=nom.strip()
		liste_des_auteurs.append(nv_nom)
	return liste_des_auteurs

	#b=liste_auteurs(phraseA)
	#phraseA = ["R. Roger", "D., -J., y., Cédric", "T.Z., Camus, Mikou"]

	#Test
	#print(b)

def dictionnaire_par_article(liste_des_auteurs, chemin, dictionnaire):

	nom_fichier = os.path.basename(chemin)  # on prend le dernier element du chemin, il s'agit du fichier avec son extension ".abs"
	id_fichier = nom_fichier[0:len(nom_fichier) - 4]  # on retire l'extension ".abs"
	dictionnaire[id_fichier] = liste_des_auteurs
	return dictionnaire



def fichier_citations():
	root = "./Projet programmation"
	pattern = "*hep-th-citations"
	i = 0
	for path, subdirs, files in os.walk(root):
		for name in files:
			if fnmatch(name, pattern):
				liste = []
				chemin_fichier_citations = os.path.join(path, name)
				with open('CitationsArticles.txt', 'a') as NvCitations:
					with open(chemin_fichier_citations, "r", encoding="utf-8") as citation:
						for lignes in citation:
							lign=[lignes[0:7],lignes[8:15]]

							NvCitations.write(lign)

							liste.append(lignes.split())
						return liste


def Dictionnaire_citations():
	root = "../"
	pattern = "*hep-th-citations"
	Dictionnaire_citation={}
	i = 0
	for path, subdirs, files in os.walk(root):
		for name in files:
			if fnmatch(name, pattern):

				chemin_fichier_citations = os.path.join(path, name)
				with open(chemin_fichier_citations, "r", encoding="utf-8") as citation:
					cle=1
					for lignes in citation:

						#liste=[]
						#liste.append(lignes[9:15])
						Dictionnaire_citation[cle]=[lignes[0:7],lignes[8:15]]
						cle +=1
				return Dictionnaire_citation






