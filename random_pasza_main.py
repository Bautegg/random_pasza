"""
Program dedicated for people who don't know what to eat today!

***Bautegg***
"""



from random import randint
import pandas as pd
def random_value():

    option = input('What do you want to do? * reset / rand *: ')

    print(option)
    if option == 'reset':
        path = r'/home/bautegg/Documents/GitHub/random_pasza/pasza_sheet.xlsx'
        data = pd.read_excel(path)  #load original file
        df = pd.DataFrame(data)
        df.to_excel('pasza_sheet_work.xlsx', index=False) #save original rows to work file
        print(df)
        random_value()
    elif option == 'rand':
        path = r'/home/bautegg/Documents/GitHub/random_pasza/pasza_sheet_work.xlsx'
        data = pd.read_excel(path)  #load working file
        df = pd.DataFrame(data)
        print(df)
        count_rows = len(df.place)
        rand_value = randint(0, count_rows - 1)  # generate random number (from first, to last row)
        print("Rand value: ", rand_value)
        print('** Today you will eat: **',df.iloc[rand_value, 0])
        df = df.drop([rand_value])
        print(df)
        df.to_excel('pasza_sheet_work.xlsx', index=False) #save file without drawed position
    else:   #if user provide invalid input go to the begining of program
        random_value()

random_value()


