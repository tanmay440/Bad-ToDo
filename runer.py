import os
import sys

#========G. Vars============

x = sys.argv[0].split("main.py")[0]
games = {"tdg":"Tower defence Game/TowerDefense.exe", "kart":"Lario Cart 1/Lario Cart.exe", "fps": "Apocales/Apocales.exe", "gole.sv":"RPS/server.py", "rps": "RPS/client.py"}

#========FUNctions==========

def open(r_path, x):
    os.startfile(f"{x}{r_path}")

#=======spaggetti code======

if __name__ == "__main__":
    game_choice = input("Which game? ")
    x = sys.argv[0].split("runer.py")[0]

    while game_choice.lower().strip() not in ["tdg", "tower defence", "mario kart", "luigi kart", "lario kart", "mario cart", "luigi cart", "lario cart"]:
        game_choice = input("Invalid game. Please choose again. ")

    if game_choice in ["tdg", "tower defence"]:
        open(games["tdg"], x)

    else:    
        open(games["kart"], x)
