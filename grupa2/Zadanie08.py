day = input("Podaj numer dnia tygodnia (od 1 do 7): ")
names_of_days = {"1": "Poniedziałek",
                 "2": "Wtorek",
                 "3": "Środa",
                 "4": "Czwartek",
                 "5": "Piątek",
                 "6": "Sobota",
                 "7": "Niedziela"}

try:
    day_name = names_of_days[day]
    print(f"{day} dzień tygodnia to {day_name}.")
except KeyError:
    print("Podano niewłaściwą wartość")
