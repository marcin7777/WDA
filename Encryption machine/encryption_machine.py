from in_the_heart_of_the_machine import encrypt_decrypt, letter_changer

decision = (input("Szyfrowanie/Deszyfrowane?: "))
if decision == "Szyfrowanie" or decision == "Deszyfrowanie":
    key = int(input("Podaj klucz: "))
    key_sequence = []
    key = str(key)
    key_current_digit = 0

    file = open("Message.txt", "r", encoding = "utf-8")
    messages = file.readlines()
    file.close()

    file = open("Message.txt", "w")
    for message in messages:
        messages[messages.index(message)] = message.replace("\n", "")
        message = message.replace("\n", "")
        index = 0
        for letter in message:
            if letter == " " or letter == "" or letter == None:
                index += 1
                continue
            else: key_sequence.append(int(key[key_current_digit]))

            letter = encrypt_decrypt(decision, letter, int(key[key_current_digit]))
            message = letter_changer(message, index, letter)
            index += 1
            
            if key_current_digit != len(key) - 1: key_current_digit += 1
            else: key_current_digit = 0

        file.write(message + "\n")
        #end for
    #end for

    file.close()
    
else: print("Proszę wybrać właściwą funkcję programu!")
