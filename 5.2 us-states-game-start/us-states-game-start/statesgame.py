import turtle,pandas
screen = turtle.Screen()
screen.title('U.S STATE GAME')
image ='5.2 us-states-game-start/us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('5.2 us-states-game-start/us-states-game-start/50_states.csv')
states = data['state'].tolist()
state_xcor =data['x'].tolist()
state_ycor = data['y'].tolist()
name = turtle.Turtle()
name.hideturtle()
name.penup()
#state_coor=data[data== answer] check if the answer
# is in the list and use the answer as index to check the coor
# of the answer
# e.g state_cor.x or state_cor.y will give the state coord in the map
# in the turtle.goto((int(state._cor.x), int(state_cor.y)))





correct=0
questions= 0
answer_lst=[]
while questions != 50:
    answer = screen.textinput(title=f'Guess correct {correct}/50', prompt="What's another state's name").title()
    if answer == 'Exit':
        missing=[state for state in states if state not in answer_lst]
        new_data = pandas.DataFrame(missing)
        new_data.to_csv('tolearnstates.csv')
        break
    for state in states:
        if answer == state:
            inx=states.index(state)
            state_cor= (state_xcor[inx],state_ycor[inx])
            name.goto(state_cor)
            name.write(state, align='center', font=('Arial',8,'bold'))
            correct += 1
            answer_lst.append(answer)
        
    questions+=1



        
