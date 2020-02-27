def palindromes_indicator(number, decimal):
    representant = number
    counter = 0
    
    while number % 10 != number // decimal:
        counter += 1
        mirror_number = list(str(number))
        last_digit = mirror_number[len(mirror_number) - 1]
        mirror_number[len(mirror_number) - 1] = mirror_number[0]
        mirror_number[0] = last_digit
        mirror_number = int(''.join(mirror_number))
        number += mirror_number

        if counter == 1000: return "%d nie spełnia hipotezy" % representant
    #end while
        
    if counter == 0: return "%d - palindrom" % representant
    else: return "%d spełnia hipotezę - liczba iteracji: %d" % (representant, counter)
#end palindromes_indicator
