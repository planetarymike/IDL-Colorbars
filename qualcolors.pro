;;defined color indices and names, referenced by loadcsvcolorbar.pro,
;;printcolornames.pro, and possibly in graphics setup.

;;MAKE SURE TO CHANGE BOTH INDEX, NAME, AND RGB VALUES IF CHANGES ARE MADE

;;set up the device for true color
;;device, true=24,decompose=0,retain=2

;;here are the color definitions

;;qualitative colors must be in a single block at either the top or
;;bottom of the color table. Here, they are put at the top. 
red = !d.table_size-1
green = !d.table_size-2
blue = !d.table_size-3
purple = !d.table_size-4
orange = !d.table_size-5
yellow = !d.table_size-6
brown = !d.table_size-7
pink = !d.table_size-8
;;and a few unsaturated grays
black = !d.table_size-9
gray25 = !d.table_size-10
gray50 = !d.table_size-11
gray75 = !d.table_size-12
white = !d.table_size-13
;;total number of qualitative colors is
nqual = 13
top_c = !d.table_size-nqual-1
bottom_c = 0

;;color names
colornames = [ 'red', 'green', 'blue', 'purple', 'orange', $
               'yellow', 'brown', 'pink', 'black', 'gray25', 'gray50', $
               'gray75', 'white']

;;color RGB values, from a colorbrewer qualitative table
qi=[red, green, blue, purple, orange, yellow, brown, pink, black, gray25, gray50, gray75, white]
qr=[228,    77,   55,    152,    255,    255,   166,  247,     0,     59,    119,    185,   255]
qg=[ 26,   175,  126,     78,    127,    255,    86,  129,     0,     59,    119,    185,   255]
qb=[ 28,    74,  184,    163,      0,     51,    40,  191,     0,     59,    119,    185,   255]
