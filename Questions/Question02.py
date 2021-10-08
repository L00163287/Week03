"""
#
# @File         : Question02.py
# @Created      : 2021-10-08 10:20
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  :
#
"""

import random

if __name__ == "__main__":
    '''
       Main method of application 

       Question 02

       Parameters:
        none

       Returns:
        none
    '''

    week1 = ["Joe", "John", "Jane", "Mick", "Mary", "Ann", "Rick", "John", "Aine", "Brenda"]  # List of players
    week1Numbers = []  # Empty List of numbers

    # Adding 10 random 10 numbers to list of numbers using loop
    for i in range(0, 10):
        week1Numbers.append(random.randint(0, 20))

    lottoNumbers1 = {}  # Empty Dictionary
    # Adding Data to dictionary using loop
    for i in range(0, 10):
        lottoNumbers1[week1[i]] = week1Numbers[i]

    week2 = ["Jack", "Mary", "Phil", "John", "Pat", "Joe", "Luke", "Bill", "Ben", "Nathan"]
    week2Numbers = []  # Empty List of numbers
    # Adding 10 random 10 numbers to list of numbers using loop
    for i in range(0, 10):
        week2Numbers.append(random.randint(0, 20))

    lottoNumbers2 = {}  # Empty Dictionary
    # Adding Data to dictionary using loop
    for i in range(0, 10):
        lottoNumbers2[week2[i]] = week2Numbers[i]

    # Find the intersection in the lists to find out who bought tickets on both weeks
    commonBuyers = []
    for i in range(0, 10):
        for j in range(0, 10):
            if week1[i] == week2[j]:
                commonBuyers.append(week1[i])

    uniquePlayers = {}
    # for i in range(0,10):  # Players in week 1
    #     name, number = lottoNumbers1.popitem()

    print(uniquePlayers)
