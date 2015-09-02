;;LOADCSVCOLORBAR.PRO
;;commands to load a CSV color table file from a local directory,
;;along with some colorbrewer qualitative colors in selected indices,
;;as defined in qualcolors.pro
;;
;; OPTIONAL:
;;
;; COLORTBL: the CSV file basename (no directory or extension) or
;; index of the colorbar to load. This must refer to a three column
;; CSV file with RGB values of the colors to load into the color
;; table. Interpolation will be performed over the color entries to
;; fit the color table into the available space. If omitted, the user
;; can interactively select from the available colorbars via a dialog.
;;
;; DIRECTORY=: overrides the default search directory with a user
;; specified directory.
;;
;; /SILENT: when loading a color table by index, by default the name
;; of the color table is printed. With this flag set, no output is
;; printed.
;;
;; /REVERSE: load the color table so that the color indices in IDL are
;; reversed relative to the order in the file.
;;
;; /NOQUAL: load the color table without the qualitative colorbrewer
;; colors. Unless the color table contains them at the ends of the
;; range, white and black will not be accessible with this flag
;; enabled.
;;
;; RGB_TABLE=: return 3x256 array of the RGB values loaded into the
;; current color table.


pro loadcsvcolorbar, colortbl, $
                     directory = directory, $
                     silent = silent, $
                     reverse = reverse, $
                     noqual = noqual,  $
                     rgb_table = rgb_table


  if keyword_set(directory) then begin
     ;;user-specified absolute directory
     rgbdir = directory
  endif else begin
     ;;find RGB table directory (by default IDL_RGB_VALUES/ in the same
     ;;directory as this procedure file on the IDL path)
     @'colorbar_filenames.pro'
     ;;this defines the directory we want as rgbdir
  endelse

  
  if n_elements(colortbl) GT 0 then begin
     ;;user specified a colorbar
     if size(colortbl, /type) EQ 7 then begin 
        ;;string colortbl, this is a filename, just add the directory
        ;;and extension
        colortbl = rgbdir+colortbl+".dat"
        if ~keyword_set(silent) then print, "Loading color bar from CSV file: ", colortbl
     endif else if size(colortbl, /type) EQ 2 then begin
        ;;by integer, get the filenames and pick the right one
        colorbarnames = file_basename(file_search(rgbdir+"/*"), '.dat')
        if ~keyword_set(silent) then print, "Loading CSV color bar: ", colorbarnames[colortbl]
        colortbl = rgbdir+colorbarnames[colortbl]+".dat"
     endif else begin
        print, "I'm not sure which colorbar you're trying to load, please pick by hand:"
     endelse
  endif else begin
     colorbarnames = file_basename(file_search(rgbdir+"/*"), '.dat')
     print, colorbarnames,  format = '(A30,A30,A30)'
     read, choice, prompt = "Select colorbar number: "
     colortbl = rgbdir+colorbarnames[choice]+".dat"
  endelse
  
  COMMON colors, r_orig, g_orig, b_orig, r_curr, g_curr, b_curr
  ;;@colors_com

  ;;load the RGB values from file
  mytbl = read_csv(colortbl)

  ;;setup color arrays
  myr = indgen(256)
  myg = indgen(256)
  myb = indgen(256)

  ;;get the qualitative color info
  @'qualcolors.pro'
  myr[qi] = qr
  myg[qi] = qg
  myb[qi] = qb

  ;;the color indices usable in the colorbar are therefore
  if max(qi) EQ !d.table_size-1 and max(qi)-min(qi)+1 EQ nqual then begin
     ;;qualcolors are at top of color table
     bottom_c = 0
     top_c = !d.table_size-nqual-1
  endif else if min(qi) EQ 0 and max(qi)-min(qi)+1 EQ nqual then begin
     ;;qualcolors are at bottom of color table
     bottom_c = nqual
     top_c = !d.table_size-1
  endif else begin
     print, "**********************************************************"
     print, "*************Error in loadcsvcolorbar.pro*****************"
     print, "**********************************************************"
     print, "Cannot determine where the qualitative colors are located,"
     print, " disabling qualitative colors."
     print, ""
     print, "Colorbar "+file_basename(colortbl)+" will be loaded "
     print, " without qualitative indices. Check qualcolors.pro to "
     print, " remedy the problem."
     print, "**********************************************************"
     print, "**********************************************************"
     print, "**********************************************************"
     noqual = 1
  endelse
     
  if keyword_set(noqual) then begin
     bottom_c = 0
     top_c = !d.table_size-1
  endif
  
  ;;now interpolate the color bar to the appropriate size
  interpr = interpolate(float(mytbl.field1), findgen(top_c-bottom_c+1) $
                                       *(n_elements(mytbl.field1)-1)/(top_c-bottom_c))
  interpg = interpolate(float(mytbl.field2), findgen(top_c-bottom_c+1) $
                                       *(n_elements(mytbl.field1)-1)/(top_c-bottom_c))
  interpb = interpolate(float(mytbl.field3), findgen(top_c-bottom_c+1) $
                                       *(n_elements(mytbl.field1)-1)/(top_c-bottom_c))

  ;;correct for RGB values that run from 0->1
  if max(interpr) > max(interpg) > max(interpb) LT 1.1 then begin
     ;;if values run from 0 to 1, multiply to put into IDL 0-255 range
     interpr *= 255
     interpg *= 255
     interpb *= 255
  endif

  ;;add the colorbar values from file to the rgb
  if keyword_set(reverse) then begin
     myr[bottom_c:top_c] = reverse(interpr)
     myg[bottom_c:top_c] = reverse(interpg)
     myb[bottom_c:top_c] = reverse(interpb)
  endif else begin
     myr[bottom_c:top_c] = interpr
     myg[bottom_c:top_c] = interpg
     myb[bottom_c:top_c] = interpb
  endelse

  ;;return the rgb values of this colorbar
  tvlct, r, g, b, /get
  r = myr
  g = myg
  b = myb
  tvlct, r, g, b

  ;;Important!  Update the colors common block.  
  r_curr = r
  g_curr = g
  b_curr = b

  if arg_present(rgb_table) then begin
     ;;return the rgb values into a 3x256 array
     rgb_table = make_array(3, 256)
     rgb_table[0, *] =  r
     rgb_table[1, *] =  g
     rgb_table[2, *] =  b
  endif


  if ~keyword_set(noqual) then begin
     ;;if we have qualitative colors, then set the global plot
     ;;variables to some nice defaults. Otherwise, the user is on
     ;;their own!
     !p.color = gray50
     !p.background = white
  endif

  ;;tplot global options to make sure the colorbars don't use
  ;;the qualitative colors
  if file_which('tplot_options.pro') NE "" then begin
     tplot_options, 'bottom', bottom_c
     tplot_options, 'top', top_c
  endif
  
end