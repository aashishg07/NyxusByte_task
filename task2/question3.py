'''

3. Create a program for "Car Racing" with the following functionalities:
    a. The initial state of the car is in the "stop" state.

    b. Display a help message to the user explaining the available commands:
    start -> start the car
    stop -> stop the car
    exit -> exit the program

    c. Users are not allowed to enter the same command if the car is already in the
    same state. For example:
        If the car is in the "start" state and the user enters the start command
        again, display "Car is already in start state."
        Similarly, if the car is in the "stop" state and the user enters the stop
        command again, display "Car is already in stop state."
        
    d. When the user enters exit, prompt them with "Are you sure you want to exit?"
    If the user inputs "yes," the program should stop. If the user inputs anything
    else, the program should continue.

'''



class Car:
    def __init__(self):
        self.car_started = False

    def help(self):
        print("Follow the instructions: ")
        print("start - Start the car")
        print("stop - Stop the car")
        print("exit - Close the program")


    def start_car(self):
        if self.car_started:
            print("Car is already started")
        else:
            self.car_started = True
            print("Car started.")

    def stop_car(self):
        if not self.car_started:
            print("Car is already stopped")
        else:
            self.car_started = False
            print("Car stopped.")

car = Car()
car.help()


while True:

    command = input("Enter the command: ").lower()

    if command == "start":
        car.start_car()
    elif command == "stop":
        car.stop_car()
    elif command == "exit":
        exit_command = input("Are you sure, you want to exit? (yes/no): ").lower()
        if exit_command == "yes":
            print("Exiting the program.........")
            break
    else:
        print("Invalid command! Please follow the instruction.")
        car.help()