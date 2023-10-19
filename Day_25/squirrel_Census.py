import pandas

data = pandas.read_csv('Squirrel_Data.csv')

gray = len(data[data['Primary Fur Color'] == 'Gray'])
red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])
total = gray + red + black
print(f'Squirrel Colors\nGray: {gray} \nRed: {red} \nBlack: {black} \n Total: {total}')

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    "Count": [gray, red, black]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv('Squirrel_count.csv')