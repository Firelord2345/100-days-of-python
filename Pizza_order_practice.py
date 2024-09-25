print("Thank you for choosing Python Pizza Deliveries!")
size = input()
add_pepperoni = input()
extra_cheese = input()
if size == 'S':
    amount = 15;
elif size == 'M':
    amount = 20;
else:
    amount = 25;

if add_pepperoni == 'Y':
    if size == 'S':
        amount += 2
    else:
        amount += 3

if extra_cheese == 'Y':
    amount += 1

print(f'Your final bill is: ${amount}.')
