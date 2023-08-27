import random 
ls= {"hello":["hello" ,"hi","good mording " , "nice to meet "] ,"bye":["i see you later" ,"i think you need the break" , "how may i hep you"]}

def engine (inp):
    st = str(inp).lower()
    if  st not in ls :return "Sorry I can't Understand what you what to say"
    
    datalist = ls[st]
    
    return( random.choice(datalist))
print("hell Im AI model enter the Message for chat with me.\nFor exit enter e only")
while(True):
    inp = str(input("\t\t\t"))
    if(inp in ['e',"E"]):break
    print(engine(inp))
    

    