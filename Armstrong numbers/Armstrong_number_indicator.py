def Armstrong_number_indicator(number, n):
    digit_sum = 0
    mirror_number = number

    while mirror_number > 0:
        digit = mirror_number % 10
        digit_sum += digit ** n
        mirror_number //= 10
    #end while

    if number == digit_sum: print(number)
#end Armstrong_number_indicator
