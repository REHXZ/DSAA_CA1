class Frequencies:

    def __init__(self,Input_File,Report_File):
        self.file = 'M.txt'
        self.Input_File = Input_File
        self.Report_File = Report_File

    def Frequency_Reader(self):
        
        with open(self.file, 'r') as f:
            file_contents = f.read().splitlines()
        single_array = [item for line in file_contents for item in line.split(' ')]

