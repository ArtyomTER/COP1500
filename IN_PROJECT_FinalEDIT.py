
# Artyom Teruni
# Itemized list of most or all guitar chords,
# Useful for writing of custom chords
# Song training
# Later implementing piano chords and time signatures

numberOne = int(input("Pick a number"))
print("This is an example of the exponent operator, 2 raised to the power of your input: ", 2 ** numberOne)
numberOne = int(input("Pick a number"))
print("This is an example of the multiplication operator: ", 2 * numberOne, end="")
numberOne = int(input("\nPick a number"))
print("This is an example of the division operator: ", 2 / numberOne, end="")
numberOne = int(input("\nPick a number"))
print("This is an example of the modulo operator: ", 2 % numberOne, end="")
numberOne = int(input("\nPick a number"))
print("This is an example of the square root operator: ", 2 // numberOne, end="")
numberOne = int(input("\nPick a number"))
print("This is an example of the addition operator: ", 2 + numberOne, end="")
numberOne = int(input("\nPick a number"))
print("This is an example of the subtraction operator: ", 2 - numberOne, end="" + "\n")

# Added conditional statements
# Added relational operators

numb = int(input("Guess a number"))
counter = 0
List1 = [1, 3, 4, 6, 7, 8]
if numb == -3 or numb != 1 and numb > 0 and numb is not None:
    while counter < 6:
        for i in range(len(List1)):
            counter += 1
            print("You guessed cor" + "rectly", counter)
else:
    print("You didn\'t guess correctly")

# https://www.101computing.net/guitar-chords-reader/
# Website I found that helps you read guitar chords.
# https://www.guitar-chord.org/chart.html
# Diagrams and names of chords that can be plugged in later.


chords = {"C": "x32010", "A": "x02220", "G": "320033", "E": "022100", "D": "xx0232", "F": "x3321x",
          "Am": "x02210", "Dm": "xx0231", "Em": "022000", "Am7": "x02010", "Bm7": "x20202",
          "Cm7": "x313xx", "Dm7": "xx0211", "Em7": "02203", "Fm7": "131111",
          "A_barr": "577655", "Bm_barr": "799777", }


# Visualization of the chord for training
# Similar to tabs but, it's only the strings and frets needed for the chord
def displayChord(chord_display):
    """

    :param chord_display:
    """
    fret_Note = chords[chord_display]

    print("\n" + chord_display)
    nut = ""
    for string in fret_Note:
        if string == "x":
            nut += "x"
        else:
            nut += "_"
    print(nut)

    for fret_Num in range(1, 10):  # YOU CAN SET THE RANGE TO AS MANY FRETS AS NEEDED
        fret = ""
        for string in fret_Note:
            if string == str(fret_Num):
                fret += "O"  # "O" REFERS TO FINGER PLACEMENT
            else:
                fret += "|"  # "|" REFERS TO STRINGS ON THE GUITAR
        print(fret)


# Listed Chords here will be printed out in the shell in tab format
# PLug in Chord names into the string and run the program
# Added chordlist to be displayed in the shell for easier user experience
# Implemented a way to quit out of the program


List = None
chordList = ['A', 'C', 'G', 'E', 'D', 'F', 'Am', 'Dm', 'Em', 'Am7', 'Bm7', 'Cm7', 'Dm7', 'Em7', 'Fm7', 'A_barr',
             'Bm_barr']
print("\n")
while List != 0:
    print('A', 'C', 'G', 'E', 'D', 'F', 'Am', 'Dm', 'Em', 'Am7', 'Bm7', 'Cm7', 'Dm7', 'Em7', 'Fm7', 'A_barr', 'Bm_barr',
          sep=', ')
    List = input("\nEnter chords you want to see one at a time, without spaces. Enter 0 to exit")
    if List == '0':
        print("Exiting program")
        quit()
    if List not in chordList:
        print("Incorrect chord entered, terminating program")
        quit()
    ListChords = List.split(",")
    for chord in ListChords:
        displayChord(chord)
