# a=input()
# print(type(a))
# print("Hello\"Hi\"jo")
# print('Joel'[0])
# name="Joel"
# print(f"Hi {name}")
# a=20/3
# print(f"{a:.2f}")
# year=int(input())
# if(year%4==0):
#      if(year%100==0):
#           if year % 400 == 0:
#             print("It's a leap year")
#           else:
#             print("It's not a leap year")
     
#      else:
#         print("It's a leap year")        

# else:
#      print("Its not a leap year")
import random
# random_no=random.randint(1,10)
# randi=random.uniform(0,1)
# print(randi)
# a=[1,2,3,4,5]
# a.append(12)
# print(a)
# b=[1,3,5,2]
# b.sort()
# print(b)
a=[1,2,3,4,5]
# b=[6,7,8]
# a.extend(b)
# z=a.insert(1,23)
# a.sort(key=None,reverse=False)
# print(a)
# students = [("John", 90), ("Jane", 85), ("Dave", 90)]
# students.sort(key=lambda x: (x[1], x[0]))  # Sort by score, then by name
# print(students)  # Output: [('Jane', 85), ('Dave', 90), ('John', 90)]

# print(a.index(4))
z=random.choice(a)
random.shuffle(a)
print(a)