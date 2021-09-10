import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_name = turtle.Turtle()


score = 0
data_list = data["state"].to_list()

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in data_list:
        state_data = data[data["state"] == answer_state]
        state_name.hideturtle()
        state_name.hideturtle()
        state_name.penup()

        x = int(state_data["x"])
        y = int(state_data["y"])
        state_name.goto(x, y)
        state_name.write(answer_state)

        score += 1
        data_list.remove(answer_state)

missing_states = {
    "Missing States": data_list
}

df = pandas.DataFrame(missing_states)
df.to_csv("missing_states.csv")


turtle.mainloop()
