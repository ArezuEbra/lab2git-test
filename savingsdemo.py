import sys # to use sys (inbuilt-module in python's standard library) we need to import it first
import argparse
# but every file in python is a module itself that can be reused by other programs
# variables:
#annual_rate = 0.05 # assignment statement
#total = 0
#total_years = 4

# after one year

# total = total + 6000 ..... total is redefined to have a new value
# total = total + total * annual_rate

# after two years

# total = total + 6000
# total = total + total * annual_rate
# : reflects the begginning of a block that is part of a for unit
# this block is defined by the indentation in python
def calculate_savings(amount, annual_rate, total_years):
    """
    Calculates savings after total_years given annual 
    saving amount and annual rate
    """ # this is a function
    history = []
    total = 0

    for year in range(total_years): # using range, loop starts at 0
        total = total + amount
        total = total * (1 + annual_rate)
        total = round(total, 2) # rounds up the decimals to 2 decimals
        history.append(total)   # put a dot after the name to get a list of options
        print(f"Total value after {year + 1}: {total} ") #translate numerical value to text
    
    return history

# substitute the value of the year in the string with {} and f 
# f before the first ""
# {year} -> 0 & 1 , but {year +1} -> 1, 2 when using range
# print("Total value after 2 years", total)
# print(sys.argv) 
# print(__name__)

if __name__ == "__main__":

    try:
        amount = int(sys.argv[1]) # using try, execpt indexerror, when running code and having indexerror, it goes through execpt block and execute the code there
        rate = float(sys.argv[2]) # int, float converts strings to numbers
        year = int(sys.argv[3])
    except IndexError:
        print("Usage: savingsdemo.py amount rate year")
        exit()
# exits the program and will not continou with the next line
# argv is a list that will contain the parameters u pass on from command line into the code
# print("final value", calculate_savings(amount, rate, year)[-1])
