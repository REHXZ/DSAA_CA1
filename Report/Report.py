from Frequency.Frequency import Frequencies
from Morse.morse_encoder import Decoder, Encoder
from Utilities.utility import Utility
from datetime import datetime
from SortedList.SortedList import SortedList
from SortedList.Word import Word

"""Inherits from Frequencies, generates reports from decoded Morse code."""
class Report(Frequencies):

    """Initializes the Report class and its attributes."""
    def init(self):
        super()._init_()
        self.x = []
        self.frequency = None
        self.Default = None

    """Decodes Morse code, calculates word frequencies, and generates a file with the report."""
    def process(self):
        self.Default = Decoder().morse_recursive("")
        self.Word = self.Default.replace("\n", " ").split(" ")
        self.frequency = self.count_frequencies(self.Word)
        words = list(self.frequency.keys())
        morse_keys = Encoder().morse_String(" ".join(words)).split(" ")
        morse_keys = [morse.strip(',') for morse in morse_keys]
        morse_word_mapping = {words[i]: morse_keys[i] for i in range(len(words))}
        Report = self.generate_report(morse_word_mapping)
        self.select_Output_file()
        is_valid_file = Utility.CheckFileType(self.Output_File, 1)
        if is_valid_file:
            return Utility.WriteFile(self.Output_File, Report)

    """Formats a report with Morse code, word frequencies, and sorted keywords."""
    def generate_report(self, morse_word_mapping):
        frequency_buckets = {}
        for word, freq in self.frequency.items():
            if freq not in frequency_buckets:
                frequency_buckets[freq] = []
            frequency_buckets[freq].append(word)

        report_lines = []

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M")
        report_lines.append("*" * 45)
        report_lines.append(f"REPORT GENERATED ON: {current_time}")
        report_lines.append("*" * 45)
        report_lines.append("\n*** Decoded Morse Text")
        report_lines.append(self.Default + '\n')

        sorted_frequencies = SortedList()
        for freq in frequency_buckets.keys():
            freq_word = Word(str(freq))
            freq_word.frequency = freq
            sorted_frequencies.insert(freq_word)

        current_freq_node = sorted_frequencies.headNode
        while current_freq_node:
            freq = int(current_freq_node.original_name)
            words_sorted = SortedList()
            for word in frequency_buckets[freq]:
                word_obj = Word(word)
                words_sorted.insert(word_obj)

            report_lines.append(f"*** Morse Words with frequency => {freq}")
            current_word_node = words_sorted.headNode
            while current_word_node:
                word = current_word_node.original_name
                morse_code = ' '.join(morse_word_mapping[word].split())
                mark = "(*)" if word.lower() not in self.Stopwords else ""
                report_lines.append(f"[{morse_code}]=> {word.upper()}{mark}")
                current_word_node = current_word_node.nextNode
            report_lines.append("")

            current_freq_node = current_freq_node.nextNode

        report_lines.append("*** Keywords sorted by frequency")
        self.Remove_Stopwords()
        self.frequency = self.count_frequencies(self.Word)

        sorted_list = SortedList()
        for word, freq in self.frequency.items():
            word_obj = Word(word)
            word_obj.frequency = freq
            sorted_list.insert(word_obj)

        current_node = sorted_list.headNode
        while current_node:
            report_lines.append(f"{current_node.original_name.upper()}({current_node.frequency})")
            current_node = current_node.nextNode

        return "\n".join(report_lines)