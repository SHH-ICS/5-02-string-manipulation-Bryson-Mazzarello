# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.

while True:
    print("Type quit to exit, type anything else for length")
    inp = input()
    if inp == "quit":
        break
    else:
        print(len(inp))