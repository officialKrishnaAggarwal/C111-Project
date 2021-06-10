import csv
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)
def random_set_of_mean():
    dataset=[]
    for i in range(0,30):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means = random_set_of_mean()
        mean_list.append(set_of_means)
    show_fig(mean_list)
first_stdev_start = population_mean - population_stdev
first_stdev_end = population_mean + population_stdev
second_stdev_start = population_mean - (2*population_stdev)
second_stdev_end = population_mean + (2*population_stdev)
third_stdev_start = population_mean - (3*population_stdev)
third_stdev_end = population_mean + (3*population_stdev)
    
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(meanList)
    standardDeviation = statistics.stdev(meanList)
    fig = ff.create_distplot([df], ["temp"], show_hist = False)
    fig.show()

setup()
