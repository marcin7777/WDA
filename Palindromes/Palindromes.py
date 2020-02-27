from Palindromes_indicator import palindromes_indicator

coefficient = 10
decimal_indicator = 10 * coefficient

print("Cyfry nie mogą być palindromami")

for i in range(10, 201):
    print(palindromes_indicator(i, coefficient))

    if i == decimal_indicator - 1:
        coefficient *= 10
        decimal_indicator = 10 * coefficient
    #end if
#end for
