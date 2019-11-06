import random

poem = '''How doth the little crocodile
     Improve his shining tail,
And pour the waters of the Nile
     On every golden scale!

How cheerfully he seems to grin,
     How neatly spreads his claws,
And welcomes little fishes in,
     With gently smiling jaws!'''

lines_list = poem.split("\n")

def lines_printed_backwards(lines_list):
    '''This function takes in a list of strings
    containing the lines of your poem as arguments and will print the poem
    lines out in reverse with the line numbers reversed.'''
    # lines_list.reverse()

    index = len(lines_list)
    lines_list.reverse()
    for line in lines_list:
        print(f"{index} {line}")
        index -=1
    # for i in range(len(lines_list)):
    #     print(i, end = " ")
    #
    #     print(lines_list[i])



def lines_printed_random(lines_list):
    '''Function which will randomly select lines from a list of strings and print them out in random order.'''

    i = 0
    for line in lines_list:
        randomLine = random.choice(lines_list)
        print(randomLine)
        i+=1





def lines_Irregular(lines_list):
    '''Irregulates words'''
    string = poem
    # reversal = ' '.join(reversed(string))
    # print(reversal)
    Irregular = string.swapcase()
    print(Irregular)




lines_printed_backwards(lines_list)
# lines_Irregular(lines_list)
# lines_printed_random(lines_list)
