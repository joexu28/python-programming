coordinates = (1, 2, 3)
x, y, z = coordinates
print (x*y*z)

# dictionary
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("age"))

phone_number = input("Phone: ")
number_conversion = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
#    "9": "Nine"
}
output = ""
for digit in phone_number:
    output += number_conversion.get(digit, "!") + " "
# "!" is set as a default value if user enters an invalid key
print(output)

message = input(">")
words = message.split(" ")           # " " space as delimiter   and words as list
print(words)
emojis = {
    ":)": "smile face",
    ":(": "sad face"
}
output =""
for word in words:
    output += emojis.get(word, word) + " "      # if "word" is not in the dictionary, simply set "word" as default value

print(output)
