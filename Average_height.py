student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
height=0
for i in student_heights:
    height+=i
print(height)
avg=round(height/(n+1))
print(avg)