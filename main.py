import turtle
import pandas as pd

# build your turtle screen
screen = turtle.Screen()
screen.setup(750,510)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # Be able to click on the map and get the coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

# import the CSV and make a list of states. list of guessed states and a list of missed states for later
state_list = pd.read_csv("50_states.csv")
all_states = state_list.state.to_list()
guessed_states = []

# create a while loop to prompt the user to guess the states, Spelling matters, case does not
while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 Guess the state",
                                    prompt= "What's another state?").title()
    # print(answer_state)
    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        missed_states_list = pd.DataFrame(missed_states)
        missed_states_list.to_csv("check.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.color("black")
        t.penup()
        state_data = state_list[state_list.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
