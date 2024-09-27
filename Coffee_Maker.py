MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffe":18,
        },
        "cost":1.5
    },
    "latte":{
        "ingredients":{
            "water":200,
            "coffe":24,
            "milk":150
        },
        "cost":2.5
    },
}
resources={
    "water":300,
    "coffe":100,
    "milk":200,
    
}
def report_coffee(report,choice):
    if report=="y":
       if choice in MENU:
             for choice in MENU:
                t=MENU[choice]
                return t
       else:
          return"Invalid Choise"
    else:
        return "Report not requested"
def resource_suffecient(x):
        for i in x:
            if x[i]<resources[i]:
                return True
        return False   
def coffee(choice) :
    for item in choice:
       resources[item] -= choice[item]
       return resources
      
    
is_on=True
while is_on==True:
      choice=input("What would you like? (espresso/latte/cappuccino): ")
      report=input("Do you want to see the report? y/n ")
      x=report_coffee(report,choice)
      print(x)
      drink=MENU[choice]
      if resource_suffecient(drink["ingredients"]):
          print(f"Thanks for the order {choice} ")
          x=coffee(drink["ingredients"])
          print(f"{resources}")
          
      on=input("Do you want to turn on or off? ")
      if on=="off":
          is_on=False
