import pandas

#Count how many grey, red, black squrriels are there and create csv file

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_num= len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_num = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_num = len(data[data["Primary Fur Color"] == "Black"])


dict = {"Fur Color": ["gray", "red", "black"],
        "Count" : [gray_num, cinnamon_num,black_num]
        }

df = pandas.DataFrame(dict)
df.to_csv("squirrel_count.csv")