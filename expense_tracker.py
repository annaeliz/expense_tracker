def addexpense(tb):
    global b
    n=int(input("Enter the No. of Expense: "))
    for i in range(n):
        key=input("key: ")
        value=int(input("value: "))
        dup=value
        if key in tb:
            t=tb[key]
            value+=t
        tb[key]=value
        b=b-dup
    print("Balance amount: ",b)
    return b
def addbalance():
    global b
    nb=int(input("Enter the new balance amount: "))
    b=b+nb
    print("Total balance: ",b)
    return b
def displayexpense(tb):
   print(tb)
b=int(input("Enter the Totalbalance: "))
totalbalance={}
c=0
dup=0
while(c<4):
    c=int(input("Enter the choice: "))
    if(c==1):
        addexpense(totalbalance)
    elif(c==2):
        addbalance()
    elif(c==3):
        displayexpense(totalbalance)
    else:
        exit()
