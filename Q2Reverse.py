# Create a program that will accept a word and output the word one letter at a time in reverse.

inp = input(); prnt = ""
for i in range(len(inp)):
    prnt=prnt+inp[len(inp)-i-1]
print(prnt)