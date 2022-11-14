day_number = input("Podaj numer dnia tygodnia (od 1 do 7): ")
days = {"1": "PONIEDZIAŁEK",
        "2": "WTOREK",
        "3": "ŚRODA",
        "4": "CZWARTEK",
        "5": "PIĄTEK",
        "6": "SOBOTA",
        "7": "NIEDZIELA"}

try:
    print(f"Twój dzień tygodnia to \n"
          f"\t {days[day_number]}.")
except KeyError:
    print("Podano niewłaściwą wartość. ")






