import requests
import json


def carica_categorie():
    response = requests.get("https://fakeapi.net/products/categories")
    if response.status_code == 200:
        return json.loads(response.text)
    print("impossibile caricare le categorie / sito offline")
    return None


def mostra_categorie(categorie):
    print("Categorie disponibili:")
    for i, categoria in enumerate(categorie, 1):
        print(f"{i} - {categoria}")


def scegli_categoria(categorie):
    try:
        scelta_cat = int(input("Scegli una categoria (inserisci il numero): "))
    except:
        print("Devi inserire un numero!")
        return None
    
    if scelta_cat < 1 or scelta_cat > len(categorie):
        print("Scelta non valida! guarda i numeri delle categorie")
        return None
    
    return categorie[scelta_cat - 1]


def carica_prodotti(categoria):
    response = requests.get(f"https://fakeapi.net/products/category/{categoria}")
    if response.status_code == 200:
        return json.loads(response.text)
    print("Errore nel caricamento dei prodotti")
    return None


def mostra_prodotti(prodotti, categoria):
    print(f"CATEGORIA: {categoria.upper()}")
    
    if len(prodotti) == 0:
        print("Nessun prodotto disponibile in questa categoria")
        return False
    
    for prodotto in prodotti["data"]:
        print(f"ID: {prodotto['id']} - {prodotto['title']} - Prezzo: €{prodotto['price']}")
    return True


def mostra_dettaglio():
    try:
        id_prodotto = int(input("Inserisci l'ID del prodotto: "))
    except:
        print("scrivilo in numero!")
        return
    
    response = requests.get(f"https://fakeapi.net/products/{id_prodotto}")
    
    if response.status_code != 200:
        print("Prodotto non trovato")
    else:
        dettaglio = json.loads(response.text)
        print("DETTAGLIO PRODOTTO")
        print(f"ID: {dettaglio['id']}")
        print(f"Nome: {dettaglio['title']}")
        print(f"Prezzo: €{dettaglio['price']}")
        print(f"Descrizione: {dettaglio['description']}")
        print(f"Categoria: {dettaglio['category']}")
        print(f"Brand: {dettaglio['brand']}")


def chiedi_continua():
    continua = input("Vuoi vedere altre categorie? (si/no): ").strip().lower()
    if continua == "no":
        print("programma terminato")
        return True
    return False


def chiedi_dettaglio():
    azione = input("Vuoi vedere il dettaglio di un prodotto? (si/no): ").strip().lower()
    if azione == "si":
        mostra_dettaglio()



fine = False

while not fine:
    categorie = carica_categorie()
    
    if categorie == None:
        fine = True
    else:
        mostra_categorie(categorie)
        categoria_scelta = scegli_categoria(categorie)
        
        if categoria_scelta != None:
            prodotti = carica_prodotti(categoria_scelta)
            
            if prodotti != None:
                if mostra_prodotti(prodotti, categoria_scelta):
                    chiedi_dettaglio()
                    fine = chiedi_continua()


