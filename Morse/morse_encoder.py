from Utilities.utility import Utility

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

    def select_Input_file(self):
        self.Input_File = input("\nPlease Enter input file: ")

    def select_Output_file(self):
        self.Output_File = input("Please Enter output file: ")
        
    def morse_recursive(self,string = None, text = None):
        while True:
            if string != None and text != None:
                self.file_contents = text
                self.process()
                return self.word
            self.select_Input_file()
            Utility.CheckFileType(self.Input_File)
            self.file_contents = Utility.OpenTextFile(self.Input_File)
            self.process()
            if string == None:
                self.select_Output_file()
                if Utility.CheckFileType(self.Output_File,1):
                        Utility.WriteFile(self.Output_File, self.word)
            else:
                return [self.word,self.Input_File]
            break


class Encoder(Morse):

    def process(self):
        self.file_contents = self.file_contents.split('\n')
        morse_lines = []
        for line in self.file_contents:
            morse_line = ','.join(self.Morse_dict[char.upper()] for char in line if char.upper() in self.Morse_dict)
            morse_lines.append(morse_line)
        self.word = '\n'.join(morse_lines)


class Decoder(Morse):

    def process(self):
        self.file_contents = self.file_contents.replace('\n', ',, ,').split(',')
        for i in self.file_contents:
            self.word += list(self.Morse_dict.keys())[list(self.Morse_dict.values()).index(i)]
        self.word = self.word.replace(', ', '\n')