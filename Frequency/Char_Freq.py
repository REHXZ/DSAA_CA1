from Morse.morse_encoder import Decoder, Encoder
from Utilities.utility import Utility
from SortedList.SortedList import SortedList
from SortedList.Word import Word
from Frequency.Frequency import Frequencies

class CharacterAnalyzer(Frequencies):
    def __init__(self):
        super().__init__()
        self.sort = ''

    """ This function takes a dictionary of character frequencies as input and displays the frequency analysis in a user-friendly format."""
    def display_frequency_analysis(self, frequencies):
        sorted_list = SortedList()
        for char, freq in frequencies.items():
            sorted_list.insert(Word(char, freq))
        
        print("\nCharacter Frequency Analysis:")
        current = sorted_list.headNode
        while current:
            print(f"Character '{current.original_name}': {'*' * current.frequency} ({current.frequency})")
            current = current.nextNode
        print()

    def Analyzer(self):
        frequencies = self.process()
        self.display_frequency_analysis(frequencies)

"""This class converts the Morse code to text before counting character frequencies."""
class MorseAnalyzer(CharacterAnalyzer):
    def process(self):
        self.Word = Decoder().morse_recursive('').replace("\n", " ").split(" ")
        return self.count_character_frequencies(self.Word)

    """This function processes the Morse code input. Decodes the Morse code using a Morse decoder."""
    def count_character_frequencies(self, words):
        frequency_dict = {}
        for word in words:
            for char in word:
                if char in frequency_dict:
                    frequency_dict[char] += 1
                else:
                    frequency_dict[char] = 1
        return frequency_dict

"""This class converts the Morse code to text before counting character frequencies."""
class TextAnalyzer(CharacterAnalyzer):
    def process(self):

        self.Word = Encoder().morse_recursive('').replace(' ','').replace("\n", ",").split(",")
        return self.count_character_frequencies(self.Word)

    """It takes a list of words as input and returns a dictionary containing the frequency of each word,and concats them along with its Morse code equivalent."""
    def count_character_frequencies(self, words):
        self.Morse_dict
        frequency_dict = {}
        for word in words:
            if word == "":
                continue
            if word in frequency_dict:
                frequency_dict[word] += 1
            else:
                frequency_dict[word] = 1
        
        updated_frequency_dict = {}
        for key, value in frequency_dict.items():
            updated_key = f"{key} ({list(self.Morse_dict.keys())[list(self.Morse_dict.values()).index(key)]})"
            updated_frequency_dict[updated_key] = value

        return updated_frequency_dict
