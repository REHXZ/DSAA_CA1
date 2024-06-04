from Morse.morse_encoder import Encoder, Decoder, Morse
from Utilities.utility import Utility
from SortedList.SortedList import SortedList
from SortedList.Word import Word

class Frequencies(Morse):
    def __init__(self):
        super().__init__()
        self.Word = ''
        self.Stopwords = Utility.OpenTextFile('Stopwords.txt').split("\n")

    def read_frequencies(self):
        self.Output_File = None
        Input = Decoder().morse_recursive("")
        self.Word = Input.replace("\n", " ").split(" ")
        self.Remove_Stopwords()  # Ensure stop words are removed before counting frequencies
        frequencies = self.count_frequencies(self.Word)
        sorted_dict = self.sort_frequencies(frequencies)  # Sort the frequencies
        self.display_frequency_graph(sorted_dict)
        self.display_frequency_labels(sorted_dict)

    def Remove_Stopwords(self):
        self.Word = [word for word in self.Word if word.lower() not in self.Stopwords]

    def count_frequencies(self, word):
        frequency_dict = {}
        for item in word:
            if item in frequency_dict:
                frequency_dict[item] += 1
            else:
                frequency_dict[item] = 1
        return frequency_dict

    def sort_frequencies(self, frequencies):
        # Convert all words to lowercase before sorting
        frequencies_lower = {word.lower(): freq for word, freq in frequencies.items()}
        print("Lowercase frequencies:", frequencies_lower)  # Debug output
        
        # Create a SortedList object
        sorted_list = SortedList()
        # Convert frequencies to Word objects and insert into the sorted list
        for word, frequency in frequencies_lower.items():
            sorted_list.insert(Word(word))

        # print(sorted_list.convertList())
        # Convert the SortedList back to a dictionary
        sorted_dict = {node.name: frequencies[node] for node in sorted_list}
        print("Sorted frequencies:", sorted_dict)  # Debug output
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
        print("-" * 60)

    def display_frequency_labels(self, frequencies):
        words = list(frequencies.keys())
        morse_keys = Encoder().morse_String(" ".join(words)).split(" ")
        morse_keys = [morse.strip(',') for morse in morse_keys]
        max_length = max(len(morse) for morse in morse_keys)

        for i in range(max_length):
            row = []
            for word, morse_code in zip(words, morse_keys):
                row.append(morse_code[i] if i < len(morse_code) else ' ')
                row.append(' ')
                row.append(word[i] if i < len(word) else ' ')
                row.append('\t')
            print(''.join(row))