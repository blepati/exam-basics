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

def copy_mechanism():
    pass

def controller(arg):
    if len(sys.argv) == 2:
        warning_message()
    else:
        print_description()


controller(sys.argv)
