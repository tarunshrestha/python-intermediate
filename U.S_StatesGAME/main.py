import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S State Game')
img = './blank_states_img.gif'
turtle.addshape(img)
turtle.shape(img)
data = pandas.read_csv('50_states.csv')
guessed = []
score = 0
canplay = True

while len(guessed) < 50:
    ans_state = screen.textinput(title=f"{len(guessed)}/ 50 States", prompt="What's another state's name?").title()
    states = data['state'].to_list()  # data.state & Must be in list
    #print(ans_state)
    if ans_state == 'Exit':
        missing = []
        for state in states:
            if state not in guessed:
                missing.append(state)
        print(f'Missed States are :{missing}')
        new_data = pandas.DataFrame(missing)
        new_data.to_csv('States_TO_Learn.csv')
        break
    if ans_state in states:
        guessed.append(ans_state)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        print(ans_state)
    else:
        print('Wrong')



# TO DETECT MOUSE
# def get_mouse_click(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click)
#turtle.mainloop()

