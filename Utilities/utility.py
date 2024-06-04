class Utility:

  def CheckFileType(file,type=0):
    if file !=  '':
      if file.endswith('.txt'):
        if type == 0:
          try:
              with open(file) as f:
                   return True
          except FileNotFoundError:
              print("\nPlease enter a valid file")
              return False
        else:
          return True
      print("\nPlease enter a valid file")
      return False
    return False


    
  def OpenTextFile(File):
    return open(File, 'r').read()

  def WriteFile(File,Value):
      f = open(File,'w+')
      f.write(Value)
      f.close()