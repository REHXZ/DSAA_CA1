class Menu:
    def ShowName():
        print(f'\n{"*" * 60}\n* ST1507 DSAA MorseCode Message Analyzer{" " * 19}*\n* {"-" * 57}*\n* {" " * 57}*\n* - Done by: Rejey Ezekiel Jeyakumar (2348935) {" "*11} *\n* - Class : DAAA/FT/2A/01 {" "*32} *\n{"*" * 60}\n\nPress Enter to continue....')
        input()  # Wait for the user to press Enter

    def ShowOption():
        option = input("Please select your choice ('1','2','3','4','5','6','7'):\n\t 1. Convert Text to Morse Code\n\t 2. Convert Morse Code to Text\n\t 3. Generate Morse Word Frequencies Report \n\t 4. Generate Morse Keyword Frequencies Graph \n\t 5. 5 \n\t 6. 6 \n\t 7. EXIT \nEnter Choice: ")
        return option
