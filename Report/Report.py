class Report:
    def _init_(self,Input_File,Output_File):
        self.Input_File = open(Input_File, 'r').read()
        self.Output_File = Output_File
        self.Stopwords = open('stopwords.txt', 'r').read()
        self.x = []

    def _str_(self):
        return f"{self.Stopwords}"
    
    def Remove_Stopwords(self):
        self.x += ([word for word in self.Input_File.split() if word not in self.Stopwords])
        return self.x
    
    def count_frequencies(self):
        frequency_dict = {}
        for item in self.x:
            if item in frequency_dict:
                frequency_dict[item] += 1
            else:
                frequency_dict[item] = 1
        return frequency_dict