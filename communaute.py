# -*- coding: utf8 -*-


from sys import argv




#class Main():

    #def condition(self):
statut = "desactivé"
nb_arguments = len(argv)

if argv[0] == "communaute.py":
    if nb_arguments == 1:
        print("")
        print( "Veillez indiquer une operation que vous voulez que votre application 'communaute' fasse pour vous avec les éventuels arguments")
        print("")
        print("Vous pouvez par exemple faire:")
        print("./communaute aide                     Pour savoir comment fonctionne  l'application")
        print("./communaute init                     Pour initialiser l'application")
        print("./communaute cite Einstein            Pour avoir la liste de tous les euteurs cité par Einstein")
        print("./communaute influence Einstein       Pour avoir la liste de tous les euteurs qui influencent Einstein")
        print("./communaute communautes Einstein 5   Pour avoir la liste du communaute de profondeur 5 de Einstein")


    if nb_arguments == 2:
        if argv[1] == 'init':
           # statut = 'initialisation activée'
            if __name__ == "__main__":
                from initialisation import Initialisation

                Initialisation()

        else:
            if argv[1] == 'aide':
                #statut = 'aide activée'
                if __name__ == "__main__":
                    from aide import Aide

                    Aide()

            else:
                if argv[1] == 'cite':
                    print("")
                    print("L'opétation 'cite' prend un argument(le nom de l'auteur qui cite")
                    print("")
                    print("Vous pouvez par exemple faire:")
                    print(
                        "./communaute cite Einstein            Pour avoir la liste de tous les euteurs cité par Einstein")
                   # statut = "desactivé"
                else:
                    if argv[1] == 'influence':
                        print("")
                        print("L'opétation 'influence' prend un argument(le nom de l'auteur qui influence")
                        print("Vous pouvez par exemple faire:")
                        print(
                            "./communaute influence Einstein       Pour avoir la liste de tous les euteurs qui influencent Einstein")
                        #statut = "desactivé"
                    else:
                        if argv[1] == 'communautes':
                            print("")
                            print(
                                "L'opétation 'communautes' prend deux arguments(le nom de l'auteur et la profondeur de la communauté")
                            print("")
                            print("Vous pouvez par exemple faire:")
                            print("./communaute communautes Einstein 5   Pour initialiser l'application")
                            #statut = "desactivé"
                        else:
                            print("")
                            print(
                                "Veillez choisir l'une des opétations suivantes: aide, init, influence, cite, influence, communautes")
                            print("Besoin d'aide?")
                            print("Tapez:")
                            print("./communaute aide                     Pour savoir comment fonctionne  l'application")
                            #statut = "desactivé"
    if nb_arguments == 3:
        if argv[1] == 'init':
            print("")
            print("L'opération d'initialisation ne prend aucun argument")
            print("")
            print("Vous devez juste faire:")
            print("./communaute init                     Pour initialiser l'application")
            print("")
            print("Besoin d'aide?")
            print("Tapez:")
            print("./communaute aide                     Pour savoir comment fonctionne  l'application")
            #statut = "desactivé"


        elif argv[1] == 'aide':
            statut = 'aide desactivée'
            print("")
            print("L'opération d'aide ne prend aucun argument")
            print("")
            print("Vous devez juste faire:")
            print("./communaute aide                     Pour savoir comment fonctionne  l'application")
            print("")

        elif argv[1] == 'cite':
            if __name__ == "__main__":
                from auteur import resultat
                resultat(argv[2])


        elif argv[1] == 'communautes':
            print("")
            print("L'opération 'communautes' prend deux arguments")
            print("")
            print("Vous pouvez par exemple faire:")
            print("./communaute communautes Einstein 5   Pour avoir la liste du communaute de profondeur 5 de Einstein")
            print("")

        else:
            print("L'application 'communaute' ne fait pas l'opertaion que vous avez demandé")
            print("")
            print("Vous pouvez faire l'une des opération ci-dessous:")
            print("./communaute aide                     Pour savoir comment fonctionne  l'application")
            print("./communaute init                     Pour initialiser l'application")
            print("./communaute cite Einstein            Pour avoir la liste de tous les euteurs cité par Einstein")
            print("./communaute influence Einstein       Pour avoir la liste de tous les euteurs qui influencent Einstein")
            print("./communaute communautes Einstein 5   Pour avoir la liste du communaute de profondeur 5 de Einstein")

    if nb_arguments == 4:
        if argv[1] == 'influence':
            if __name__ == "__main__":
                from auteur import influence
                influence(argv[2],int(argv[3]))



"""

if Main.condition=="initialisation activée":
    from initialisation import Initialisation
    Initialisation()
else:
    from aide import Aide
    Aide()


if __name__=='__main__':
    Main()

"""


