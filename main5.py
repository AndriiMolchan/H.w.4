# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class CoachNotFoundError(Exception):
    pass


class SportsComplex:
    def __init__(self):
        self.sports = {
            "Football": "11 players per team",
            "Basketball": "5 players per team",
            "Tennis": "1 player per side"
        }
        self.coaches = {
            "John Doe": "Football",
            "Jane Smith": "Basketball",
            "Michael Johnson": "Tennis"
        }
        self.schedule = {
            "Football": "Monday, Wednesday, Friday at 18:00",
            "Basketball": "Tuesday, Thursday at 17:00",
            "Tennis": "Saturday, Sunday at 10:00"
        }
        self.prices = {
            "Football": 100,
            "Basketball": 80,
            "Tennis": 120
        }

    def display_sports(self):
        print("List of sports:")
        for sport, description in self.sports.items():
            print(f"{sport}: {description}")

    def display_coaches(self):
        print("List of coaches:")
        for coach, sport in self.coaches.items():
            print(f"{coach}: {sport}")

    def display_schedule(self):
        print("Training schedule:")
        for sport, time in self.schedule.items():
            print(f"{sport}: {time}")

    def display_prices(self):
        print("Training prices:")
        for sport, price in self.prices.items():
            print(f"{sport}: ${price}")

    def search_coach(self, name):
        for coach, sport in self.coaches.items():
            if name.lower() == coach.lower():
                print(f"Coach {coach} trains {sport}")
                return
        raise CoachNotFoundError(f"Error: Coach {name} not found")


sports_complex = SportsComplex()

while True:
    print("\nMenu:")
    print("1 - List of sports")
    print("2 - List of coaches")
    print("3 - Training schedule")
    print("4 - Training prices")
    print("5 - Search coach by name")
    print("0 - Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        sports_complex.display_sports()
    elif choice == "2":
        sports_complex.display_coaches()
    elif choice == "3":
        sports_complex.display_schedule()
    elif choice == "4":
        sports_complex.display_prices()
    elif choice == "5":
        name = input("Enter coach's name: ")
        try:
            sports_complex.search_coach(name)
        except CoachNotFoundError as e:
            print(e)
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 0 to 5.")
