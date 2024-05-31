class Morse:
    def __init__(self,file,O_file):
        self.file = file
        self.O_file = O_file
        self.Morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": " ",
    "\n":" ",
    ',':""
}

    def Encoder(self):
        Morse = ''
        Text = ''
        with open(self.file, 'r') as f:
            file_contents = f.read().splitlines()  # Splitting the text into lines
        for line in file_contents:
            Text += line + ' '  # Adding a space after each line
        
        for i in file_contents:
            for x in i:
                x = x.upper()
                Morse += self.Morse_dict[x] + ','
            Morse += '\n'

        f = open(self.O_file,'w+')
        f.write(Morse)
        f.close()

    def Decoder(self):
        Decoded = ''
        with open(self.file, 'r') as f:
            file_contents = f.read()
        file_contents_new =  file_contents.replace('\n',',, ,')
        new_char = (file_contents_new.split(','))

        for i in new_char:
            Decoded += list(self.Morse_dict.keys())[list(self.Morse_dict.values()).index(i)]
        
        Decoded =  Decoded.replace(', ','\n')
        f = open(self.O_file,'w+')
        f.write(Decoded)
        f.close()