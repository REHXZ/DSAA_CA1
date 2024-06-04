class Utility:
  """Checks the file that is given"""
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
      else:
        print("\nPlease enter a valid file")
        return False
    else:
      return False

  """Returns a string version of the file parsed in"""
  def OpenTextFile(File):
    return open(File, 'r').read()

  """creates a file with a parameter"""
  def WriteFile(File,Value):
      f = open(File,'w+')
      f.write(Value)
      f.close()