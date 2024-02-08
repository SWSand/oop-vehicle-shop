import os
import random

class CarManager:
    # CLASS Attributes
    total_cars = 0
    all_cars =[]

    #INSTANCE Attributes
    def __init__(self,make,model,year,mileage,service=[]):
        self._id = (CarManager.total_cars + 1)
        CarManager.total_cars+=1

        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._service = service
        #UPDATE all_cars
        CarManager.all_cars.append(self)


    
    def print_cars(self):
        return f"{self._id} {self._make} { self._model} {self._year} {self._mileage} {self._service}"
    
    
    
    #Tbe able to print the entire "all_cars" list instead of showing the object's allocation in memory
    def __repr__(self):
        return str(self.print_cars())
    
    def add_car():
        os.system('cls' if os.name == 'nt' else 'clear')

        make_input = input("\nEnter the car information in the following format--> 'make' :\n")
        model_input = input("\nEnter the car information in the following format--> 'model' :\n")
        year_input = input("\nEnter the car information in the following format--> 'year' :\n")
        mileage_input = input("\nEnter the car information in the following format--> 'mileage' :\n")
        service_input = input("\nEnter the car information,if any, in the following format--> ''service' :\n")
        
        CarManager.total_cars = CarManager(make_input,model_input,year_input,mileage_input,service_input)
        print("New car entered successfully!")


    @staticmethod
    def enter_menu():
        
        main_menu = f"\n----  WELCOME  ---- \n1. Add a car\n2. View all cars\n3. View total number of cars\n4. See a car's details\n5. Service a car\n6. Update mileage\n7. Quit\n"

        program_running = True

        menu_options = "1234567q"

        while program_running:
            print(main_menu)
            menu_input = input("Enter your menu selection: \n")
            
            if menu_input in menu_options:
                if menu_input == '1':
                    CarManager.add_car()

                elif menu_input == '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for car in CarManager.all_cars:
                        print(car)

                elif menu_input == '3':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"\nThere is a total of {CarManager.total_cars} car/s.")

                elif menu_input == '4':
                    car_id = input("Enter the ID of the car to view: ")
                    car = next((car for car in CarManager.all_cars if car._id == int(car_id)), None)
                    print(car)
                
                elif menu_input == '5':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    car_id = input("Enter the ID of the car to service: ")
                    car = next((car for car in CarManager.all_cars if car._id == int(car_id)), None)
                    if car:
                        service_input = input("Enter the service to add: ")
                        car._service.append(service_input)
                        print("Service added successfully!")
                    else:
                        print("Car not found!")
                
                elif menu_input == '6':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    car_id = input("Enter the ID of the car to update mileage: ")
                    car = next((car for car in CarManager.all_cars if car._id == int(car_id)), None)
                    if car:
                        new_mileage = input("Enter the new mileage: ")
                        car._mileage = new_mileage
                        print("Mileage updated successfully!")
                    else:
                        print("Car not found!")  
            else: 
                print("Invalid entry!")        
            if menu_input == '7' or menu_input == 'q':
                break            


evo = CarManager("Mitsu",'Evolution',"2014",'90000')
evo8 = CarManager("Bishi",'Evolution',"2004",'120000')
evo9 = CarManager("Mitsubishi",'Evolution',"2006",'10000')

# 21 = CarManager("Test","TEst","tsst","tsttt1")

if __name__ == '__main__':
    CarManager.enter_menu()
