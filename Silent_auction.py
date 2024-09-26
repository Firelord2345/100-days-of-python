should_continue=True
bid={}
while should_continue==True:
    name= input("whats the name of the bidder? ")
    pay=int(input("What value of bid "))
    bid[name]=pay
    input1=input("Do you want to add a bidder?yes/no  ").lower()
    if input1=='no':
        should_continue=False
        n=max(bid,key=bid.get)
        print(f"The max value bidder {n}")
    else:
        should_continue=True 
        print('\n'*30)
    
    