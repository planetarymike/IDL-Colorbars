;;as long as loadcsvcolorbar is in the same location as the color
;;information (ie, directory structure matches the github repo), this
;;will put IDL in the right place in a system-independent way
colortabledir = file_dirname(file_which('loadcsvcolorbar.pro'))+"/"
colortablefile = colortabledir+"mycolorbars.tbl"
rgbdir = colortabledir+"IDL_rgb_values/"
