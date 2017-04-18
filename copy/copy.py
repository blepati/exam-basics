# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

import sys

def print_description():
    print("copy [source] [destination]")

def warning_message():
    print("No destination provided")

"""def content_to_copy():
    source =  sys.argv[2]
    try:
        content = open("source", "r")
        text = content.readlines()
        content.close()
        return text
    except FileNotFoundError:
        print("I can't find your file")

def paste_the_content():
    destination = sys.argv[3]
    destination.write(content_to_copy(text))"""


def controller(arg):
    if len(sys.argv) == 2:
        warning_message()
    else:
        print_description()


controller(sys.argv)
