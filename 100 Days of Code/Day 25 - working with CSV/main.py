import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
score = 0
title = "Guess the State"

while len(all_states) > 0:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()
    if answer_state in all_states:
        score += 1
        title = f"{score}/50 States Correct"
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        all_states.remove(answer_state)
    if answer_state == "Exit":
        new_data = pandas.DataFrame(all_states)
        new_data.to_csv("states_to_learn.csv")
        break
