##price = 10
#price = 10 * 2
#rating = 4.9
#name = 'joe'
#is_published = False
#print(price)
# print(rating)
# print(name, is_published)

#name = 'john smith'
#age = 20
#is_newpatient = True

#i = 1
#while i<=5:
#    print('$' * i)
#    i += 1
#print("done")

#times = 1
#value = 9
#while times <= 3:
#    guess = int(input ("GUESS: "))
#    times += 1
#    if guess == value:
#        print ("you win")
#        break
#else:
#    print ("Sorry, you failed")

options = ''
help_comment = '''
start - to start the car
stop - to stop the car
quit - to exit
'''
start_comment = "Car startd ... Ready to go"
stop_comment = "Car stopped ... "
started = False
while True:
    options = input("> ").lower()
    if options == 'help':
        print(help_comment)
    elif options == 'start':
        if started:
            print("the car is already started")
        else:
            print(start_comment)
            started = True
    elif options == 'stop':
        if started:
            print(stop_comment)
            started = False
        else:
            print ("the car is already stopped")
    elif options == 'quit':
        break
    else:
        print("I don't understand that ...")
