from NumberField  import NumberField
from CommandField import CommandField


class X (NumberField):   'X axis'
class Y (NumberField):   'Y axis'
class Z (NumberField):   'Z axis'
class I (NumberField):   'I offset'
class J (NumberField):   'J offset'
class G (CommandField):  'Go command'



class Statement       (object):

  BLANK  = ''
  SPACE  = ' '
  TAB    = '\t'

  def __init__        (self):
    self._set_value_  (self.BLANK)
    self._set_serial_ (0)

    self.x       = X  (self)
    self.y       = Y  (self)
    self.z       = Z  (self)
    self.g       = G  (self)
    self.i       = I  (self)
    self.j       = J  (self)

    self.tag     = self.__class__.__name__

  def _fields_        (self):
    return (self.x, self.y, self.z, self.i, self.j)

  def _description_   (self):
    return (self.tag, str (self.serial),  repr (self.g), 
            repr (self.x), repr (self.y), repr (self.z),
            repr (self.i), repr (self.j))

  def _display_        (self):
    result = [ 'N', str (self.serial), ' ']
    if self.g.is_exist():  result += [ 'G', str (self.g) ]
    if self.x.is_exist():  result += [ 'X', str (self.x) ]
    if self.y.is_exist():  result += [ 'Y', str (self.y) ]
    if self.z.is_exist():  result += [ 'Z', str (self.z) ]
    if self.i.is_exist():  result += [ 'I', str (self.i) ]
    if self.j.is_exist():  result += [ 'J', str (self.j) ]
    return result

  def __str__         (self):
    return str (self.value)

  def __repr__        (self):
    return self.TAB.join (self._description_ ())

  def _set_value_     (self, text):
    self._value_ = text

  def _get_value_     (self):
    return self._value_ 

  def _set_serial_    (self, index):
    self._serial_ = index

  def _get_serial_    (self):
    return self._serial_ 

  def is_exist        (self):
    return self.i.is_exist () or self.j.is_exist () or self.x.is_exist () or self.y.is_exist () or self.z.is_exist () or self.g.is_exist ()

  def __call__        (self):
    return self.BLANK.join (self._display_ ())

  value  = property (_get_value_,  _set_value_)
  serial = property (_get_serial_, _set_serial_)

