"""
7.1PP Data Classes
"""
__author__ = "ZUBAIR AHMED" 

"""
Define an enumeration of car types
"""
from dataclasses import dataclass
from enum import Enum

class CarType(Enum):
    '''
    Enumerations of car types.
    '''
    ICE = "internal combustion engine"
    HEV = "hybrid electrical vehicle"
    PHEV = "plug-in hybrid electric vehicle"
    BEV = "battery electric vehicle"
    
@dataclass
class Car:
    '''
    Showing registration details of a car.
    '''
    registration: str
    seats: int
    drive_wheels: int
    car_type: CarType

    def __str__(self):
        '''
        Returns a formatted string representing the car details.
        '''
        car_type_str = self.car_type.name.upper()  # Getting the uppercase name of the car type
        seats_str = f"{self.seats}-seat"  # Formatting the seats as string
        drive_wheels_str = f"{self.drive_wheels} wheel drive"  # Formatting the drive wheels as string
        car_desc = f"{self.registration}: {seats_str} {drive_wheels_str} {car_type_str}"  
        # Adding car description
        
        # Append additional info based on the number of seats
        if self.seats < 3:
            car_desc += " coupe"
        elif self.seats > 7:
            car_desc += " people mover"
        
        return car_desc

def input_car_type() -> CarType:
    '''
    Allows the user to select a car type from the menu.
    '''
    print("Select car type:")
    for index, car_type in enumerate(CarType):
        print(f"{index + 1}. {car_type.name}")
    
    user_selection = int(input("Enter Your Choice: "))
    while user_selection < 1 or user_selection > len(CarType):
        print("Invalid choice. Please try again.")
        user_selection = int(input("Enter Your Choice: "))
    
    return CarType(list(CarType)[user_selection - 1])


def input_car() -> Car:
    '''
    Takes input from the user to create a Car object.
    '''
    registration = input("Enter car's registration: ")

    seats = input("Enter number of seats: ")
    while not seats.isdigit() or int(seats) < 1:
        print("Number of seats must be at least 1.")
        seats = input("Enter number of seats: ")

    drive_wheels = input("Enter number of drive wheels: ")
    while not drive_wheels.isdigit():
        print("Invalid input. Please enter a number.")
        drive_wheels = input("Enter number of drive wheels: ")

    car_type = input_car_type()

    return Car(registration, int(seats), int(drive_wheels), car_type)

def add_many(cars,count):
    '''
    Allows the user to add multiple cars at once.
    '''
    for i in range (count):
        add_car(cars)

def add_car(cars):
    """
    This function adds a new car entry into the list.
    """
    cars.append(input_car()) 
        
def most_seats(cars: list[Car], car_type: CarType) -> Car:
    '''
    Finds the car with the most seats of a given type.
    '''
    has_most = None

    for car in cars:
        if car.car_type == car_type:
            if has_most is None or car.seats > has_most.seats:
                has_most = car

    return has_most

def average_seats(cars: list[Car], car_type: CarType) -> float:
    '''
    Calculates the average number of seats in cars of a particular type.
    '''
    total_seats = 0
    count = 0

    for car in cars:
        if car.car_type == car_type:
            total_seats += car.seats
            count += 1

    if count == 0:
        return 0
    else:
        return total_seats / count

def main():
    cars = []  # List to store Car objects
    number_of_cars = int(input("Enter the number of cars to add: "))
    add_many(cars, number_of_cars)
    
    choice = 0
    while choice != 5:
        print("\nMenu:")
        print("1. Add a car")
        print("2. Display all cars")
        print("3. Display the car with the most seats of a particular type")
        print("4. Display the average number of seats in cars of a particular type")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_car(cars)
            # new_cars = add_many()
            # cars.extend(new_cars)
            print("Car added successfully!")
        elif choice == "2":
            print("\nAll Cars:")
            for car in cars:
                print(car)
        elif choice == "3":
            car_type = input_car_type()
            car_with_most_seats = most_seats(cars, car_type)
            if car_with_most_seats is not None:
                print(f"The car with the most seats of type {car_type.name}:")
                print(car_with_most_seats)
            else:
                print("No cars of that type.")
        elif choice == "4":
            car_type = input_car_type()
            avg_seats = average_seats(cars, car_type)
            print(f"The average number of seats in {car_type.name} cars is {avg_seats:.2f}")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
