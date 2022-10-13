"""

The pseudorandom number generator is a mathematical function that generates a sequence of nearly random numbers.

It takes a parameter to start off the sequence, called the seed. The function is deterministic, meaning given the same seed,
it will produce the same sequence of numbers every time. The choice of seed does not matter.

The seed() function will seed the pseudorandom number generator, taking an integer value as an argument, such as 1 or 7.
If the seed() function is not called prior to using randomness, the default is to use the current system time in milliseconds from epoch (1970).

The example below demonstrates seeding the pseudorandom number generator,
generates some random numbers, and shows that reseeding the generator will result in the same sequence of numbers being generated.

"""

from random import seed
from random import randint
def random_value():

    #seed(0)
    rand_value = randint(1, 5) # generate random number (from a, to b)
    print("Rand value: ", rand_value)

    places = dict({1: "Hindus", 2: "Chinol", 3: "Pizza", 4: "Burger", 5: "Sushi"})

    print(places[rand_value])

# random_value()

"""
podpiąć ceny z gazetek i przepisy, ma mi zwrócić najtańsze danie
"""