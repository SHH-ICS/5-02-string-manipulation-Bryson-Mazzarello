import time; inp = input();import os; os.system('clear'); prnt = ""
def timer(x):
    time.sleep(x/len(inp)*2)
for i in range(len(inp)):
    os.system('clear')
    print(inp[0:i+1],end='\r'); timer(2)
for i in range(len(inp)):
    prnt=prnt+inp[len(inp)-i-1]; print(prnt,end='\r'); timer(2.5)
    os.system('clear')
for i in range(len(inp)):
    prnt=""
    for l in range(round((len(inp)-i)/1.9)):
        prnt=prnt+" "
    print(prnt,inp[0:i+1],prnt); timer(0.02*len(inp)+3)
time.sleep(2);os.system('clear'); print("Your welcome for the preformance by the goat, Bryson")
