#work in progress
ruch1 = str(input("Gracz 1: kamień, papier, czy nożyce? "))
while ruch1 != ("kamień" or "papier" or "nożyce"):
    ruch1 = str(input("Gracz 1: kamień, papier, czy nożyce? "))

ruch2 = str(input("Gracz 2: kamień, papier, czy nożyce? "))
while ruch1 != ("kamień" or "papier" or "nożyce"):
    ruch2 = str(input("Gracz 2: kamień, papier, czy nożyce? "))

if ruch1 == "kamień" and ruch2 == "nożyce" or ruch1 == "papier" and ruch2 == "kamień" or ruch1 == "nożyce" and ruch2 == "papier":
    czyPowtorka = str(input("Gracz 1 wygrał. Ponowić rozgrywkę? "))

if ruch2 == "kamień" and ruch1 == "nożyce" or ruch2 == "papier" and ruch1 == "kamień" or ruch2 == "nożyce" and ruch1 == "papier":
    czyPowtorka = str(input("Gracz 2 wygrał. Ponowić rozgrywkę? "))

else:
    czyPowtorka = str(input("Remis. Ponowić rozgrywkę? "))