"""
Program dedicated for people who don't know what to eat today!

***Bautegg***
"""


from random import seed
from random import randint
def random_value():

    #seed(0)
    rand_value = randint(1, 5) # generate random number (from a, to b)
    print("Rand value: ", rand_value)

    places = dict({1: "Indian", 2: "China", 3: "Pizza", 4: "Burger", 5: "Sushi"})

    print(places[rand_value])

random_value()

