import math

# getting input
# name = input('What is your name? ')
# color = input('what is your favorite color? ')
# print('hi ' + name )
# print('your favorite color is ' + color)

# type converter
# birth_year = input ('Birth Year: ')
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print (age)

# weight_pounds = input ('weight in pounds: ')
# weight_KG = float(weight_pounds) * 0.453592
# print ('your weight is ' + str(weight_KG))

# Strings
course = '''
Hi John,
Thanks for your support
Joe
'''
#course = "Python's course for beginner"
another = course.upper()
print(course, another)
print(len(course))
#print(course.find('P'))
#print(course.replace('beginner', 'Absolute begineers'))

if ('Python' in course):
    print ("this is a python course")
else:
    print ("this is NOT a python course")


#first = 'john'
#last = 'smith'
#message = first + ' [' + last + ' ] is a coder'
#msg = f'{first} [{last}] is a coder'
#print (message, msg)

# x=2.9
# print(round(x))
# print(abs(-2.9))
# print(math.atan(x))

good_credit = True
price = 1000000

down_payment2 = price * 0.2
if good_credit:
    down_payment = price * 0.1
    print(f"down payment is ${down_payment}")
else:
    down_payment = price * 0.2
    print(f"down payment is ${down_payment}")
