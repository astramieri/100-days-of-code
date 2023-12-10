# Caesar Cipher

while True:
    action = input("Type 'encode' to encrypt, 'decode' to decrypt, or 'exit' to quit: ")

    if action == 'exit':
        break
    elif action in ["encode", "decode"]:
        input_text = input("Input text: ").lower()
        output_text = ""

        shift = int(input("Shift number: "))

        if action == 'decode':
             shift = shift * -1 

        base = 26 # characters in alphabet
        offset = 96 # a=97 ASCII table

        for i in range(0, len(input_text)):
            position = ord(input_text[i]) - offset # a=1, b=2, .. z=26

            if position in range(1, base+1):
                position += shift
                position %= base

                output_text += chr(position + offset)
            else:
                output_text += input_text[i]

        print(f"Ouput text: {output_text}")
                 



    