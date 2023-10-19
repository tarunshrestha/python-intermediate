# import csv
# with open('weather_data.csv') as Data:
#     data = csv.reader(Data)
#     temperatures= []
#     for i in data:
#         if i[1] != 'temp':
#             temperatures.append(int(i[1]))   #TO make it list
#     print(temperatures)

import pandas

# get data in columns
data = pandas.read_csv('weather_data.csv')
type = type(data['temp'])  # data type
read = data['temp']  # data.temp
dict = data.to_dict()  # To make it dictionary
list = data['temp'].to_list()  # To make it list
length = len(data['temp'].to_list())  # To make it len
avg = sum(list) / len(list)  # min = data['temp'].mean()
max = max(data['temp'])  # data['temp'].max()

# get data in row
d = data[data.day == 'Monday']
m = data[data.temp == data.temp.max()]
specific = d.temp
c2f = (specific * 9 / 5) + 32  # celcius to fahrenheit

door = {
    'name': ['hina','kima', 'dor'],
    'price': [10, 20, 30]
}

data2 = pandas.DataFrame(door)
print(data2)
# create csv = data2.to_csv('newdata.csv')
