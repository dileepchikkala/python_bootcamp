import turtle
import pandas

screen = turtle.Screen()
screen.title("u.s state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
  answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt= "what's the another state name?").title()

  if answer_state == "Exit":
    missing_states = []
    for state in all_states:
      if state not in guessed_state:
        missing_states.append(state)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    #print(missing_states)
    break
 
  if answer_state in all_states:
    guessed_state.append(answer_state)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)