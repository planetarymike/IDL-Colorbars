;;IDL colortables run from 0-74, so we can add ours starting at 75

;;get colorbardir
@'colorbar_filenames'

modifyct_from_file, colorbardir+'cubehelix_rainbow_256.csv', 75, 'LAB rainbow'
modifyct_from_file, colorbardir+'MPL_rainbow.csv', 76, 'MPL rainbow'
modifyct_from_file, colorbardir+'matplotlib_option_a.csv', 77, 'MPL option A'
modifyct_from_file, colorbardir+'matplotlib_option_b.csv', 78, 'MPL option B'
modifyct_from_file, colorbardir+'matplotlib_option_c.csv', 79, 'MPL option C'
modifyct_from_file, colorbardir+'matplotlib_option_d.csv', 80, 'MPL option D'

