def far_to_cel(temp):
    return (temp - 32) / 1.8


def far_to_kel(temp):
    return 273.5 + (temp - 32.0) / 1.8


def cel_to_far(temp):
    return temp * 1.8 + 32


def cel_to_kel(temp):
    return temp + 273.15


def kel_to_cel(temp):
    return temp - 273.5


def kel_to_far(temp):
    return (temp - 273.5) * 1.8 + 32


conversions = {"CF": cel_to_far,
               "CK": cel_to_kel,
               "KF": kel_to_far,
               "KC": kel_to_cel,
               "FC": far_to_cel,
               "FK": far_to_kel}

temp = float(input("Podaj temperaturę: "))
scale1 = input("Podaj skalę początkową (C/K/F): ")
scale2 = input("Podaj skalę, docelową (C/K/F): ")
option = scale1.upper() + scale2.upper()

try:
    print(conversions[option](temp))
except KeyError:
    print('Wybrano niewłaściwą opcję.')
