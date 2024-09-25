year = int(input())
if year%4==0:
     if year%100==0:
           if year%400==0:
             print("Its leap year")
           else:
               print("Its not leap year")
     else:
         print("Its  leap year")
else :
    print("Its not leap year")