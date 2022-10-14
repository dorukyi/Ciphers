# Caesar's Cypher Test

import numpy as np
from math import sqrt



wordlist = ['this', 'micromessage', 'will', 'selfdestruct', 'in', 'forty', 'two', 'seconds', 'shoot', 'film', 'shaken', 'not', 'stirred']


def caesar_encoder(message):
    if type(message) != str:
        raise TypeError

    '''
    cleaned_message step-by-step:
    1) split the message to get rid of spaces
    2) turn it back in to a string with .join()
    3) capitalize the letters with map()
    4) collect the map() output in a list
    5) convert it back to a string
    '''
    cleaned_message = ''.join(list(map(str.upper, ''.join(message.split())))) 

    side = sqrt(len(cleaned_message))
    if not side.is_integer():
        return f'The length of your string is {len(cleaned_message)}. The square root of the length has to be a whole number. Try again.'

    side = int(side)

    ascii = [ord(char) for char in cleaned_message]
    matrix = np.array(ascii).reshape((side, side))

    rotated = np.flipud(np.rot90(matrix, k=1))  # Rotate to the left 90 degrees, flip upside down

    enc_chars = ""

    for i in range(side):
        for j in range(side):
            enc_chars += chr(rotated[i, j])

    return enc_chars


def caesar_decoder(message):
    if type(message) != str:
        raise TypeError

    cleaned_message = ''.join(list(map(str.upper, ''.join(message.split()))))

    side = sqrt(len(cleaned_message))
    if not side.is_integer():
        return f'The length of your string is {len(cleaned_message)}. The square root of the length has to be a whole number. Try again.'

    side = int(side)
    ascii = [ord(char) for char in cleaned_message]
    matrix = np.array(ascii).reshape((side, side))


    flipped = np.flipud(matrix)  # Flip first
    rotated = np.rot90(flipped, k=3)  # Rotate to the left 90 degrees 3 times, so that it's rotated to the right once.

    dec_chars = ""
    temp_word = ""

    for i in range(side):
        for j in range(side):
            temp_word+= chr(rotated[i, j])
        
            if temp_word.lower() in wordlist:
                dec_chars += temp_word + ' '
                temp_word = ""
           

    return dec_chars



def main():
    print(caesar_encoder('SHOOT FILM.......'))
    print(caesar_decoder('SOIHTLOFM'))
    print(caesar_decoder('TRGEROSHOELUREIMWFCTCSEIDTYOMSLEITNISLSNWDCASTFOS'))
    print(caesar_decoder('SETRHNSRANTEKOID'))



if __name__ == '__main__':
    main()
