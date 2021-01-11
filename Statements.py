from collections import OrderedDict


from Statement import Statement



class Statements (OrderedDict):

  SEPERATOR = '\n'

  def __init__   (self):
    OrderedDict.__init__ (self, {})
    self.serial = 0

  def lines      (self, text):
    return [s for s in text.split (self.SEPERATOR) if (s != '')]

  def index      (self):
    result = self.serial
    self.serial += 1
    return result

  def create     (self, text):
    result = Statement ()
    result.value  = text
    return result

  def set        (self, text):
    statements = [ s for s in map (self.create, self.lines (text)) if s.is_exist() ]
    for s in statements: s.serial = self.index ()
    for s in statements: self.update ({s.serial:s})
    
  def __call__    (self):
    return self.SEPERATOR.join ([v() for v in self.values ()])

  def __str__    (self):
    return self.SEPERATOR.join (map (str,  self.values ()))

  def __repr__   (self):
    return self.SEPERATOR.join (map (repr, self.values ()))



if __name__ == '__main__':
  import sys
  s = Statements ()
  s.set (sys.stdin.read ())
  print (s())
