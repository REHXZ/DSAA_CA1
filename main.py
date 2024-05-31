from morse_encoder import Morse
from Report import Frequencies

Input_State = True
Current_state = True

input(f'\n{"*" * 60}\n* ST1507 DSAA MorseCode Message Analyzer{" " * 19}*\n* {"-" * 57}*\n* {" " * 57}*\n* - Done by: Rejey Ezekiel Jeyakumar (2348935) {" "*11} *\n* - Class : DAAA/FT/2A/01 {" "*32} *\n{"*" * 60}\n\nPress Enter to continue....')

while Current_state:
    option = int(input(f"Please select your choice ('1','2','3','4','5','6','7'):\n\t 1. Convert Text to Morse Code\n\t 2. Convert Morse Code to Text\n\t 3. Generate Morse Word Frequencies Report \n\t 4. Generate Morse Keyword Frequencies Graph \n\t 5. 5 \n\t 6. 6 \n\t 7. EXIT \nEnter Choice: "))
    match option:
        case 1 | 2:
            while Input_State:
                Input_File_Name = input("\nPlease Enter input file: ")
                Output_File_Name = input("Please Enter output file: ")
                Input_State = False
                File = Morse(Input_File_Name,Output_File_Name)
                if option == 1:
                    File.Encoder()
                if option == 2:
                    File.Decoder()
        case 3:
            F = Frequencies('a','a')
            F.Frequency_Reader()
        case 4:
            print("case 4")
        case 5:
            print('case 5')
        case 6:
            print('case 6')
        case 7:
            print("Bye, thanks for using ST1057 DSAA: MorseCode Message Analyzer")
            Current_state = False