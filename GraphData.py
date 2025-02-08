'''
@author: Devangini Patel

Reference: https://www.python.org/doc/essays/graphs/
'''

#create a dictionary with all the mappings
connections = {
    "Adam": {"Bob", "Minh", "Ema"},
    "Bob": {"Adam", "Dolly", "Ema"},
    "Ema": {"Adam", "Bob", "Dolly"},
    "Minh": {"Adam", "Frank", "George"},
    "George": {"Minh"},
    "Dolly": {"Bob", "Ema"},
    "Frank": {"Minh"},
}

