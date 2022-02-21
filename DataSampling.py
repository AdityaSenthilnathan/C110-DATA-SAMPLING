import statistics
import pandas as px
import random
import plotly.figure_factory as ff
df = px.read_csv("medium_data.csv")
data = df["claps"].tolist()



def random_set_of_mean():
    dataset = []
    for a in range (1, 30):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)


mean_list = []
for a in range(0,100):
    set_of_means = random_set_of_mean()
    mean_list.append(set_of_means)
fig = ff.create_distplot([mean_list], ["temp"], show_hist = False)
fig.show()