;;a routine to write all IDL colortable RGB values out to CSV text
;;files
pro write_idl_rgb_values, loadctfile = loadctfile
  ;;color information directory
  @'colorbar_filenames.pro'
  ;;we want to output RGB information to rgbdir, from color table file colortablefile
  
  if ~keyword_set(loadctfile) then loadctfile = colortablefile

  ;;get the length of each defined color table and the list of color
  ;;table names
  ncolors = !d.table_size
  loadct, get_names=colortablenames, file = loadctfile
  
  ncolortables = n_elements(colortablenames)

  for i = 0, ncolortables-1 do begin
     ;;extract the rgb data
     loadct, i, rgb_table=rgb_table, file = loadctfile
     
     fname = strtrim(string(i), 2) + "_" + colortablenames[i] + ".dat"
     ;;special character treatment
     fname = strjoin(strsplit(fname, " ", /extract), "_")
     fname = strjoin(strsplit(fname, "/", /extract), "-")
     fname = strjoin(strsplit(fname, "+", /extract), "plus")
     ;;pad values less than 10 for ease of filesystem sorting
     if i LT 10 then fname = '0'+fname
     fname = rgbdir+fname

     ;;amazingly, write_csv writes column-major, while read_csv reads
     ;;row-major! So to fix this we must transpose on output.
     write_csv, fname, transpose(rgb_table)
  endfor

end
     
