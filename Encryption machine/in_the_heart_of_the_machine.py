def encrypt_decrypt(decision, letter, letter_key):
    if decision == "Szyfrowanie":
        if (ord(letter) < 91 and letter_key + ord(letter) > 90):
            difference = letter_key + ord(letter) - 90 - 1
            letter = chr(65 + difference)
        elif (ord(letter) < 91 and letter_key + ord(letter) < 91): letter = chr(ord(letter) + letter_key)

        if (ord(letter) > 96 and letter_key + ord(letter) > 122):
            difference = letter_key + ord(letter) - 122 - 1
            letter = chr(97 + difference)
        elif (ord(letter) > 96 and letter_key + ord(letter) < 123): letter = chr(ord(letter) + letter_key)
    #end if

    if decision == "Deszyfrowanie":
        if (ord(letter) < 91 and ord(letter) - letter_key < 65):
            difference = 65 - (ord(letter) - letter_key) - 1
            letter = chr(90 - difference)
        elif (ord(letter) < 91 and ord(letter) - letter_key > 64): letter = chr(ord(letter) - letter_key)

        if (ord(letter) > 96 and ord(letter) - letter_key < 97):
            difference = 97 - (ord(letter) - letter_key) - 1
            letter = chr(122 - difference)
        elif (ord(letter) > 96 and ord(letter) - letter_key > 96): letter = chr(ord(letter) - letter_key)
    #end if

    return letter
#end encrypt_decrypt

def letter_changer(word, index, replacement): return '%s%s%s'%(word[:index], replacement, word[index + 1:])
