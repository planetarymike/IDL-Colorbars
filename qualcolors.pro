;;defined color indices and names, referenced by loadcsvcolorbar.pro,
;;printcolornames.pro, and possibly in graphics setup.

;;MAKE SURE TO CHANGE BOTH INDEX, NAME, AND RGB VALUES IF CHANGES ARE MADE

red = 0
green = 1 
blue = 2
purple = 3 
orange = 4
yellow = 5
brown = 6 
pink = 7
;;and a few unsaturated grays
black = 8
gray25 = 9
gray50 = 10
gray75 = 11
white = 12
;;total number of qualitative colors is
nqual = 13

;;color names
colornames = [ 'red', 'green', 'blue', 'purple', 'orange', $
               'yellow', 'brown', 'pink', 'black', 'gray25', 'gray50', $
               'gray75', 'white']

;;color RGB values, from a colorbrewer qualitative table
qi=[red, green, blue, purple, orange, yellow, brown, pink, black, gray25, gray50, gray75, white]
qr=[228,    77,   55,    152,    255,    255,   166,  247,     0,     59,    119,    185,   255]
qg=[ 26,   175,  126,     78,    127,    255,    86,  129,     0,     59,    119,    185,   255]
qb=[ 28,    74,  184,    163,      0,     51,    40,  191,     0,     59,    119,    185,   255]
