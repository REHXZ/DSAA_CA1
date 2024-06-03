from Morse.morse_encoder import Encoder, Decoder
from Frequency.Report import Frequencies
from menu.Menu import Menu
Current_state = True

Menu.ShowName()
def main():
    Current_state = True
    while Current_state:
        option = Menu.ShowOption()
        if option.isdigit() and 1 <= int(option) <= 7:
            match int(option):
                case 1:
                    encoder = Encoder()
                    encoder.morse_recursive()
                case 2:
                    decoder = Decoder()
                    decoder.morse_recursive()
                case 3:
                    F = Frequencies()
                    F.read_frequencies()
                case 4:
                    print("case 4")
                case 5:
                    print('case 5')
                case 6:
                    print('case 6')
                case 7:
                    print("Bye, thanks for using ST1057 DSAA: MorseCode Message Analyzer")
                    Current_state = False
        else:
            print('\nPlease enter a Valid integer between 1 - 7.\n')

if __name__ == '__main__':
    main()