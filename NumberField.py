from Field import Field


class NumberField      (Field):

  'a numeric field of a statement'

  ALLOWED = { s for s in "0123456789-+Ee." }

  def _field_          (self, text):
    field = Field._field_ (self, text)
    if field != None:  return float (field)



      
      