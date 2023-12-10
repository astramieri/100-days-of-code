# Caesar Cipher

while True:
    action = input("Type 'encode' to encrypt, 'decode' to decrypt, or 'exit' to quit: ")

    if action == 'exit':
        break
    else:
        message = input("Type your input message: ").lower()

        shift = int(input("Type the shift number: "))

        if action == 'decode':
             shift = shift * -1

        for i in range(0, len(message)):
            pass # tofix
                 



    