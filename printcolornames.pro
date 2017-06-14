;;prints names and indices for named colors loaded by loadcsvcolorbar
pro printcolornames
  @'qualcolors'

  print, 'Here are the defined named colors usable with a loadcsvcolorbar command:'
  for i = 0, size(qualcolors.colornames, /n_elements)-1 do begin
     print, qualcolors.qi[i], ": ", qualcolors.colornames[i]
  end
  
end
