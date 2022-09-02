import pandas



# data= pandas.read_csv('5.2 us-states-game-start/us-states-game-start/2.1 weather_data.csv')
# mx=data['temp'].max()
# print(data[data.temp == mx])
data= pandas.read_csv('5.2 us-states-game-start/us-states-game-start/4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color=data['Primary Fur Color'].to_list()
gray=fur_color.count('Gray')
black=fur_color.count('Black')
cinnamon=fur_color.count('Cinnamon')
fur_count = {'Count':[gray, black, cinnamon],'Fur color':['Gray', 'Black', 'Cinnamon']}
squirrel = pandas.DataFrame(fur_count)
squirrel.to_csv('squirrel_color_count.csv')

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()