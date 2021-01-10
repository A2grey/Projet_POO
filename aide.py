# -*- coding: utf8 -*-
from sys import argv


class Aide():

    def f1(self):
        """Communauté"""

        print("")
        print(
            "Veillez indiquer une operation que vous voulez que votre application 'communaute' fasse pour vous avec les éventuels arguments")
        print("")
        print("Vous pouvez par exemple faire:")
        print("./communaute.py aide                     Pour savoir comment fonctionne  l'application")
        print("./communaute.py init                     Pour initialiser l'application")
        print("./communaute.py cite Einstein            Pour avoir la liste de tous les auteurs cité par Einstein")
        print(
            "./communaute.py influence Einstein       Pour avoir la liste de tous les auteurs qui influencent Einstein")
        print(
            "./communaute.py influence_par Einstein   Pour avoir la liste de tous les auteurs qui sont influencé par Einstein")
        print("./communaute.py communautes Einstein 5   Pour avoir la liste du communaute de profondeur 5 de Einstein")

    def f2(self):
        """Aide"""

        print("")
        print("L'opération d'aide ne prend aucun argument")
        print("")
        print("Vous devez juste faire:")
        print("./communaute.py aide                     Pour savoir comment fonctionne  l'application")
        print("")

    def f3(self):
        """Init"""

        print("")
        print("L'opération d'initialisation ne prend aucun argument")
        print("")
        print("Vous devez juste faire:")
        print("./communaute.py init                     Pour initialiser l'application")
        print("")
        print("Besoin d'aide?")
        print("Tapez:")
        print("./communaute.py aide                     Pour savoir comment fonctionne  l'application")

    def f4(self):
        """Cite"""

        print("")
        print("L'opétation 'cite' prend un argument(le nom de l'auteur qui cite)")
        print("")
        print("Vous pouvez par exemple faire:")
        print("./communaute.py cite Einstein            Pour avoir la liste de tous les auteurs cité par Einstein")

    def f5(self):
        """Influence"""

        print("")
        print("L'opétation 'influence' prend un argument(le nom de l'auteur qui influence")
        print("Vous pouvez par exemple faire:")
        print(
            "./communaute.py influence Einstein       Pour avoir la liste de tous les auteurs qui influencent Einstein")

    def f6(self):
        """influence_par"""

        print("")
        print("L'opétation 'influence_par' prend deux arguments(le nom de l'autheur et la profondeur")
        print("Vous pouvez par exemple faire:")
        print(
            "./communaute.py influence Einstein       Pour avoir la liste de tous les auteurs qui influencent Einstein")

    def f7(self):
        """communautes"""

        print("")
        print("L'opétation 'communautes' prend deux arguments(le nom de l'autheurs et la profondeur de la communauté")
        print("")
        print("Vous pouvez par exemple faire:")
        print("./communaute.py communautes Einstein 5   Pour initialiser l'application")
        print("")
        print("Veillez choisir l'une des opétations suivantes: aide, init, influence, cite, influence, communautes")
        print("Besoin d'aide?")
        print("Tapez:")
        print("./communaute.py aide                     Pour savoir comment fonctionne  l'application")

    def f8(self):
        print("")
        print("L'opération 'communautes' prend deux arguments")
        print("")
        print("Vous pouvez par exemple faire:")
        print("./communaute communautes Einstein 5   Pour avoir la liste du communaute de profondeur 5 de Einstein")
        print("")

    def f9(self):
        print("L'application 'communaute' ne fait pas l'opertaion que vous avez demandé")
        print("")
        print("Vous pouvez faire l'une des opération ci-dessous:")
        print("./communaute aide                     Pour savoir comment fonctionne  l'application")
        print("./communaute init                     Pour initialiser l'application")
        print("./communaute cite Einstein            Pour avoir la liste de tous les euteurs cité par Einstein")
        print(
            "./communaute influence Einstein       Pour avoir la liste de tous les euteurs qui influencent Einstein")
        print(
            "./communaute communautes Einstein 5   Pour avoir la liste du communaute de profondeur 5 de Einstein")

    def f10(self):
        print("")
        print(
            "Veillez choisir l'une des opétations suivantes: aide, init, influence, cite, influence, communautes")
        print("Besoin d'aide?")
        print("Tapez:")
        print(
            "./communaute aide                     Pour savoir comment fonctionne  l'application")





