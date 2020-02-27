from Armstrong_number_indicator import Armstrong_number_indicator

n = 1
decimal_indicator = 10
current_number = 1

print("Liczby Armstronga to:")

while True:
    Armstrong_number_indicator(current_number, n)

    if current_number == decimal_indicator - 1:
        n += 1
        decimal_indicator *= 10
    #end if

    current_number += 1
#end while
