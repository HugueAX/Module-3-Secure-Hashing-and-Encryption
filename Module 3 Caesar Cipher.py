#Uses a Caesar Cipher to encrypt and decrypt input text
# constants
FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def caesar_shift(message, shift):
    # result placeholder
    result = ""

    # go through each of the letters in the message and convert to uppercase
    for char in message.upper():
        # only change alpha characters
        if char.isalpha():
            # convert character to ASCII code
            char_code = ord(char)
            #shift character
            new_char_code = char_code + shift

            # prevent no non alpha characters in encrypted message
            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            # convert ASCII code back to character
            new_char = chr(new_char_code)
            # add character to result
            result += new_char
        # add non alpha characters as is
        else:
            result += char

    # print encrypted message
    print(result)


user_message = input("Message to Encrypt: ")
user_shift_key = int(input("Shift Key (integer): "))

caesar_shift(user_message, user_shift_key)