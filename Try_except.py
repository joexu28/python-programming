try:
    age = int(input("age: "))
    income = 10000
    risk = income / age
    print(age)
    print(risk)
except ZeroDivisionError:
    print("Age can not be zero")
except ValueError:
    print("Invalid Value")
