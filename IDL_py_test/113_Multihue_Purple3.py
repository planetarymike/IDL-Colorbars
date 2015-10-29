from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.000019872508023912684, 0.000019586801788918958, 0.000019529289536969018],
[0.00041127322738149810, 0.000317606, 0.00030368805485795296],
[0.0012435039105459682, 0.00088728016131298191, 0.00083958035061048675],
[0.0025014563816057678, 0.0016846040008852208, 0.0015859137256578079],
[0.0041844945413279065, 0.0026848072338675798, 0.00252205],
[0.00629632, 0.0038704529510779915, 0.0036356783149997245],
[0.0088425344652074272, 0.0052280147855776442, 0.0049192000063749989],
[0.011829746979179327, 0.0067463969650290697, 0.0063680743728801899],
[0.015265074769150833, 0.00841616, 0.0079799844128488878],
[0.0191559, 0.010229075478405743, 0.0097543260294145565],
[0.023509797287092491, 0.012177824916816784, 0.011691884819569754],
[0.028334267215938701, 0.014255822624051093, 0.013794618833818087],
[0.033636834706593372, 0.016457074263873536, 0.016065506947488557],
[0.0394249, 0.018776081426847720, 0.018508440092191911],
[0.0454341, 0.021207769723790387, 0.021128141710994714],
[0.051393033885418264, 0.023747434271084611, 0.023930108849898237],
[0.057315715627857582, 0.026390697636987051, 0.026920568251603848],
[0.063205687823364220, 0.0291335, 0.0301064],
[0.069065928263788046, 0.031971957811650062, 0.033495331406918467],
[0.074898931866923257, 0.034902573611999298, 0.037095483101595467],
[0.080706793080726619, 0.037921988717336333, 0.0409064],
[0.086491270706455098, 0.041015022470066241, 0.044753314450792538],
[0.092253839532189019, 0.044055871699751857, 0.048613501978096031],
[0.097995731924095636, 0.047043064105639305, 0.052491111255036409],
[0.10371797166933727, 0.049979340072961571, 0.056389968100011407],
[0.10942140176808918, 0.052867238428490331, 0.060313624367429076],
[0.11510670744820217, 0.0557091, 0.064265387491299813],
[0.12077443537007832, 0.058507215002775219, 0.068248345215745743],
[0.12642500976540635, 0.061263595930524529, 0.072265386419175348],
[0.13205874608738233, 0.063980241940257587, 0.0763192],
[0.137676, 0.066659029948041237, 0.080412383561182688],
[0.14327649044368396, 0.069301752046125598, 0.084547268798550013],
[0.14886068192772184, 0.071910126516165573, 0.088726119845870227],
[0.154428, 0.074485807434026108, 0.092951048966328637],
[0.15997961539834357, 0.077030393087164722, 0.097224043362610174],
[0.16551413053973132, 0.079545433385149994, 0.10154697211760447],
[0.17103176614730128, 0.082032436411673487, 0.10592159216368108],
[0.17653227469085686, 0.084492874240617771, 0.11034955341177674],
[0.18201536235893340, 0.086928188117905175, 0.11483240315000623],
[0.187481, 0.089339793093922981, 0.11937158980409429],
[0.19292788823242613, 0.091729082177472082, 0.12396846613778031],
[0.198357, 0.094097430070790966, 0.12862429195980418],
[0.20376618657810674, 0.096446196535767387, 0.13334023639461329],
[0.20915635884426603, 0.098776729433592031, 0.13811737976614480],
[0.21452654039748487, 0.10109036747353398, 0.14295671513761499],
[0.21987618993344538, 0.10338844270095884, 0.14785914954492330],
[0.22520473871544972, 0.10567228275003149, 0.15282550495686559],
[0.23051159203086818, 0.10794321288254050, 0.15785651899167671],
[0.23579613052689241, 0.11020255783086705, 0.16295284541636906],
[0.24105771144136612, 0.11245164346017206, 0.16811505445277014],
[0.24629566974257111, 0.11469179826235004, 0.17334363291203728],
[0.25150931919026837, 0.11692435469208476, 0.17863898417764537],
[0.25669795332893824, 0.11915065035343061, 0.18400142805534667],
[0.26186084642298602, 0.12137202904367494, 0.18943120050735576],
[0.26699725434269589, 0.12358984165976822, 0.19492845328697664],
[0.27210641540886399, 0.12580544697134055, 0.200493],
[0.27718755120329386, 0.12802021226320570, 0.206126],
[0.28223986735172413, 0.13023551384927637, 0.211825],
[0.28726255428519676, 0.13245273745899355, 0.21759232842054310],
[0.29225478798541382, 0.13467327849663860, 0.22342627684348232],
[0.29721573071921981, 0.13689854217330261, 0.22932681844623470],
[0.30214453176700085, 0.13912994351078825, 0.23529349998566995],
[0.30704032814947307, 0.14136890721632966, 0.24132577921572895],
[0.31190224535708844, 0.14361686742671456, 0.24742302424895263],
[0.31672939808603356, 0.14587526732020581, 0.25358451294959966],
[0.32152089098461462, 0.14814555859455655, 0.25980943236980791],
[0.32627581941362682, 0.15042920080941147, 0.26609687824005746],
[0.33099327022416458, 0.15272766059147958, 0.27244585452500830],
[0.33567232255618046, 0.15504241070105387, 0.27885527305559055],
[0.34031204866097498, 0.15737492895872823, 0.28532395324802917],
[0.34491151475069010, 0.15972669703154532, 0.29185062192025413],
[0.34946978187776290, 0.16209919907826956, 0.29843391321592849],
[0.35398590684720083, 0.16449392025403026, 0.305072],
[0.35845894316444638, 0.16691234507522343, 0.31176443725786857],
[0.36288794202148433, 0.16935595564627740, 0.31850847594028747],
[0.36727195332377271, 0.171826, 0.32530274987510238],
[0.37161002676045685, 0.17432463880951129, 0.33214543314237094],
[0.37590121292023859, 0.17685264571169523, 0.33903460948832242],
[0.38014456445515410, 0.179412, 0.34596827326348639],
[0.38433913729439906, 0.18200324806639445, 0.35294433053829555],
[0.38848399191022542, 0.18462870542172485, 0.35996060040284100],
[0.39257819463778065, 0.18728947928494596, 0.36701481645689238],
[0.396621, 0.189987, 0.37410462849563503],
[0.40061094739359593, 0.19272248708231984, 0.381228],
[0.40454767207414294, 0.19549741371051693, 0.38838123220701004],
[0.40843009721385126, 0.19831303644389736, 0.39556292244931507],
[0.41225734026068955, 0.20117062593172358, 0.40277001062325651],
[0.41602853366310799, 0.20407141717661487, 0.40999975993023008],
[0.41974282660646400, 0.20701660651741882, 0.41724936420620179],
[0.42339938681215295, 0.210007, 0.42451595106784368],
[0.42699740239952705, 0.21304475343002804, 0.43179658527005688],
[0.43053608381042702, 0.21612988328969068, 0.43908827227280345],
[0.434015, 0.21926374992562525, 0.44638796201412395],
[0.437432, 0.22244731163410775, 0.45369255288524962],
[0.44078860438828899, 0.22568147049462328, 0.46099889590265347],
[0.44408257077512220, 0.22896706969020703, 0.46830379907086256],
[0.44731366168734749, 0.23230489094194173, 0.47560403192884221],
[0.45048126532372940, 0.23569565207333676, 0.48289633027168583],
[0.45358480735037982, 0.23914000471972646, 0.49017740103838264],
[0.45662375328180199, 0.24263853219704346, 0.49744392735540416],
[0.45959761090818280, 0.24619174754345852, 0.50469257372488763],
[0.46250593276527790, 0.24980009174634882, 0.51191999134527433],
[0.46534831864279197, 0.253464, 0.51912282355134220],
[0.46812441812679323, 0.25718356116595187, 0.52629771135973946],
[0.47083393317124894, 0.26095919495951708, 0.53344129910532656],
[0.47347662069338320, 0.26479097267885227, 0.54055024015290465],
[0.47605229518714082, 0.26867895567377120, 0.54762120266823189],
[0.47856083134860677, 0.27262312704428310, 0.55465087543165492],
[0.48100216670686063, 0.27662339141023912, 0.56163597367714579],
[0.48337630425330941, 0.28067957491977069, 0.56857324493913430],
[0.48568331506214874, 0.284791, 0.57545947488915195],
[0.48792334089423023, 0.28895861332622807, 0.58229149314408912],
[0.49009659677620249, 0.29318073157487795, 0.58906617902768554],
[0.49220337354643146, 0.29745729734321308, 0.59578046726684219],
[0.49424404035884267, 0.30178775284372233, 0.60243135360437661],
[0.49621904713547521, 0.30617146679893231, 0.60901590031000108],
[0.49812892695817318, 0.31060773605176351, 0.61553124157154260],
[0.49997429838955071, 0.31509578737963251, 0.62197458874878664],
[0.50175586771301572, 0.31963477950281288, 0.62834323547276494],
[0.503474, 0.32422380527670652, 0.63463456257386230],
[0.505131, 0.32886189405692279, 0.64084604282276136],
[0.50672618607528930, 0.33354801422541819, 0.64697524546896334],
[0.50826143719248695, 0.33828107586539408, 0.65302],
[0.50973780481832098, 0.34305993357219233, 0.65897760304498876],
[0.51115656271003740, 0.34788338938708996, 0.66484641659838095],
[0.51251908484265585, 0.35275019584062189, 0.67062427723833851],
[0.51382684660104427, 0.35765905909189832, 0.67630929664335249],
[0.51508142578750837, 0.36260864215030192, 0.68189970520938747],
[0.51628450343241883, 0.36759756816597539, 0.68739385482228721],
[0.51743786439533013, 0.37262442377556587, 0.69279022134103230],
[0.51854339774393932, 0.37768776248987956, 0.69808740678626668],
[0.51960309689823902, 0.382786, 0.70328414122975968],
[0.520619, 0.38791795816125901, 0.70837928438178088],
[0.52159348718548948, 0.39308178732592530, 0.71337182687463641],
[0.52252868467754465, 0.39827605087363432, 0.71826089124190251],
[0.52342705913713050, 0.40349918806684809, 0.72304573259414939],
[0.524291, 0.40875, 0.72772573899319082],
[0.52512347152843442, 0.41402578061770467, 0.73230043152809809],
[0.52592682286588643, 0.41932606462777144, 0.73676946409738819],
[0.52670397396204127, 0.42464888609052714, 0.74113262290290660],
[0.52745781900746558, 0.42999265388470764, 0.74538982566200274],
[0.52819134237932752, 0.43535578031628797, 0.74954112054559230],
[0.52890761541984532, 0.44073668410454059, 0.75358668485066071],
[0.52960979285051946, 0.44613379327531261, 0.75752682341661270],
[0.53030110881643600, 0.45154554795530427, 0.76136196679570967],
[0.53098487255641536, 0.45697040306177422, 0.76509266918853325],
[0.53166446369645060, 0.46240683088275852, 0.76871960615607848],
[0.53234332716572230, 0.46785332354354242, 0.77224357212065753],
[0.53302496773657060, 0.47330839535574015, 0.77566547766826888],
[0.53371294419203852, 0.47877058504599251, 0.77898634666550992],
[0.53441086312707775, 0.48423845786187197, 0.78220731320443460],
[0.53512237239217097, 0.48971060755319412, 0.78532961838900028],
[0.53585115419097173, 0.49518565822748800, 0.78835460697694315],
[0.53660091784653907, 0.50066226607894759, 0.79128372389098045],
[0.53737539225394992, 0.50613912099067782, 0.79411851061329242],
[0.53817831804029648, 0.51161494801058116, 0.79686060147716664],
[0.53901343945648295, 0.51708850870166634, 0.79951171986958158],
[0.53988449602860067, 0.522559, 0.80207367435831767],
[0.54079521400010067, 0.52802406715816774, 0.80454835475695308],
[0.54174929759932877, 0.53348378104762684, 0.80693772814079656],
[0.54275042017027886, 0.538937, 0.80924383482647300],
[0.54380221520746241, 0.54438167223297340, 0.81146878432747416],
[0.54490826733875985, 0.54981781182034495, 0.813615],
[0.54607210330263811, 0.55524412625346864, 0.815684],
[0.54729718296840635, 0.56065970334545301, 0.817679],
[0.54858689045006526, 0.56606367425392023, 0.81960139554175271],
[0.54994452536556637, 0.57145521370220997, 0.821454],
[0.55137329429432591, 0.57683354010647348, 0.82324001088472865],
[0.55287630248594932, 0.58219791561284606, 0.82496088916359733],
[0.55445654587297322, 0.58754764604895193, 0.82661949314224170],
[0.556117, 0.59288208079408467, 0.828218],
[0.55786012999501933, 0.59820061257244406, 0.82976011520244131],
[0.55968884940415631, 0.60350267717386241, 0.83124732262210044],
[0.56160554831274856, 0.60878775310642941, 0.83268262721961894],
[0.56361257041647694, 0.61405536118545301, 0.83406867845431465],
[0.56571211130672228, 0.619305, 0.83540814153032594],
[0.567906, 0.62453646570321619, 0.83670369411507328],
[0.57019676467046765, 0.62974921080518165, 0.83795802315732015],
[0.57258549013215709, 0.63494298418170891, 0.83917382180771882],
[0.57507395454672228, 0.64011751009400686, 0.840354],
[0.57766355790782187, 0.64527255154875218, 0.84150061380407271],
[0.58035553478202273, 0.65040790956064931, 0.84261699822433611],
[0.58315095381247128, 0.655523, 0.84370562899102652],
[0.58605071790482710, 0.66061896471976378, 0.84476918779833054],
[0.58905556508148937, 0.665694, 0.84581034631753427],
[0.59216606998467614, 0.67074981401983924, 0.84683176387566672],
[0.59538264600341573, 0.67578504514816007, 0.847836],
[0.598706, 0.68080015239196900, 0.84882593853065724],
[0.602135, 0.68579518005124407, 0.84980393319097969],
[0.60567057687387982, 0.69077, 0.85077265812964964],
[0.60931245291721370, 0.69572532942256449, 0.851735],
[0.61306016225000037, 0.70066069266398712, 0.85269254110702342],
[0.616913, 0.70557645759184506, 0.85364875864767564],
[0.620871, 0.710473, 0.85460582240114913],
[0.62493284862768705, 0.71534998683184836, 0.855566],
[0.62909781364946027, 0.72020821453067641, 0.85653230430799698],
[0.63336495806304682, 0.72504776893705059, 0.85750655470218362],
[0.63773320347869256, 0.72986894404258273, 0.85849131346898388],
[0.64220137038904213, 0.734672, 0.85948891601689770],
[0.64676818468778296, 0.73945744837318472, 0.86050166368000569],
[0.65143228420849020, 0.74422547914382409, 0.86153182285063956],
[0.65619222524397003, 0.74897653207898263, 0.862582],
[0.66104648900917418, 0.75371100985794781, 0.86365326191276370],
[0.66599348801340918, 0.75842933452133510, 0.86474889314692349],
[0.67103157231058175, 0.76313194672299889, 0.86587063735981895],
[0.67615903559914425, 0.76781930500306306, 0.86702057585429859],
[0.68137412114637608, 0.77249188508311328, 0.868201],
[0.68667502751468268, 0.77715017918454166, 0.86941316749954101],
[0.69205991407034373, 0.78179469537102064, 0.87065978878465400],
[0.69752690625803449, 0.78642595691606776, 0.87194254004436889],
[0.70307410062702325, 0.79104450169665053, 0.87326330637903704],
[0.70869956959733282, 0.79565088161383601, 0.87462393298089192],
[0.71440136595654358, 0.80024566204147951, 0.87602622503865302],
[0.72017752707983262, 0.80482942130403867, 0.87747194769338610],
[0.72602607886768766, 0.80940275018466790, 0.87896282604436415],
[0.731945, 0.813966, 0.880501],
[0.73793242228481093, 0.81852053949700976, 0.88208675040053808],
[0.743986, 0.823066, 0.88372304712973970],
[0.75010450543022311, 0.82760398876042107, 0.885411],
[0.75628523679874182, 0.83213443319875269, 0.88715213974284335],
[0.76252645742753045, 0.836658, 0.88894794998134408],
[0.76882619885287262, 0.84117604686031877, 0.89079988110265273],
[0.77518250218666107, 0.84568856003524007, 0.89270934389224477],
[0.78159341942247151, 0.85019645628010299, 0.89467771133922669],
[0.78805701443892806, 0.85470043173127419, 0.89670631914754717],
[0.79457136369374559, 0.85920119209433055, 0.89879646631064891],
[0.80113455659886357, 0.86369945269239790, 0.90094941575579701],
[0.80774469556336392, 0.868196, 0.90316639506606478],
[0.81439989568595594, 0.87269138480539066, 0.90544859729010507],
[0.82109828407267804, 0.87718653661426860, 0.90779718185258162],
[0.82783799874762143, 0.88168214997516670, 0.91021327558158771],
[0.83461718711433397, 0.88617899207966144, 0.912698],
[0.84143400391267265, 0.89067784205972533, 0.91525234202431505],
[0.84828660859896876, 0.89517949187823220, 0.91787741675420809],
[0.855173, 0.89968474744000071, 0.92057420798187939],
[0.86209182250389604, 0.90419442997070587, 0.92334370089399287],
[0.86904074046491697, 0.90870937772496641, 0.92618685839305903],
[0.87601805253896004, 0.91323044810396214, 0.92910462402240312],
[0.88302187372559437, 0.91775852028916138, 0.93209792550477255],
[0.89005028788175211, 0.922294, 0.93516767908069365],
[0.89710133577649664, 0.92683931632133754, 0.93831479490472713],
[0.90417299998044809, 0.93139394162465017, 0.94154018386403615],
[0.91126318550326657, 0.93595938371885756, 0.94484476634389469],
[0.91836969459456230, 0.94053670204492512, 0.94822948371246796],
[0.92549019333850180, 0.94512701800126153, 0.95169531369138050],
[0.932622, 0.94973153093607443, 0.95524329142681930],
[0.93976285405407323, 0.95435154038484138, 0.95887453918361432],
[0.94690916199700992, 0.95898847793281272, 0.96259030956483305],
[0.95405752684263845, 0.963644, 0.966392],
[0.96120370638095498, 0.96831983443536507, 0.97028151093551396],
[0.96834243214841098, 0.97301835639562262, 0.97426091156847983],
[0.97546678696696387, 0.97774235120337327, 0.97833326722465574],
[0.98256696041465175, 0.98249567353568945, 0.98250303284453644],
[0.98962731050645314, 0.98728421705615543, 0.98677766165310821],
[0.99661705109721776, 0.99211911369325512, 0.99117263797041988],
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
