# IDL-Colorbars

Description
-----------
This repository is designed to get decent colormaps into IDL. To learn more about why to use perceptually uniform color maps, as opposed to the more typical rainbow color map ubiquitous in science, look at these slides I made, as well as the embedded references: https://docs.google.com/presentation/d/1JYg041YcdfGe_FhuJCuNK1NvlO0uXZdfkDUSXdS0Iko/edit?usp=sharing . These slides are also included as a PDF file in this repository.

Included is a new IDL colortable file with the new Matplotlib perceptual colorbars, as designed by Stéfan van der Walt and Nathaniel Smith (http://bids.github.io/colormap/). These colorbars are better than most of the builtin IDL default colorbars. To see why, you can look at the .png files located in the IDL_py_png directory, which apply the python-based sequential colormap analysis tools to the IDL builtin maps. Aside from the monochromatic and colorbrewer color bars, almost all IDL colorbars suffer from extreme deficiencies in perceptual uniformity and colorblind friendliness. By contrast, the new colorbars are perceptually uniform, colorblind friendly, and print correctly in black and white. 

Also included is a series of routines to read in RGB colorbars from CSV files and load them into the current colortable, along with a series of qualitative colors. These colors are taken from a colorbrewer qualitative scheme (http://colorbrewer2.org/?type=qualitative&scheme=Set1&n=8), supplemented with some unsaturated grays. This allows IDL to have access to a decent colorbar and a set of good qualitative colors simultaneously, which is surprisingly difficult in vanilla IDL.

Installation
------------
To install, clone the entire repository onto your machine and add it to your IDL !PATH variable. All of the routines should compile on demand and find the files and directories they need automatically.

To improve interaction with loadcsvcolorbar, I recommend adding qualcolors to your IDL startup script. You can do this by appending the line

	@'qualcolors'

to your startup file. This script load a structure that stores information about qualitative colors, for intuitive access (eg qualcolors.red = 0). Otherwise, the indices and color names are available through the command printcolornames, which does what it says on the tin. qualcolors also defines the usable range of colors in the color bar and the number of qualitative colors as variable names.

To check that you've installed everything correctly, you can run the following commands:

	loadcsvcolorbar, 78, /noqual ;;loads the Matplotlib 'option B' colorbar
	window, 0, xsize=256, ysize=256 ;;prepares an appropriately sized X window
	tvscl, rebin(rebin(indgen(256),256.*256),[256,256]) ;;plots a 256x256 horizontally increasing array

If the package is successfully installed, you should see this in your X window:

![idl_png_out](https://cloud.githubusercontent.com/assets/13734186/9619362/9f0b4e26-50cc-11e5-845f-d2ad6c905d57.png)

If you see a black and white version of the above, try running this command and trying again:

	device, true=24, decompose=0, retain=2

You may wish to add this command to your startup file, in a seperate script or by uncommenting the line in qualcolors that does this for you.

Loading Color Tables
--------------------
**Using loadcsvcolorbar**

To load a set of qualitative colors and a colorbar from file, use the command 

  	loadcsvcolorbar

You can specify the filename of a colorbar CSV file, relative to the IDL_rgb_values directory, or call it without arguments and see a list of all the colorbar files hosted in this directory, and select which one to load by number. Examples:

	loadcsvcolorbar, 80 ;; loads Matplotlib option D
	loadcsvcolorbar, '80_MPL_option_D' ;; same as above
	loadcsvcolorbar ;; no argument, displays a list of options and asks the user to select by number

By default, a set of qualitative colors is loaded along with the specified quantitative colormap, comprising eight colorbrewer colors (http://colorbrewer2.org/?type=qualitative&scheme=Set1&n=8) and 5 intervals of gray from black to white. If qualcolors is on your IDL !PATH, you can refer to these colors with named elements of the qualcolors structure referring to the appropriate color indices (eg, color=qualcolors.blue). To disable loading these qualitative colors, use the /noqual keyword, but beware! this may mean you cannot access black or white.

Other keywords include:
* /reverse, which loads the color table in reverse order (especially useful for colorbrewer monotonic schemes);
* directory= , which specifies the search directory for RGB data files;
* /silent, which disables echoing of loaded colorbar name to terminal; and
* rgb_table= , which returns a 3x256 array of the RGB values loaded to the user, respecting both /reverse and /noqual.
* low_quant=, which limits the loaded values to start at the specified quantile of the colors in the original table.
* high_quant=, which limits the loaded values to end at the specified quantile of the colors in the original table.

**Using loadct (not recommended)**

To load a table from the supplied colortable, point loadct at the location of the table file:

	loadct, file='/path/to/IDL-Colorbars/mycolorbars.tbl' 

The new perceptual schemes are stored at the end of the table, in indices 75 and on.

**Object graphics**

If you are using object graphics, the keyword rgb_table will return a 3x256 array of the RGB color values in the default color table, so that you can pass this to the plot() function. Unless you specify otherwise, a set of qualitative colors will be included in this array. Best to call like so:

       loadcsvcolorbar, 78, rgb_table=rgb_table, /noqual

This will put the Matplotlib option B color RGB values into the rgb_table array. You can use the /reverse keyword as well to swap the order of the colortable.

**Defining new colormaps**

This is as easy as adding a new 3 column CSV file of RGB values to the IDL_rgb_values/ directory, following the naming convention already present in the directory. RGB values can range either from 0-1 or 0-256 (the package assumes that CSV files with any entries larger than 1 are scaled from 0-256). The number of rows must be at least two, but is otherwise unrestricted.

Interpolation is performed in RGB space on the input CSV file, to compress or expand the input color arrays to the space available in the IDL colortable. For this reason, it is possible to create new RGB colorbars easily in CSV format. Two examples are given in the make_csv directory, bw.csv and brw.csv . Because RGB colorspace is not perceptually uniform, it's best to keep it simple with manually entered color tables, and leave creating new perceptually uniform color bars to languages with a more robust color handling system than IDL. 

Colormaps available
-------------------
Here is a graphical description of the available colormaps:
![all_idl_tables](https://github.com/planetarymike/IDL-Colorbars/blob/master/all_idl_tables.png)


Plotting Heatmaps
-----------------
When using qualitative colors, make sure that any array display commands, such as tv or tvscl, refer only to indices in the quantitative scheme. One way to do this is to bytscl images into the appropriate range. At the moment, the number of qualitative colors loaded is 13, so that images should be scaled to the values 13-255 before being displayed. This is possible, for example, using the commands

    sclarr=bytscl(arr,top=(255-13))+13
    tv, sclarr

tvscl will not work, because IDL has no bottom keyword for these commands. 

If you added qualcolors to your startup script, you can replace the magic numbers in the tvscl example above with

    sclarr=bytscl(arr,top=(qualcolors.top_c-qualcolors.bottom_c))+qualcolors.bottom_c
    tv, sclarr

Interaction with tplot
----------------------
If you are using tplot, written in large part by Davin Larson (available here: http://themis.ssl.berkeley.edu/software.shtml), then telling tplot to use only the quantitative colors for all spectrogram plots is done with the commands

    tplot_options, 'bottom', qualcolors.bottom_c ;; bottom_c = 13
    tplot_options, 'top', qualcolors.top_c ;; top_c = 255

These commands are run automatically by loadcsvcolorbar if it detects tplot on your IDL path.

You may experience a problem where color scales are not drawn after loading the package. This happens if you use do not use qualitative colors, because the color bar spans indices 0-255, and tplot checks if it can draw a color scale by calling keyword_set(bottom), which is terrible and not the proper syntax. You can fix this by running

    tplot_options, 'bottom', qualcolors.bottom_c+1 ;; bottom_c = 13
    tplot_options, 'top', qualcolors.top_c ;; top_c = 255

These commands are run if you load a colorbar without qualitative colors while using tplot.

Additional Notes
----------------
Many routines and files hosted here, particularly those in the IDL_py_test/ and make_csv/ directories, are useful only if you want to reproduce the work I did to export the IDL color tables, analyze them with the python tools, and import new colortables into IDL. This work requires the python viscm toolkit, available here: https://github.com/matplotlib/viscm . There's also an unfortunate detour into Mathematica to perform some basic file generation (basically, to convert IDL csv tables to the viscm format), as I don't yet know how to do this sort of thing in Python (I'm sure it's easy!).

