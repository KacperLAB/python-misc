a = input("Podaj ciag znakow: ")
a = list(a)

try:
    b = int(input("Podaj indeks znaku do wyswietlenia: "))
except ValueError:
    print("Indeks musi być liczbą całkowitą")
else:
    try:
        print(a[b])
    except IndexError:
        print("Indeks nie istnieje")


