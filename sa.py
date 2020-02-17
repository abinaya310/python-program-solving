a="stone";
b="paper";
c="scissor";
d=input("enter the value");
e=input("enter the value");
if(d=="stone" and e=="paper"):
    print("paper wins")
elif(d=="paper" and e=="scissor"):
    print("scissor wins")
elif(d=="stone" and e=="scissor"):
    print("stone wins")
else:
    print("draw match")
    
