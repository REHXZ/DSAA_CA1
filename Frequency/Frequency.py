from Morse.morse_encoder import Encoder, Decoder, Morse
from Utilities.utility import Utility
from SortedList.SortedList import SortedList
from SortedList.Word import Word
from datetime import datetime

"""Inheriting the Morse class"""
class Frequencies(Morse):
    def __init__(self):
        super().__init__()
        self.Word = ''
        self.Stopwords = Utility.OpenTextFile('Stopwords.txt').split("\n")

    """This function is the main entrypoint to see the Graph"""
    def read_frequencies(self):
        self.Output_File = None
        Input = Decoder().morse_recursive("")
        self.Word = Input.replace("\n", " ").split(" ")
        self.Remove_Stopwords()  # Ensure stop words are removed before counting frequencies
        frequencies = self.count_frequencies(self.Word)
        Output = self.display_frequency_graph(frequencies)
        self.select_Output_file()
        is_valid_file = Utility.CheckFileType(self.Output_File, 1)
        if is_valid_file:
            return Utility.WriteFile(self.Output_File, Output)


    """This function removes stop words""" 
    def Remove_Stopwords(self):
        self.Word = [word for word in self.Word if word.lower() not in self.Stopwords]

    """Uses a sorted list to create a sorted dictionary of the words in the parameter."""
    def count_frequencies(self, words):
        frequency_dict = {}
        for item in words:
            item_lower = item.lower()
            if item_lower in frequency_dict:
                frequency_dict[item_lower].frequency += 1
            else:
                frequency_dict[item_lower] = Word(item)

        sorted_list = SortedList()
        for word_obj in frequency_dict.values():
            sorted_list.insert(word_obj)

        sorted_dict = {}
        current = sorted_list.headNode
        while current:
            sorted_dict[current.original_name] = current.frequency
            current = current.nextNode
        
        return sorted_dict

    """Code to create the graph"""
    

    def display_frequency_graph(self, frequencies):
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M")

        header = ''
        header += "*"*45 + '\n'
        header += f'REPORT GENERATED ON: {current_time}' + '\n'
        header += "*"*45

        max_freq = max(frequencies.values())
        words = list(frequencies.keys())

        graph_rows = [''] * max_freq
        for level in range(max_freq, 0, -1):
            row = '\t'.join('*\t' if frequencies[word] >= level else '' for word in words)
            graph_rows[max_freq - level] = row

        output_string = header + "\n"  # Add the header to the output string

        for row in graph_rows:
            output_string += row + "\n"

        output_string += "-" * 60 + "\n"  # Add the separator line

        words = list(frequencies.keys())
        morse_keys = Encoder().morse_String(" ".join(words)).split(" ")
        morse_keys = [morse.strip(',') for morse in morse_keys]
        max_length = max(len(morse) for morse in morse_keys)

        for i in range(max_length):
            row = []
            for word, morse_code in zip(words, morse_keys):
                row.append(morse_code[i] if i < len(morse_code) else ' ')
                row.append('')
                row.append(word[i] if i < len(word) else ' ')
                row.append('\t')
            output_string += ''.join(row) + "\n"

        return output_string  # Return the complete string
