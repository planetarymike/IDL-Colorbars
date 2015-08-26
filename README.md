# IDL-Colorbars
RGB values and helper routines for IDL colorbars.

Included is a new IDL colortable file with the new Matplotlib perceptual colorbars, as designed by Stéfan van der Walt and Nathaniel Smith (http://bids.github.io/colormap/). These colorbars are better than most of the builtin IDL default colorbars. To see why, you can look at the .png files located in the IDL_py_png directory, which apply the python-based sequential colormap analysis tools to the IDL builtin maps. Aside from the monochromatic and colorbrewer color bars, almost all IDL colorbars suffer from extreme deficiencies in perceptual uniformity and colorblind friendliness. By contrast, the new colorbars are perceptually uniform, colorblind friendly, and print correctly in black and white.

Also included is a series of routines to read in RGB colorbars from CSV files and load them into the current colortable, along with a series of qualitative colors. These colors are taken from a colorbrewer qualitative scheme (http://colorbrewer2.org/?type=qualitative&scheme=Set1&n=8), supplemented with some unsaturated grays. This allows IDL to have access to a decent colorbar and a set of good qualitative colors simultaneously, which is surprisingly difficult in vanilla IDL.

To install, clone the entire repository onto your machine and add it to your IDL !PATH variable. All of the routines should compile on demand and find the files and directories they need automatically.

To load a table from the supplied colortable, point loadct at the location of the table file:
loadct, file='/path/to/IDL-Colorbars/mycolorbars.tbl'. The new perceptual schemes are stored at the end of the table, in indices 75 and on.

To load a set of qualitative colors and a colorbar from file, use the command loadcsvcolorbar. You can specify the filename of a colorbar CSV file, relative to the IDL_rgb_values directory, or call it without arguments and see a list of all the colorbar files hosted in this directory, and select which one to load by number.

Interpolation is performed in RGB space on the input CSV file, to compress or expand the input color arrays to the space available in the IDL colortable. For this reason, it is possible to create new RGB colorbars easily in CSV format. Two examples are given in the colorbar_csv_source directory, bw.csv and brw.csv . Because RGB colorspace is not perceptually uniform, it's best to keep it simple with manually entered color tables, and leave creating new perceptually uniform color bars to languages with a more robust color handling system than IDL. 

When using qualitative colors, make sure that any array display commands, such as tv or tvscl, refer only to indices in the quantitative scheme. One way to do this is to bytscl images into the appropriate range. At the moment, the number of qualitative colors loaded is 13, so that images should be scaled to the values 13-255 before being displayed. This is possible, for example, using the commands

    sclarr=bytscl(arr,top=(255-13))+13
    tv, sclarr

tvscl will not work, because IDL has no bottom keyword for these commands.

If you are using tplot, written in large part by Davin Larson (available here: http://themis.ssl.berkeley.edu/software.shtml), then this scaling can be accomplished for all spectrogram plots by setting

    tplot_options, 'bottom', 13
    tplot_options, 'top', 255

This is done automatically by loadcsvcolorbar if it detects tplot on your IDL path.

I recommend adding qualcolors.pro to your IDL startup script. This sets some variable names to their qualitative indices (eg red = 0). Otherwise, the indices and color names are available through the command printcolornames, which does what it says on the tin. qualcolors.pro also defines the usable range of colors in the color bar and the number of qualitative colors as variable names, so that you can replace the magic numbers in the tvscl example above with

    sclarr=bytscl(arr,top=(top_c-bottom_c))+bottom_c
    tv, sclarr

Many routines and files hosted here, particularly those in the IDL_py_test/ and colorbar_csv_source/ directories, are useful only if you want to reproduce the work I did to export the IDL color tables, analyze them with the python tools, and import new colortables into IDL. This work requires the python viscm toolkit, available here: https://github.com/matplotlib/viscm . There's also an unfortunate detour into Mathematica to perform some basic file generation (basically, to convert IDL csv tables to the viscm format), as I don't yet know how to do this sort of thing in Python (I'm sure it's easy!).

