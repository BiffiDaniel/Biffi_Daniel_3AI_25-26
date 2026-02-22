import requests
import json
fine=False
while not fine:
    Pokemon = input("Inserisci il nome del pokemon: ").upper()
    x = requests.get(f"https://pokeapi.co/api/v2/pokemon/{Pokemon}")
    name=requests.get(f"https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
    if x.status_code != 200:
        print("Pokemon non trovato/sito offline")
 
    else:
           
 
        Info = json.loads(x.text)
        peso=Info["weight"]
        peso=peso/10
        altezza=Info["height"]
        altezza=altezza/10
        link=Info["sprites"]["other"]["home"]["front_default"]
       
       
        print(f"{Pokemon}: altezza = {altezza} metri ;  peso = {peso} kg ;abilità principale = {Info["abilities"][0]["ability"]["name"]} ; numero sul pokedex = {Info["id"]} ")
        print(f"\033]8;;" + link + "\033\\Clicca qui per vederla\033]8;;\033\\")
        sh=input("vuoi vedere la sua versione shiny? (si no )").strip().lower()
        if sh=="si":
            shiny= link=Info["sprites"]["other"]["home"]["front_shiny"]
            print(f"\033]8;;" + link + "\033\\Clicca qui per vedere la versione shiny \033]8;;\033\\")
            ancora=input("vuoi vedere un altro pokemon? (si no)").strip().lower()
            if ancora=="no":
                fine =True
            else:
                fine=False
        else:
            print("sarà per la prossima ...  ")
 
            ancora=input("vuoi vedere un altro pokemon? (si no)").strip().lower()
            if ancora=="no":
                fine =True
            else:
                fine=False