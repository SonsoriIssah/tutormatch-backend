your_age = int(input('Enter your age: '))

if your_age >= 18: 
    print('You are old enough to learn to drive.')
else:
    years_left = 18 - your_age
    print(f'You need {years_left} more to learn to drive.')

my_age = int(input(''))
if your_age > my_age:
    age_difference = your_age - my_age
    print(f'You are {age_difference} years older than me.')
elif my_age > your_age:
    age_difference = my_age - your_age
    print(f'I am  {age_difference} years older than you.')
else:
    print('We are the same age')

a= int(input(''))
b = int(input(''))
if  a > b:
    print(f'{a} is greater than {b}')
elif a< b:
    print(f'{a} is smaller than {b}')

for i in range(100):
    if i >= 80:
        print('A')
    elif 70 >= i and i <= 79:
        print('B')
    elif  60 >= i and i <= 69:
        print('C')
    elif 50 >= i and i <= 59:
        print('D')
    else:
        print('F')

months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

users_month =input('Which month is it ').lower()
if users_month in months[8:11]:
    print('Autumn')
elif users_month in months[:2] or users_month == 'december':
    print('Winter')
elif users_month in months[2:5]:
    print('Spring')
else:
    print('Summer')

fruits = ['banana', 'orange', 'mango', 'lemon']

user_fruit = input('')

if user_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(user_fruit)
