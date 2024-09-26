def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
operations={
    '+':add,
    '*':multiply
}
def calculator():
    num1=int(input("Enter the number:"))
    for i in operations:
        print(i)
    should_continue=True
    while should_continue==True:
       op=input("Enter the operation:")
       
       num2=int(input("Enter the other number:"))
       answer=operations[op](num1,num2)
       print(f"Enter a no.{answer}")
       x=input("To continue or not yes or no \n")
       if x=='no':
           num1=answer
           print(num1)
           should_continue=False
           calculator()
           
           
calculator()