# try except to capture exceptions

try:
    age = int(input('Age: '))
    risk = 2000/age
    print(age)
    print(risk)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print('Cannot be divided by 0')

