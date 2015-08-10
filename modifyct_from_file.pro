;;loads an RGB colorbar from a CSV file into a specified index in the
;;IDL colortable, with a specified name.

pro modifyct_from_file, csv_filename, $
                        colortable_index, $
                        colortable_name, $
                        colortable_filename = colortable_filename
  
  if ~keyword_set(colortable_filename) then begin
     @'colorbar_filenames.pro'
     colortable_filename = colortablefile
  endif

  mytbl = read_csv(csv_filename)
  myr = indgen(256)
  myg = indgen(256)
  myb = indgen(256)

  ;;add the colorbar values from file to the rgb
  myr = mytbl.field1
  myg = mytbl.field2
  myb = mytbl.field3
  
  if max(myr) > max(myg) > max(myb) LT 1.1 then begin
     ;;if values run from 0 to 1, multiply to put into IDL 0-255 range
     myr *= 255
     myg *= 255
     myb *= 255
  endif

  ;;load this table into IDL's color table
  tvlct, myr, myg, myb
  modifyct, colortable_index, colortable_name, myr, myg, myb,  $
            file = colortable_filename
  
end