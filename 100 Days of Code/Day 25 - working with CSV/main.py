import csv
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

with open("50_states.csv") as data_file:
    states_data = csv.reader(data_file)
    states = []
    for row in states_data:
         if row[0] != "state":
             states.append(row[0])

states_lowercase = [i.lower() for i in states]
score = 0
title = "Guess the State"


while True:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?")
    if answer_state.lower() in states_lowercase:
        states_lowercase.remove(answer_state.lower())
        score += 1
        title = f"{score}/50 States Correct"

# Niepotrzebnie zmieniałem stany do listy
# Potrzebne są współrzędne
# Oraz stany z wielkiej litery żeby je wypisać na mapie