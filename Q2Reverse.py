# Create a program that will accept a word and output the word one letter at a time in reverse.

# inp = input(); prnt = ""
# for i in range(len(inp)):
#    prnt=prnt+inp[len(inp)-i-1]
# print(prnt)

import time; inp = input(); prnt = ""
for i in range(len(inp)):
    prnt=prnt+inp[len(inp)-i-1]; print(prnt, end='\r'); time.sleep(0.6/len(inp)+0.04)