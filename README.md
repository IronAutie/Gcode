# Gcode
Gcode processing tools

GCODE TRANSPOSITION UTILITY:
Copyright 2008 by Aulë (http://aule.ganoksin.com/blogs/), all rights reserved.

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
      RX  : rx,
      RY  : ry,
      RXY : rxy,
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
