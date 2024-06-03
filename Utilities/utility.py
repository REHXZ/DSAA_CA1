class Utility:

  def CheckFileType(file,type = 0):
    if (file !=  '') and (file.endswith('.txt')):
      if type == 0:
        try:
            with open(file) as f:
                  return False
        except FileNotFoundError:
            print("\nPlease enter a valid file in Directory")
            return True
    print("\nPlease enter a text file")
    return True
    
  def OpenTextFile(File):
    return open(File, 'r').read()

  def WriteFile(File,Value):
      f = open(File,'w+')
      f.write(Value)
      f.close()