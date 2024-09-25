print("The Love Calculator is calculating your score...")
name1 = input()
name2 = input()
name=name1+name2
t=name.lower().count('t',0,len(name))
r=name.lower().count('r',0,len(name))
u=name.lower().count('u',0,len(name))
e=name.lower().count('e',0,len(name))
true=(str)(t+r+u+e)
l=name.lower().count('l',0,len(name))
o=name.lower().count('o',0,len(name))
v=name.lower().count('v',0,len(name))
e=name.lower().count('e',0,len(name))
love=(str)(l+o+v+e)
score= int(true+love)
if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40<score<=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")