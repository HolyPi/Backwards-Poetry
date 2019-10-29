poem = '''If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!'''


def lines_printed_backwards(lines_list):
    '''This function takes in a list of strings
    containing the lines of your poem as arguments and will print the poem
    lines out in reverse with the line numbers reversed.'''
    #TODO: Reverse the list.
    lines_list.reverse()
    print(lines_list)
    #TODO: Use for loop to print out items in list.
    pass

def lines_printed_random():
    '''Function which will randomly select lines from a list of strings and print them out in random order.'''
    pass

def my_custom_function():
    '''Does something of my choosing. TODO: comment later'''
    pass

#testing code
#TODO: get poem string into list of lines.
lines_list = poem.split("\n")
lines_printed_backwards(lines_list)

#lines_printed_backwards()
#lines_printed_random()
