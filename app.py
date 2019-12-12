#print("Joe XU")
#print('o----o')
#print(' |||| ')
#print('*' * 10)

#high_income = True
#good_credit = True
#if (high_income and good_credit):
#    print ('elgible for loan')
#if (high_income or good_credit):
#    print ('still elgible for loan')

#temperature = 30
#if temperature > 30:
#    print ("it is a hot day")
#else:
#    print ("it is not a hot day")

#name = input('please give your name: ')
#if (len(name) < 3):
#    print('name must be at least 3 characters')
#elif (len(name) > 50):
#    print ('name can be a maximum of 50 characters')
#else:
#    print ('thank you')

weight = int(input ("Weight: "))
L_K = input ("(L)bs or (K)g: ")
if L_K.upper() == 'L':
    weight = weight * 0.45
    print (f"your weight is {weight}KG")
elif L_K.upper() == 'K':
    weight = weight / 0.45
    print (f"your weight is {weight}Lbs")


numbers = [5, 6, 9, 1, 2]
numbers.sort()
print(numbers)
