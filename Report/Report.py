from Frequency.Frequency import Frequencies
from Morse.morse_encoder import Decoder, Encoder
from Utilities.utility import Utility
from datetime import datetime

class Report(Frequencies):
    def _init_(self):
        super().__init__()
        self.x = []
        self.frequency = None
        self.Default = None
    
    def process(self):
        self.Default = Decoder().morse_recursive("")
        self.Word = self.Default.replace("\n", " ").split(" ")
        self.frequency = self.count_frequencies(self.Word)
        words = list(self.frequency.keys())
        morse_keys = Encoder().morse_String(" ".join(words)).split(" ")
        morse_keys = [morse.strip(',') for morse in morse_keys]
        morse_word_mapping = {words[i]: morse_keys[i] for i in range(len(words))}
        # Report = self.generate_report(morse_word_mapping)
        # while True:
        #     self.select_Output_file()
        #     if not Utility.CheckFileType(self.Output_File, 1):
        #         continue
        #     else: 
        #         return Utility.WriteFile(self.Output_File, Report)
                


    def generate_report(self,morse_word_mapping):
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


        for freq, words in sorted(frequency_buckets.items()):
            # Sort words by the length of their Morse code representation (longest to shortest)
            words_sorted = sorted(words, key=lambda word: len(morse_word_mapping[word]), reverse=True)
            report_lines.append(f"*** Morse Words with frequency=> {freq}")
            for word in words_sorted:
                morse_code = ' '.join(morse_word_mapping[word].split())
                mark = "(*)" if word.lower() not in self.Stopwords else ""
                report_lines.append(f"[{morse_code}]=> {word.upper()}{mark}")
            report_lines.append("")

        report_lines.append("*** Keywords sorted by frequency")
        self.Remove_Stopwords()
        self.frequency = self.count_frequencies(self.Word)
        for word, freq in sorted(self.frequency.items(), key=lambda item: item[1], reverse=True):
            report_lines.append(f"{word.upper()}({freq})")

        return "\n".join(report_lines)