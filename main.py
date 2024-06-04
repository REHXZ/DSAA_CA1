"""Importing Classes"""
from Morse.morse_encoder import Encoder, Decoder
from Frequency.Frequency import Frequencies
from menu.Menu import Menu
from Report.Report import Report
from Frequency.Char_Freq import MorseAnalyzer, TextAnalyzer

# Setting State of Loop
Current_state = True

#Initializing the Menu to call the show name function
Menu.ShowName()
def main():
    Current_state = True
    while Current_state:
        option = Menu.ShowOption()
        #Checking for Options conditions
        if option.isdigit() and 1 <= int(option) <= 7:
            # The 7 cases Initializing and calling its function
            match int(option):
                case 1:
                    encoder = Encoder()
                    encoder.morse_recursive()
                case 2:
                    decoder = Decoder()
                    decoder.morse_recursive()
                case 3:
                    Reports = Report()
                    Reports.process()
                case 4:
                    Frequency = Frequencies()
                    Frequency.read_frequencies()
                case 5:
                    analyzer = MorseAnalyzer()
                    analyzer.Analyzer()
                case 6:
                    analyzer = TextAnalyzer()
                    analyzer.Analyzer()
                case 7:
                    print("Bye, thanks for using ST1057 DSAA: MorseCode Message Analyzer")
                    Current_state = False
        else:
            print('\nPlease enter a Valid integer between 1 - 7.\n')

if __name__ == '__main__':
    main()