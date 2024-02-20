vertebrado = input()
animal = input()
tipo = input()

if vertebrado == "vertebrado":
    if animal == "ave":
        if tipo == "carnivoro":
            print("aguia")
        elif tipo == "onivoro":
            print("pomba")

    elif animal == "mamifero":
        if tipo ==  "onivoro":
            print("homem")
        elif tipo == "herbivoro":
            print("vaca")

elif vertebrado == "invertebrado":
    if animal == "inseto":
        if tipo == "hematofago":
            print("pulga")
        elif tipo == "herbivoro":
            print("lagarta")

    elif animal == "anelideo":
        if tipo == "hematofago":
            print("sanguessuga")
        elif tipo == "onivoro":
            print("minhoca")    

