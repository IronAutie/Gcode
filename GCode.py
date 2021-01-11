from Statements import Statements
from Statement  import Statement

class GCode (Statements):

  def normalize   (self, increment = 1):

    result = []
    serial = increment

    for v in self.values ():
      v.serial  = serial
      serial   += increment
      result   += [v]
  
    self.clear ()
    for r in result:  self [r.serial] = r

  def out          (self, number, depth):
    result        = Statement ()
    result.value  = "G00Z%f" % (depth * -1.0)
    result.serial = number - 1
    return result

  def back         (self, number, depth):
    result        = Statement ()
    result.value  = "G00Z%f" % depth
    result.serial = number + 1
    return result

  def add_z_moves  (self, depth = -0.01):

    if abs (depth) == 0.0:
      depth = -0.01

    result = GCode ()
    
    for v in self.values ():
      if str (v.g) == "00":
        number = v.serial
        out    = self.out  (number, depth)
        back   = self.back (number, depth)
        result.update ({out.serial:out})
        result.update ({back.serial:back})

    self.update (result)

  def flip_z_moves (self):

    for v in self.values ():
      if str (v.z) != "None":
        z = v.z.value
        v.z.value = -1.0 * z

  def flip_x_moves (self):

    for v in self.values ():

      if str (v.x) != "None":
        x = v.x.value
        v.x.value = -1.0 * x

      if str (v.i) != "None":
        i = v.i.value
        v.i.value = -1.0 * i

  def flip_y_moves (self):

    for v in self.values ():
      if str (v.y) != "None":
        y = v.y.value
        v.y.value = -1.0 * y

      if str (v.j) != "None":
        j = v.j.value
        v.j.value = -1.0 * j

  def scale_x_moves (self, depth):

    for v in self.values ():

      if str (v.x) != "None":
        x = v.x.value
        v.x.value = depth * x

      if str (v.i) != "None":
        i = v.i.value
        v.i.value = depth * i


  def scale_y_moves (self, depth):

    for v in self.values ():

      if str (v.y) != "None":
        y = v.y.value
        v.y.value = depth * y

      if str (v.j) != "None":
        j = v.j.value
        v.j.value = depth * j


  def rerange_x     (self):

     minimum = 0.0

     for v in self.values ():
       x = v.x.value
       if x == None:  continue
       if x < minimum:  minimum = x

     for v in self.values ():
       x = v.x.value
       if x == None:  continue
       v.x.value = x - minimum


  def rerange_y     (self):

     minimum = 0.0

     for v in self.values ():
       y = v.y.value
       if y == None:  continue
       if y < minimum:  minimum = y

     for v in self.values ():
       y = v.y.value
       if y == None:  continue
       v.y.value = y - minimum
 


  def rerange_z     (self):

     minimum = 0.0

     for v in self.values ():
       z = v.z.value
       if z == None:  continue
       if z < minimum:  minimum = z

     for v in self.values ():
       z = v.z.value
       if z == None:  continue
       v.z.value = z - minimum
  

  def __call__     (self):

    ks = [ k for k in self.keys ()]
    ks.sort ()
    vs = [ self [k] for k in ks ]
    return self.SEPERATOR.join ([v() for v in vs])
    



depth = 0.0

def deep   (a, s):  
  global depth
  
  try:
    depth = float (a)

  except:
    pass



def flipx  (a, s):  s.flip_x_moves  (); 
def flipy  (a, s):  s.flip_y_moves  (); 
def flipxy (a, s):  s.flip_x_moves  (); s.flip_y_moves  ();
def flipz  (a, s):  s.flip_z_moves  ();
def scalex (a, s):  s.scale_x_moves  (depth); 
def scaley (a, s):  s.scale_y_moves  (depth); 
def scalexy(a, s):  s.scale_x_moves  (depth); s.scale_y_moves  (depth);
def mirx   (a, s):  s.flip_x_moves  (); s.rerange_x ();
def miry   (a, s):  s.flip_y_moves  (); s.rerange_y ();
def mirxy  (a, s):  s.flip_x_moves  (); s.flip_y_moves  (); s.rerange_x (); s.rerange_y ()
def mirz   (a, s):  s.flip_z_moves  (); s.rerange_z ();
def rx     (a, s):  s.rerange_x (); 
def ry     (a, s):  s.rerange_y (); 
def rxy    (a, s):  s.rerange_x (); s.rerange_y ()
def rz     (a, s):  s.rerange_z ();
def insz   (a, s):  s.normalize(10); s.add_z_moves (depth)
def nop    (a, s):  pass


if __name__ == '__main__':
  import sys

  if len (sys.argv) == 1:
    print ("""
PYTHON 3.1

GCODE TRANSPOSITION UTILITY:
Copyright 2008 by Aule (http://aule.ganoksin.com/blogs/), all rights reserved.

This code may be used to help in engraving or machining by either for-profit or 
not-for-profit organizations.   This code's other usage conditions are covered 
under the original GNU Public License.  This code may be incorporated or linked
or aggregated with another project only if appropriate attribution is given.

python gcode.py [ <command> ... <command> ] < -standard input- > -standard output-

commands:
      FX  : flip sign of X coordinates
      FY  : flip sign of Y coordinates
      FXY : flip sign of both X and Y coordinates
      FZ  : flip sign of Z coordinates
      MX  : mirror horizontal in place
      MY  : mirror vertical in place
      MXY : mirror vertical and horizontal in place
      MZ  : mirror depth in place
      Z   : insert z movements where needed to protect cutter
      RX  : rerange X movements to positive range
      RY  : rerange Y movements to positive range
      RXY : rerange to first quadrant
      RZ  : rz
      <floating point number> : set depth of z movements (default -0.01)

example

python gcode.py -0.1 Z < heart.txt > result.txt
      will insert z movements at - and + 0.1 as needed to plunge cutter or protect cutter
      (reverse the sign if plunge is in opposite direction!)

python gcode.py MXY < result.txt > resultmxy.txt
      will mirror image across x and y axes but keep image in the first quadrant

python gcode.py FXY < result.txt > resultfxy.txt
      will flip image to fourth quadrant

""")
    exit (0)

  s = GCode ()
  s.set (sys.stdin.read ())

  for arg in sys.argv:
    {
      'FX'   : flipx,
      'FY'   : flipy,
      'FZ'   : flipz,
      'FXY'  : flipxy,
      'MX'   : mirx,
      'MY'   : miry,
      'MZ'   : mirz,
      'MXY'  : mirxy,
      'RX'   : rx,
      'RY'   : ry,
      'RXY'  : rxy,
      'RZ'   : rz,
      'S'    : scalexy,
      'SX'   : scalex,
      'SY'   : scaley,
      'Z'    : insz,
    }.get (arg, deep)(arg, s)
    
   
  print (s ())
