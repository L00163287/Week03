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

    Week1 = ["Joe", "John", "Jane", "Mick", "Mary", "Ann", "Rick", "John", "Aine", "Brenda"]  # List of players
    Week1Numbers = []  # Empty List of numbers

    # Adding 10 random 10 numbers to list of numbers using loop
    for i in range(0, 10):
        Week1Numbers.append(random.randint(0, 20))

    LottoNumbers1 = {}  # Empty Dictionary

    Week2 = ["Jack", "Mary", "Phil", "John", "Pat", "Joe", "Luke", "Bill", "Ben", "Nathan"]
    Week2Numbers = []  # Empty List of numbers
    # Adding 10 random 10 numbers to list of numbers using loop
    for i in range(0, 10):
        Week2Numbers.append(random.randint(0, 20))
