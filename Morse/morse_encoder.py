from Utilities.utility import Utility

"""New class Morse"""
class Morse:
    
    def __init__(self):
        self.Input_File = ''
        self.Output_File = ''
        self.Morse_dict = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
            "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
            "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
            "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
            "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", ",": "--..--", ".": ".-.-.-",
            "?": "..--..", "/": "-..-.", "-": "-....-", "(": "-.--.", ")": "-.--.-", " ": " ", "\n": " ", ',': ""
        }
        self.word = ''
        self.file_contents = None
    """Function to initialize the Input File"""
    def select_Input_file(self):
        self.Input_File = input("\nPlease Enter input file: ")

    """Function to initialize the Output File"""
    def select_Output_file(self):
        self.Output_File = input("Please Enter output file: ")

    """Function to convert a string from text to morse"""
    def morse_String(self,string):
        self.file_contents = string 
        self.process()
        return self.word
    
    """Function to recursively call itself when the user enters a invalid file type"""
    def morse_recursive(self,string = None):
        self.select_Input_file()
        if Utility.CheckFileType(self.Input_File):
            self.file_contents = Utility.OpenTextFile(self.Input_File)
            self.process()
        else:
            self.morse_recursive()
        if string == None:
            state = True
            if state:
                self.select_Output_file()
                if Utility.CheckFileType(self.Output_File,1):
                    Utility.WriteFile(self.Output_File, self.word)
                    state = False
        else:
            return self.word

"""Subclasses of Morse"""
class Encoder(Morse):
    """Encoder Functiontion to Encode Text into Morse"""
    def process(self):
        if '-' in self.file_contents:
            print('Invalid File Type')
            return self.morse_recursive()
        self.file_contents = self.file_contents.split('\n')
        morse_lines = []
        for line in self.file_contents:
            morse_line = ','.join(self.Morse_dict[char.upper()] for char in line if char.upper() in self.Morse_dict)
            morse_lines.append(morse_line)
        self.word = '\n'.join(morse_lines)


class Decoder(Morse):
    """Decoder Functiontion to decode Morse to Text"""
    def process(self):
        self.file_contents = self.file_contents.replace('\n', ',, ,').split(',')
        for i in self.file_contents:
            try:
                self.word += list(self.Morse_dict.keys())[list(self.Morse_dict.values()).index(i)]
            except ValueError:
                print("Invalid File Type")
                return self.morse_recursive()
        self.word = self.word.replace(', ', '\n')