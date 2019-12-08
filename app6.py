car_status = False

while True:
    command = input(">: ").lower()
    if command == "start":
        if car_status == True:
            print("car already started")
        else:
            print("car started")
            car_status = True
    elif command == "stop":
        if car_status == False:
            print("car already stopped")
        else:
            print("car stopped")
            car_status = False
    elif command == "quit":
        break
    elif command == "help":
        print("""
start - to start the car
stop  - to stop the car
quit  - to quit
        """)
    else:
        print("sorry, I don't understand that")
