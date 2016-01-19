from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.000019872508023912684, 0.000019586801788918958, 0.000019529289536969018],
[0.00039604584052443947, 0.00032667266029436863, 0.00027448448256426830],
[0.0011821691681321357, 0.00092335895922523905, 0.00072658593845017876],
[0.00235386, 0.0017706305409428381, 0.0013223087696326663],
[0.0039013377774062322, 0.0028485695766541593, 0.00202959],
[0.00581908, 0.0041445800210534473, 0.0028251676012923566],
[0.0081032805652593559, 0.0056500297202465473, 0.0036906925422785912],
[0.010750879560582098, 0.0073588005720749816, 0.00461103],
[0.013759075482077670, 0.0092665304434616444, 0.0055733245961935365],
[0.017125073046201214, 0.011370167854469914, 0.0065664699904971029],
[0.020845929294860069, 0.013667688737147111, 0.0075807400667538723],
[0.024918457692110249, 0.016157905483626406, 0.0086075546094171399],
[0.029339165175695184, 0.018840332330412182, 0.0096393042820851812],
[0.034104209496405115, 0.021715087023436823, 0.010669221389580897],
[0.039209369672770410, 0.024782816862201407, 0.0116913],
[0.044460840383811671, 0.028044641699951658, 0.012700119365062004],
[0.049628105418853576, 0.0315021, 0.013690975775190932],
[0.0547241, 0.035157158242180103, 0.014659633859194826],
[0.059751306715670714, 0.039012090821843905, 0.015602379646900311],
[0.064711958268927339, 0.0429785, 0.016516],
[0.0696077, 0.046908274441175062, 0.017397561233545772],
[0.074440021562576231, 0.050814455474700017, 0.018244754792363302],
[0.079209924312089064, 0.054700479211757184, 0.0190555],
[0.0839183, 0.058569493083537157, 0.019828083686070357],
[0.088565839436605731, 0.062424377238814978, 0.020561148961882374],
[0.093153000072792202, 0.066267777557233620, 0.021253627114298776],
[0.097680124360977200, 0.070102133076022616, 0.021904743367298769],
[0.10214741159389790, 0.073929698945703892, 0.022513995212425676],
[0.10655494371109597, 0.077752565775869975, 0.023081136876426135],
[0.11090269907740641, 0.081572676042636211, 0.023606165005487543],
[0.11519056420262372, 0.085391838086601724, 0.024089305485413364],
[0.11941834376468594, 0.089211738121430934, 0.024531001336057262],
[0.12358576922560144, 0.093033950589512915, 0.024931901632894323],
[0.127693, 0.096859947136214153, 0.025292851419754393],
[0.13173816127445523, 0.10069110442335527, 0.025614882585251443],
[0.13572228690283608, 0.10452871096237346, 0.025899205681895760],
[0.13964438705192392, 0.10837397311566119, 0.026147202671726988],
[0.14350392115407679, 0.11222802038895183, 0.026360420585899730],
[0.14730030798256402, 0.11609191011695694, 0.026540566088265226],
[0.15103292901275345, 0.11996663162767871, 0.026689500934832716],
[0.15470113140313246, 0.12385310995711610, 0.026809238322232878],
[0.15830423064789254, 0.12775220917483573, 0.026901940119071960],
[0.16184151294505123, 0.13166473537158482, 0.026969914974465634],
[0.165312, 0.13559143935242537, 0.027015617298156682],
[0.16871563752047419, 0.13953301907244561, 0.027041647106515434],
[0.17205092375953959, 0.14349012184673959, 0.027050750728444054],
[0.17531728424943618, 0.14746334636182992, 0.027045822364795823],
[0.17851388662859147, 0.15145324451191256, 0.027029906494405256],
[0.18163987925143327, 0.15546032308008442, 0.027006201119225116],
[0.18469439237346824, 0.15948504528198623, 0.026978061840395105],
[0.18767653924362834, 0.16352783218698083, 0.026949006756332935],
[0.190585, 0.16758906403000087, 0.026922722173147749],
[0.19342, 0.17166908142552489, 0.026903069116822751],
[0.19618, 0.17576818649368492, 0.026894090635702871],
[0.198863, 0.17988664390727996, 0.026900019880841355],
[0.20146967522761827, 0.18402468186740842, 0.026925288950702068],
[0.20399817019173883, 0.18818249301452267, 0.026974538485574715],
[0.20644769307641475, 0.19236, 0.027052627995822562],
[0.20881725294393155, 0.19655803269007161, 0.0271646],
[0.21110584924807274, 0.20077597610744385, 0.027315926301293154],
[0.21331247253271390, 0.20501412394730584, 0.027512051340571175],
[0.21543610512911049, 0.20927250283919424, 0.0277589],
[0.21747572185726816, 0.21355110825766815, 0.028062528475631881],
[0.21943029073662063, 0.21784990511852226, 0.028429442100251483],
[0.221299, 0.22216882834441709, 0.028866353631318720],
[0.22308012739373895, 0.22650778340265865, 0.029380326989816043],
[0.22477330383554356, 0.230867, 0.029978767550807309],
[0.22637725132414910, 0.23524526666062484, 0.030669438571475697],
[0.22789091521691934, 0.239643, 0.031460478057117096],
[0.22931323881401167, 0.24406102844366162, 0.032360416022562274],
[0.23064316427672710, 0.24849772838996981, 0.033378192103007756],
[0.23187963359680280, 0.25295330163052654, 0.034523173464509692],
[0.23302158962256941, 0.25742746066607125, 0.035805172960471997],
[0.23406797714822841, 0.26191989212169153, 0.037234467476307133],
[0.23501774407293358, 0.26643025713516194, 0.038821816400110953],
[0.23586984263682442, 0.27095819173857877, 0.040576176473067958],
[0.236623, 0.27550330723514138, 0.042452038378703948],
[0.23727687336504033, 0.28006519057292600, 0.044458412966262788],
[0.23782974407557173, 0.284643, 0.0465958],
[0.23828082666202544, 0.28923748902509133, 0.048864135629889886],
[0.23862911688456889, 0.29384695961849938, 0.051263235051825930],
[0.23887362436212506, 0.29847130976697372, 0.053792441800296333],
[0.23901337460888916, 0.30311001027248607, 0.056450873179263707],
[0.23904741123527767, 0.30776250986385867, 0.059237425691414596],
[0.23897479833033325, 0.31242823560067984, 0.062150817579159946],
[0.23879462304466265, 0.31710659328880669, 0.065189627905333447],
[0.23850599839540210, 0.32179696790924822, 0.068352331634445762],
[0.23810806631748427, 0.32649872406221536, 0.071637330427579443],
[0.23760000098864398, 0.33121120642810359, 0.075042979075503113],
[0.23698101245932718, 0.33593374024714828, 0.078567607662242772],
[0.23625035062287591, 0.34066563181946735, 0.082209539676314669],
[0.23540730956632788, 0.34540616902716981, 0.085967106372896507],
[0.23445123234782583, 0.35015462188016250, 0.089838657742966760],
[0.23338151625326808, 0.35491024308724633, 0.093822570470939948],
[0.232198, 0.35967226865403312, 0.097917253266723597],
[0.23089906310362141, 0.36443991850914925, 0.10212114994698454],
[0.22948544704645596, 0.36921239716013365, 0.10643274061858701],
[0.22795644907377482, 0.37398889438033800, 0.11085054128865032],
[0.22631183798827337, 0.37876858592806922, 0.115373],
[0.22455148250502827, 0.383551, 0.11999900510625225],
[0.22267536216018580, 0.38833418951364673, 0.12472685984751852],
[0.22068357952782675, 0.39311838993852388, 0.12955530019763162],
[0.21857637393251639, 0.39790236314562966, 0.13448297937385637],
[0.216354, 0.402685, 0.13950856521509469],
[0.21401742941981844, 0.40746608962763853, 0.144631],
[0.211567, 0.41224405231504480, 0.14984817133357775],
[0.20900381587345357, 0.41701820858797922, 0.15515955516972430],
[0.206329, 0.42178764622221004, 0.160564],
[0.203544, 0.42655144813452150, 0.16605885963114048],
[0.200651, 0.43130869350421464, 0.17164409643308925],
[0.19765163626952331, 0.43605845893168738, 0.17731790404120726],
[0.19454845835026791, 0.44079981963342302, 0.18307888944165021],
[0.19134441760315837, 0.44553185067250128, 0.18892563163267251],
[0.18804289611640357, 0.45025362822355791, 0.19485667781934937],
[0.184648, 0.45496423087089971, 0.20087053987539072],
[0.18116373718296489, 0.45966274093827436, 0.20696569108003143],
[0.17759589018437283, 0.46434824584857975, 0.21314056313545071],
[0.17395032136499619, 0.46901983951157439, 0.21939354346813500],
[0.17023397604912471, 0.47367662373744263, 0.22572297281599774],
[0.16645482671334977, 0.47831770967385107, 0.23212714310177845],
[0.16262201251129610, 0.48294221926390629, 0.23860429559222601],
[0.15874599647416726, 0.487549, 0.24515261934175259],
[0.15483874130473097, 0.49213806002617117, 0.25177],
[0.15091390398391374, 0.49670770241889223, 0.25845526841079314],
[0.14698704827106260, 0.50125739392105129, 0.26520570070946731],
[0.14307587243556744, 0.50578633284739027, 0.27201951706516936],
[0.13920044700814985, 0.51029373732455752, 0.27889463191432995],
[0.13538345376612559, 0.514779, 0.28582890397116822],
[0.13165041236423500, 0.51924092358144103, 0.29282013658073197],
[0.12802987487011458, 0.52367925427206019, 0.29986607832820139],
[0.124554, 0.52809315131487711, 0.30696442389925455],
[0.12125639890005222, 0.53248195442412227, 0.31411281518591960],
[0.11817642721679114, 0.53684503202978873, 0.32130884263195680],
[0.11535451033871810, 0.54118178268724360, 0.32855004681141031],
[0.112834, 0.54549163645354259, 0.33583392023354475],
[0.11065900528490189, 0.54977405622581832, 0.34315790936695240],
[0.108875, 0.55402853903714799, 0.35051941687517496],
[0.10752623429542943, 0.55825461730531600, 0.35791580405570900],
[0.10665368229615321, 0.562452, 0.36534439347381437],
[0.10629442319393034, 0.56661987393351165, 0.37280247178207077],
[0.10647924142867810, 0.57075830454201237, 0.38028729271615774],
[0.10723125592625579, 0.57486683720086296, 0.38779608025686274],
[0.10856483124748406, 0.57894519802215338, 0.39532603194788796],
[0.11048504637181725, 0.582993, 0.402874],
[0.11298778475882446, 0.58701051760511014, 0.41043810668011482],
[0.11606041601884440, 0.59099713991076574, 0.41801452444394099],
[0.11968295572296714, 0.59495291882087653, 0.42560070334953981],
[0.12383, 0.59887779582327705, 0.43319376318994352],
[0.12847000165564271, 0.60277175720992826, 0.44079081986176111],
[0.13357147371722980, 0.60663483444689625, 0.44838898944689848],
[0.13909974802743757, 0.61046710445133212, 0.45598539235271857],
[0.14502046594979534, 0.61426868977375559, 0.46357715749725509],
[0.1513, 0.61803975868432415, 0.47116142652595044],
[0.15790622921218694, 0.62178052516210791, 0.47873535804631723],
[0.16480873535968346, 0.62549124878677742, 0.48629613186689774],
[0.17197928831532067, 0.62917223453250182, 0.49384095322693261],
[0.17939183297123762, 0.63282383246422524, 0.50136705700322481],
[0.18702251344379575, 0.63644643733689599, 0.50887171188084590],
[0.19484960136861365, 0.64004048809859571, 0.51635222447452123],
[0.20285337803847697, 0.64360646729891191, 0.52380594338779207],
[0.21101599019630229, 0.64714490040427985, 0.53123026319737676],
[0.21932129387268162, 0.65065635502238361, 0.53862262835050401],
[0.22775469625520917, 0.65414144003807140, 0.54598053696343485],
[0.23630300217299077, 0.65760080466360593, 0.55330154450984714],
[0.24495426925114172, 0.66103513740637543, 0.56058326738828956],
[0.25369767397602055, 0.66444516495754269, 0.56782338635847596],
[0.26252338965578281, 0.66783165100538389, 0.57501964983680398],
[0.27142247642277179, 0.67119539497736447, 0.58216987704212531],
[0.28038678289154373, 0.67453723071524319, 0.58927196098349088],
[0.28940885876947819, 0.67785802508773740, 0.59632387128229791],
[0.29848187754942473, 0.68115867654548667, 0.60332365682202071],
[0.30759956834633334, 0.68444011362322765, 0.61026944821945128],
[0.31675615593694406, 0.687703, 0.61715946011218792],
[0.32594630809868891, 0.69094919988237013, 0.62399199325787169],
[0.33516508940396822, 0.694179, 0.63076543644150140],
[0.34440792069711995, 0.69739325407403907, 0.63747826818794351],
[0.35367054355689803, 0.70059348979631264, 0.64412905827757272],
[0.36294898912137269, 0.70378062488488846, 0.65071646906377034],
[0.37223955072314285, 0.706956, 0.65723925659180105],
[0.38153875984818864, 0.71011998535435394, 0.66369627151936206],
[0.39084336499121997, 0.71327444716911503, 0.670086],
[0.40015031303408743, 0.71642027774711736, 0.676409],
[0.40945673282118322, 0.71955862783862035, 0.68266262028546132],
[0.41875992064793205, 0.72269065810241950, 0.68884696486414332],
[0.42805732741533581, 0.72581753740112887, 0.69496122784682623],
[0.43734654723574162, 0.72894044111610712, 0.701005],
[0.44662530730329714, 0.73206054948641430, 0.706977],
[0.45589145886687116, 0.735179, 0.71287827285362548],
[0.46514296916470815, 0.73829711567316469, 0.71870743104411561],
[0.47437791419842351, 0.74141594372574593, 0.72446459182539591],
[0.483594, 0.74453671381599451, 0.73014965306262514],
[0.49279091797958902, 0.747661, 0.73576260386868031],
[0.50196561723329092, 0.75078879865995740, 0.74130352327843674],
[0.51111702214178145, 0.75392246033679044, 0.74677257879441505],
[0.52024366679830081, 0.75706275517067134, 0.75217002481195505],
[0.52934416325343137, 0.76021083822649527, 0.75749620093231040],
[0.53841719785049380, 0.76336785494123693, 0.76275153017219410],
[0.54746152785140323, 0.76653493994978883, 0.76793651707845900],
[0.556476, 0.76971321596849263, 0.773052],
[0.56545943921813824, 0.77290379273746324, 0.77809787782249407],
[0.57441086273041087, 0.776108, 0.78307565028447024],
[0.58332926072343605, 0.77932621667746826, 0.78798587336752945],
[0.59221370239014781, 0.78256020976673402, 0.79282942828558867],
[0.60106331201886554, 0.785811, 0.797607],
[0.609877, 0.789079, 0.80232039977874026],
[0.61865479525451361, 0.79236584072598060, 0.80696991314621325],
[0.627395, 0.79567231111005410, 0.81155694726354144],
[0.63609772915235896, 0.79899938595541598, 0.81608270371649250],
[0.64476182942558091, 0.80234802055862853, 0.82054844113820213],
[0.65338688926948252, 0.80571914997231198, 0.824955],
[0.66197236488931233, 0.80911368860268385, 0.829305],
[0.67051775315548823, 0.81253252986279756, 0.83359893223718062],
[0.67902259008765997, 0.81597654588027002, 0.83783823931674606],
[0.687486, 0.81944658725825825, 0.842025],
[0.69590894096402456, 0.82294348288834795, 0.84615955224976114],
[0.70428970959950898, 0.82646803981404360, 0.85024470473112912],
[0.71262843349595773, 0.83002104314349268, 0.85428168577952679],
[0.72092482295257465, 0.83360325601012797, 0.85827216591936428],
[0.72917861901620351, 0.837215, 0.862218],
[0.73738959215075761, 0.84085825310413365, 0.86612048078308723],
[0.74555754091296744, 0.84453245401613541, 0.86998182648509870],
[0.753682, 0.84823869807182761, 0.87380368996601054],
[0.76176369206297845, 0.85197763953234806, 0.87758790189623770],
[0.76980162007756891, 0.85575, 0.88133632052327771],
[0.77779597226591046, 0.85955612562851336, 0.88505083051729117],
[0.78574666755751654, 0.863397, 0.88873334198961151],
[0.79365364477925915, 0.86727272607906902, 0.89238578970443194],
[0.80151686116028409, 0.87118423423031910, 0.89601013250745421],
[0.80933629076402403, 0.87513192947771046, 0.89960835299975572],
[0.81711192282729372, 0.87911632427474007, 0.90318245749087578],
[0.82484375998193626, 0.88313791258531593, 0.90673447627238746],
[0.83253181632854634, 0.88719717047810520, 0.91026646426263813],
[0.84017611532422598, 0.89129455678465075, 0.91378050208547490],
[0.84777668743627455, 0.89543051383077532, 0.917279],
[0.85533356750053458, 0.89960546825402299, 0.92076318841252580],
[0.862847, 0.90381983192419768, 0.92423614420346389],
[0.87031639409794070, 0.90807400298988050, 0.92769977119193148],
[0.877742, 0.91236836708187929, 0.93115631679632727],
[0.88512483349392901, 0.91670329871570078, 0.93460807607248497],
[0.89246368670108389, 0.92107916295106074, 0.93805739988430659],
[0.89975893723222367, 0.925496, 0.94150670539751491],
[0.90701052661094672, 0.929955, 0.94495848963357620],
[0.91421835101788818, 0.93445590530912059, 0.94841534713144504],
[0.921382, 0.93899904209155116, 0.95187999324026962],
[0.92850196616311253, 0.943585, 0.95535529531524077],
[0.93557715735510649, 0.94821380730298455, 0.958844],
[0.94260731783781604, 0.95288620746105213, 0.96235036930828344],
[0.94959174191654172, 0.957603, 0.96587711323649572],
[0.95652943515525080, 0.962363, 0.969429],
[0.963419, 0.96716895835817518, 0.97301],
[0.97025831437197774, 0.97202040425801972, 0.97662638839236282],
[0.97704431943193193, 0.97691856508216801, 0.98028571610256143],
[0.98377200210901294, 0.98186488333543342, 0.983998],
[0.99043252378901425, 0.98686175763956208, 0.987779],
[0.997007, 0.99191415614352951, 0.99165836747121527],
[1, 0.99704378266210936, 0.99575555752072120]]

test_cm = LinearSegmentedColormap.from_list(__file__, cm_data)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    try:
        from pycam02ucs.cm.viscm import viscm
        viscm(test_cm)
    except ImportError:
        print("pycam02ucs not found, falling back on simple display")
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',
                   cmap=test_cm)
    plt.show()