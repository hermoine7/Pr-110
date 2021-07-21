import plotly.figure_factory as ff
import pandas as pd
import statistics
import random

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

mean=statistics.mean(data)
print("population mean: ", mean)

def findMean():
    dataset=[]
    for i in range(0,30):
        ran=random.randint(0,len(data))
        v=data[ran]
        dataset.append(v)
    mean2=statistics.mean(dataset)
    return(mean2)

def  plotGraph(meanList):
    graph=ff.create_distplot([meanList], ["reading time"], show_hist=False)
    graph.show()

def setup():
    meanList = []
    for i in range(0,100):
        means=findMean()
        meanList.append(means)
    plotGraph(meanList)
    mean3=statistics.mean(meanList)
    print("sampling mean: ", mean3)

setup()