"""
Program dedicated for people who don't know what to eat today!

***Bautegg***
"""


#from random import seed
from random import randint
import pandas as pd
def random_value():
    data = pd.read_excel(r'C:\Users\User\Documents\GitHub\random_pasza\pasza_sheet.xlsx')
    df = pd.DataFrame(data)
    print(df)
    print('ILE: ',len(df.place))
    #seed(0)
    rand_value = randint(0, len(df.place)-1) # generate random number (from a, to b)
    print("Rand value: ", rand_value)
    #
    # places = dict({1: "Indian", 2: "China", 3: "Pizza", 4: "Burger", 5: "Sushi"})
    #
    # print(places[rand_value])
    print(df.iloc[rand_value,0])


random_value()

