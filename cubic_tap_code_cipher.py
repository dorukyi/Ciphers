import numpy as np
matrix = np.arange(65, 92).reshape((3,3,3)) # 3D Numpy array with the ascii values of all characters
matrix[2][2][2] = 32

def encode(string):
    matrix = np.arange(65, 92).reshape((3,3,3)) # 3D Numpy array with the ascii values of all characters
    matrix[2][2][2] = 32
    split = list(string) # Separate individual characters
    code = [ord(char) for char in split] # List consisting of the ascii number values of the string characters 
    indeces = [] 

    # indeces contains the "locations" of the characters in the array.
    for char in code:
        indeces.append(list(np.where(matrix==char)))


    coordinates = []
    dots = []

    # The locations are converted to ints, then added to the coordinates list.
    for item in indeces:
        temp = []
        for location in item:
            temp.append(int(str(location)[1])+1)
        temp.reverse() # The order is reversed for the format column, row, layer.
        coordinates.append(temp)
            
    # In coordinates, character coordinates are stored in sublists. Coordinates2 is just one big list without sublists. 
    coordinates2 = []
    for i in coordinates:
        for k in i:
            coordinates2.append(k)

    # The encoding is created.
    for n in coordinates2:
        dots.append('.'*n)

    # The encoded list is returned as a string.
    return ' '.join(dots)


def decode(string):
    matrix = np.arange(65, 92).reshape((3,3,3))
    matrix[2][2][2] = 32
    split = string.split() # List of individual encoded characters(dots)

    numbers = [] 
    for char in split:
        numbers.append(len(char)-1) # Converting the dots into the ascii values of each character.
    
    segmented = []
    i = 0
    sub = []
    while i < len(numbers):
        sub.append(numbers[i])
        i += 1
        if i % 3 == 0:
            segmented.append(sub)
            sub = []

    message = []

    for value in segmented:
        message.append(chr(matrix[value[2],value[1],value[0]]))
    
    return ''.join(message)


def main():
    print(encode('N')) # .. .. ..
    print(encode('TEST')) # .. . ... .. .. . . . ... .. . ...
    print(encode('HELLO WORLD')) # .. ... . .. .. . ... . .. ... . .. ... .. .. ... ... ... .. .. ... ... .. .. ... ... .. ... . .. . .. .

    print(decode(".. .. ..")) # N
    print(decode(".. . ... .. .. . . . ... .. . ...")) # TEST
    print(decode(".. ... . .. .. . ... . .. ... . .. ... .. .. ... ... ... .. .. ... ... .. .. ... ... .. ... . .. . .. .")) # HELLO WORLD

if __name__ == '__main__':
    main()
