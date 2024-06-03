from Morse.morse_encoder import Encoder, Decoder, Morse
from Utilities.utility import Utility

class Frequencies(Morse):
    def __init__(self):
        super().__init__()
        self.Input_File = ''
        self.Word = ''
        self.Stopwords = Utility.OpenTextFile('Stopwords.txt').split("\n")

    def read_frequencies(self):
        Input = Decoder().morse_recursive('')
        self.Input_File = Input[1]
        self.Word = Input[0].replace("\n", " ").split(" ")
        self.Remove_Stopwords()  # Ensure stop words are removed before counting frequencies
        frequencies = self.count_frequencies(self.Word)
        self.display_frequency_graph(frequencies)
        self.display_frequency_labels(frequencies)
        print(frequencies)

    def Remove_Stopwords(self):
        self.Word = [word for word in self.Word if word.lower() not in self.Stopwords]

    def count_frequencies(self,word):
        frequency_dict = {}
        for item in word:
            if item in frequency_dict:
                frequency_dict[item] += 1
            else:
                frequency_dict[item] = 1
        
        # Sort the dictionary items based on their values in descending order
        sorted_items = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
        
        # Convert the sorted items back into a dictionary
        sorted_dict = {}
        for key, value in sorted_items:
            sorted_dict[key] = value
        
        return sorted_dict

    def display_frequency_graph(self, frequencies):
        max_freq = max(frequencies.values())
        words = list(frequencies.keys())
        graph_rows = [''] * max_freq

        for level in range(max_freq, 0, -1):
            row = ''.join('*\t ' if frequencies[word] >= level else '  ' for word in words)
            graph_rows[max_freq - level] = row

        for row in graph_rows:
            print(row)
        print("-" * 50)

    def display_frequency_labels(self, frequencies):
        words = list(frequencies.keys())
        morse_keys = Encoder().morse_recursive(" "," ".join(words)).split(" ")
        max_length = max(len(morse) for morse in morse_keys)

        for i in range(max_length):
            row = []
            for word, morse_code in zip(words, morse_keys):
                row.append(morse_code[i] if i < len(morse_code) else ' ')
                row.append(' ')
                row.append(word[i] if i < len(word) else ' ')
                row.append('\t')
            print(''.join(row))