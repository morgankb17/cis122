'''
CIS 122 Summer 2020 Lab 6
Author: Morgan Bartlett
Credit:
Description: Word Check Program
'''

# Loop until nothing entered
while True:
    # Prompt for input
    word = input("Enter a search word (blank to exit): ")
    word = word.strip() # Remove leading/trailing
    if len(word) == 0:
        # Exit if nothing entered
        break
    else:
        # Perform search
        # Open file
        fin = open("words_alpha.txt")

        # Search for word by looping over file
        # Initialize default search result to False
        word_found = False
        for line in fin:

            # Remove file line leading/trailing white space and line endings
            line = line.strip()

            # Test for match changing to same case
            if word.upper() == line.upper():

                # Set result status and exit loop
                word_found = True
                break

        # Close file
        fin.close()

        # Print results
        if word_found:
            print("Word " + word + " found")
        else:
            print("Word " + word + " not found")

