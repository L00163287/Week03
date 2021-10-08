"""
#
# @File         : Question01.py
# @Created      : 2021-10-04 22:37
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  :
#
"""

if __name__ == "__main__":
    '''
       Main method of application 

       code to read in a student Lnumber and using a combination of the above fields print the name of the 
       modules they take and the grade they received in each module.

       Parameters:
        none

       Returns:
        none
    '''

    LNumbers = ("L12345", "L54321")  # Tuple of student numbers
    ModuleList = ["Java", "Python"]  # List of Modules
    Java = {"L12345": 40, "L54321": 70}  # Java grade dictionary
    Python = {"L12345": 69, "L54321": 58}  # Python grade dictionary
    i = 0  # Loop
    while i < 2:
        print("Student Number : {} \t".format(LNumbers[i])  # Print student number from Tuple
              + "{} ".format(ModuleList[0])  # Print Module from List
              + "Grade : {} \t".format(Java[format(LNumbers[i])])  # Print Java grade
              + ": {} ".format(ModuleList[1])  # Print Module from List
              + "Grade : {} \t".format(Python[format(LNumbers[i])])  # Print Python grade
              )
        i += 1
