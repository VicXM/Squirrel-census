import pandas
data = pandas.read_csv("central_park_squirrel_data.csv")
color_list = data["Primary Fur Color"].to_list()
black_times = color_list.count("Black")
cinnamon_times = color_list.count("Cinnamon")
gray_times = color_list.count("Gray")

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_times, cinnamon_times, black_times]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
