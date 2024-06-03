from Morse.morse_encoder import Encoder, Decoder, Morse
from collections import Counter
# from Utilities
class Frequencies(Morse):
    def __init__(self):
        super().__init__()
        self.input_file = ''
        self.report_file = ''
        self.time = None
        # self.Stopwords = 

    def read_frequencies(self):
        decoder = Decoder()
        self.time = decoder.morse_recursive('').replace("\n", " ").split(" ")
        self.Remove_Stopwords()
        frequencies = self.count_frequencies()
        print(frequencies)

    def Remove_Stopwords(self):
        self.time += ([word for word in self.Input_File.split() if word not in self.Stopwords])
        self.time = self.time

    def count_frequencies(self):
            frequency_dict = {}
            for item in self.time:
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



    # def display_frequency_graph(self, frequencies):
    #     max_freq = max(frequencies.values())
    #     words = list(frequencies.keys())
    #     graph_rows = [''] * max_freq

    #     for level in range(max_freq, 0, -1):
    #         row = ''.join('*\t ' if frequencies[word] >= level else '  ' for word in words)
    #         graph_rows[max_freq - level] = row

    #     for row in graph_rows:
    #         print(row)
    #     print("-" * 60)

    # def display_frequency_labels(self, frequencies):
    #     morse_codes = Morse(self.input_file).to_string().replace("\n", "").split(" ")
    #     morse_codes[0] = ',' + morse_codes[0]
    #     morse_frequency = self.count_frequencies(morse_codes)
    #     morse_keys = list(morse_frequency.keys())
    #     words = list(frequencies.keys())
    #     max_length = max(len(morse) for morse in morse_keys)

    #     for i in range(max_length):
    #         row = []
    #         for word, morse_code in zip(words, morse_keys):
    #             row.append(morse_code[i] if i < len(morse_code) else ' ')
    #             row.append(' ')
    #             row.append(word[i] if i < len(word) else ' ')
    #             row.append('\t')
    #         print(''.join(row))