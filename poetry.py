import random

poem = '''How doth the little crocodile
     Improve his shining tail,
And pour the waters of the Nile
     On every golden scale!

How cheerfully he seems to grin,
     How neatly spreads his claws,
And welcomes little fishes in,
     With gently smiling jaws!'''


def lines_printed_backwards(lines_list):
    '''This function takes in a list of strings
    containing the lines of your poem as arguments and will print the poem
    lines out in reverse with the line numbers reversed.'''
    #TODO: Reverse the list.
    lines_list.reverse()
    print(lines_list)
    #TODO: Use for loop to print out items in list.
    pass

def lines_printed_random(lines_list):
    '''Function which will randomly select lines from a list of strings and print them out in random order.'''
    i = 0
    for lines in poem:
        i+=1

# with open('poetry.py', 'r') as poem:
#     randomLine = poem.readlines()[wordSelect]
    randomline = random.choice(poem)
    print(randomline)
    pass


def my_custom_function():
    '''Does something of my choosing. TODO: comment later'''
    pass

#testing code
#TODO: get poem string into list of lines.
lines_list = poem.split("\n")
lines_printed_backwards(lines_list)
lines_printed_random(lines_list)

#lines_printed_backwards()
#lines_printed_random()
