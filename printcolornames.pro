;;prints names and indices for named colors loaded by loadcsvcolorbar
pro printcolornames
  @'qualcolors'
  colorindex = indgen(size(colornames, /n_elements))

  print, 'Here are the defined named colors usable with a loadcsvcolorbar command:'
  for i = 0, size(colornames, /n_elements)-1 do begin
     print, colorindex[i], ": ", colornames[i]
  end
end
