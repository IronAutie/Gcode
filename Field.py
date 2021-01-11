from Friend import Friend



class Field             (Friend):

  'a field of a statement'

  ALLOWED = { None }
  SPACE   = ' '
  BLANK   = ''

  def __init__          (self, friend):
    Friend.__init__     (self, friend)
    self.tag = self.__class__.__name__.upper ()
    self._value_ = None
   
  def _letter_          (self, letter):
    return [self.SPACE, letter][letter in self.ALLOWED]

  def _pre_             (self, text):
    return self.BLANK.join (map (self._letter_, text))

  def _field_           (self, text):
    position = text.find (self.tag)
    if (position < 0):      return
    pre    = self._pre_ (text [position:])
    pieces = pre.split ()
    if (len (pieces) == 0): return
    return pieces [0]

  def _get_value_       (self):
    if (self._value_ == None):
      self._set_value_  (self._field_ (str (self.friend)))
    return self._value_

  def _set_value_       (self, value):
      self._value_ = value

  def __str__           (self):
    return str (self.value)

  def __repr__          (self):
    return "%s = %s" % (self.tag, str (self))

  def is_exist          (self):
    return self.value != None

  value = property (_get_value_, _set_value_)
