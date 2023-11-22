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
        print("Exiting the program.........")
        break
    else:
        print("Invalid command! Please follow the instruction.")
        car.help()