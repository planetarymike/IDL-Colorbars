pro loadcsvcolorbar, filename, reverse = reverse, silent = silent
  ;;commands to load my own color table combining qualitative colors
  ;;and a tabulated colorbar, based on Davin's loadct2

  ;;find RGB table directory
  @'colorbar_filenames.pro'
  ;;the directory we want is rgbdir
  
  if n_elements(filename) GT 0 then begin
     ;;user specified a colorbar
     if size(filename, type = 7) EQ 7 then begin 
        ;;by string filename, just add the directory
        filename = rgbdir+filename
     endif else if isa(filename, /integer) then begin
        ;;by integer, get the filenames and pick the right one
        colorbarnames = file_basename(file_search(rgbdir+"/*"), '.dat')
        if ~keyword_set(silent) then print, "Loading CSV color bar: ", colorbarnames[filename]
        filename = rgbdir+colorbarnames[filename]+".dat"
     endif else begin
        print, "I'm not sure which colorbar you're trying to load, please pick by hand:"
     endelse
  endif else begin
     colorbarnames = file_basename(file_search(rgbdir+"/*"), '.dat')
     print, colorbarnames,  format = '(A30,A30,A30)'
     read, choice, prompt = "Select colorbar number: "
     filename = rgbdir+colorbarnames[choice]+".dat"
  endelse
  
  COMMON colors, r_orig, g_orig, b_orig, r_curr, g_curr, b_curr
  ;;@colors_com

  ;;load the RGB values from file
  mytbl = read_csv(filename)

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
  bottom_c = 0
  top_c = !d.table_size-nqual-1

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
  
  r_curr = r                    ;Important!  Update the colors common block.
  g_curr = g
  b_curr = b

  !p.color = gray50
  !p.background = white

  ;;tplot global options to make sure the colorbars don't use
  ;;the qualitative colors
  if file_which('tplot_options.pro') NE "" then begin
     tplot_options, 'bottom', bottom_c
     tplot_options, 'top', top_c
  endif
  
end