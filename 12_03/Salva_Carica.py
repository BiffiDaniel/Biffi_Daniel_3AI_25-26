def StampaMenu():

    print(" ------------- MENU --------------")

    print("Scegli: ")
    print("1) - Inserisci nuovo film")
    print("2) - Visualizza fil inseriti")
    print("3) - Modifica un film")
    print("4) - Elimina un film")
    print("0) - terminare il programma")
 
def SceltaUtente():
    corretto = False
    while not corretto:
        try:
            scelta = int(input("Inserisci la tua scelta: "))
            if scelta < 0 or scelta > 4:
                print("Scelta non valida")
                corretto = False
            else:
                corretto = True  
                return scelta          
        except:
            print("Formato scelta non valida")
            corretto = False
def chiediNomeFilm(film):
    corretto = False
    while not corretto:
        nome = input("Inserisci il nome del film: ").strip().title()
        if len(nome) == 0 or nome in film:
            print("Nome film non valido")
            corretto = False
        else:
            corretto = True
    return nome

def chiediPosizione(f):
    corretto = False
    while not corretto:
        try:
            scelta = int(input("Indica il numero del indice per modificare un film : "))
            if scelta < 1 or scelta > len(f):
                print("Numero indice non valido")
                corretto = False
            else:

                return scelta  

        except:

            print("Scrivi in forma numerica ")

            corretto = False

def archivioPieno(film):
    if len(film)==0:
        print("archivio vuoto")
        return False
    else: 
        return True


def VisualizzaFilm(f):
    if archivioPieno(film):
        for i,f in enumerate(f):
            print(f"{i+1} - {f}")
def SalvaFile (percorso, lista):
    file = open (percorso, "w", encoding="utf-8")
    for f in lista:
        file.write (f + "|")
    file.close()

def CaricaFile (percorso):
    try:

        file = open (percorso, "r", encoding="utf-8")
        file = file.read()
        archivio = file.split ("|")
        archivio.pop ()

        return archivio

    except:

        return []
 
film = []
film = CaricaFile ("./risultati.txt")
fine = False

while not fine:
    StampaMenu()
    s = SceltaUtente()
    if s == 1:
        n = chiediNomeFilm (film)
        film.append (n)
    elif s == 2:
        VisualizzaFilm(film)
    elif s == 3:
        if archivioPieno(film):
            VisualizzaFilm(film)
            posizione = chiediPosizione(film)
            nome = chiediNomeFilm(film)
            film[posizione-1] = nome

    elif s == 4:
        if archivioPieno(film):
            VisualizzaFilm(film)
            posizione = chiediPosizione(film)
            film.pop(posizione-1)
    elif s == 0:
        print("Programma terminato")
        fine = True
    SalvaFile ("./risultati.txt", film)

 