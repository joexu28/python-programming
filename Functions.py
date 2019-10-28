#def greet_user(username):
#    print(f"Hi {username}")
#    print("welcome onboard")


#print("Start")
#first_name=input("what is your name: ")
#greet_user(first_name)
#print("Finish")

def greet_user1(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("welcome onboard")


print("Start")
greet_user1("John", "Smith")                        # positional arguments
greet_user1(last_name="Chur", first_name="Mary")    # keyword arguments
print("Finish")

def square(number):
    return number * number


result = square(3)
print(result)
print(square(4))

def emoji_cnv(message):
    words = message.split(" ")
    emojis = {
        ":)": "smile face",
        ":(": "sad face"
    }
    output =""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_cnv(message))
