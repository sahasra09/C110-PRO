
import plotly.express as px
import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
temp_list = df["reading_time"].tolist()
mean = statistics.mean(temp_list)
print("population Mean -",mean)
standard_Deviation = statistics.stdev(temp_list)
print("population Standard Deviation -", standard_Deviation)
#
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(temp_list)-1)
        value = temp_list[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    #print("Mean -",mean)
    standard_Deviation = statistics.stdev(dataset)
    #print("Standard Deviation -", standard_Deviation)
    return mean

def show_fig(list):
    mean = statistics.mean(list)
    fig = ff.create_distplot([list],["READING TIME"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


def main():
    mean_list=[]
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
        mean = statistics.mean(mean_list)
       
    print("Mean of sample Distribution : " ,mean)
    show_fig(mean_list)

main()

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()