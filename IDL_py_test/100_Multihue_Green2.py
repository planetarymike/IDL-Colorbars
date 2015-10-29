from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.000019872508023912684, 0.000019586801788918958, 0.000019529289536969018],
[0.00040414202080346878, 0.00031685300497793627, 0.000337636],
[0.0012180805416863209, 0.00088433, 0.00096262835880248619],
[0.0024470485926491761, 0.0016778219494240462, 0.0018529028008505235],
[0.0040915072385109569, 0.0026725011731048285, 0.0029839452558377737],
[0.0061566834660047249, 0.0038509780335011195, 0.0043370840964282774],
[0.00865003, 0.0051998607002723719, 0.0058964280997749587],
[0.011580237713328405, 0.00670827, 0.0076475979375033335],
[0.014956682755055357, 0.0083670550766274093, 0.0095770944309065652],
[0.018789188665852417, 0.010168355257441712, 0.011671949793359906],
[0.023087819525899538, 0.012105297274040005, 0.013919523417888149],
[0.0278628, 0.014171811742864403, 0.016307379008853616],
[0.033124223908550125, 0.016362498267933699, 0.018823210907275206],
[0.038882382965477053, 0.018672529604655590, 0.0214548],
[0.044920905215348007, 0.021097580979276533, 0.024190001810827717],
[0.050920570235993855, 0.023633776885810556, 0.027016721133004028],
[0.056894, 0.026277650373542172, 0.0299229],
[0.062844524373854571, 0.029026111474785666, 0.032896690426775350],
[0.068774913512198665, 0.0318764, 0.035926130423450199],
[0.0746874, 0.034826178255492571, 0.038999506473206852],
[0.080583806807637298, 0.037873290906454395, 0.042058369685392609],
[0.086465604714313082, 0.041004190062793967, 0.044998754016794727],
[0.092333966249540683, 0.044091145326440019, 0.047831324233731869],
[0.0981898, 0.047132131697109038, 0.050557424892487233],
[0.10403382861063709, 0.050130380897910006, 0.053178239225583825],
[0.10986653262954243, 0.053088928589924554, 0.055694820959721454],
[0.11568826010104141, 0.056010641846897379, 0.058108120708168919],
[0.12149920433046860, 0.0588982, 0.060419007989567099],
[0.12729942970566882, 0.061754324034522308, 0.062628289682692268],
[0.133089, 0.064581372278674554, 0.064736725546769042],
[0.13886742328446053, 0.067381774480854389, 0.066745041301807084],
[0.14463479839405902, 0.070157833136446079, 0.068653939660909158],
[0.150391, 0.072911775341199719, 0.070464109627948385],
[0.156135, 0.075645761132561218, 0.072176234313301474],
[0.16186636875676558, 0.078361890586300997, 0.073790997473002273],
[0.16758517727675989, 0.081062209850766342, 0.075309088939524787],
[0.17329055190167122, 0.083748716269036849, 0.076731209083016200],
[0.17898187154374998, 0.086423362713671348, 0.078058072418402152],
[0.184658, 0.089088061238165206, 0.079290410455048699],
[0.19031964819743749, 0.091744686132634201, 0.080428973870557585],
[0.19596466164352611, 0.094395076457771176, 0.081474534078037702],
[0.201593, 0.097041038120145057, 0.0824279],
[0.20720308224905520, 0.0996843, 0.083289839823614709],
[0.212795, 0.10232674297887304, 0.0840612],
[0.21836722359935146, 0.10496994550598782, 0.0847429],
[0.22391929806367455, 0.10761563974200566, 0.085335826364805134],
[0.22945019143093870, 0.11026548430882452, 0.085840797774052707],
[0.23495899366031298, 0.112921, 0.0862588],
[0.24044477907657952, 0.11558412020369133, 0.086590694853538236],
[0.24590660806472248, 0.11825609002251985, 0.0868375],
[0.25134352864395343, 0.12093856674712072, 0.087000186936075335],
[0.25675457793309869, 0.12363306906684773, 0.087079700547219752],
[0.26213878351787712, 0.126341, 0.087077035120224550],
[0.26749516472940421, 0.12906407935193065, 0.086993179532959430],
[0.27282273384222783, 0.13180347683524662, 0.0868291],
[0.27812049719931886, 0.13456067746118275, 0.086585859647968333],
[0.283387, 0.13733704762147328, 0.086264369425020027],
[0.28862260865159822, 0.14013392083039403, 0.0858656],
[0.29382494900591283, 0.142953, 0.085390606053470458],
[0.29899346995937198, 0.14579434061955499, 0.084840245215532600],
[0.30412716294748210, 0.14866038162269049, 0.084215475763414399],
[0.30922501902209315, 0.15155191266474066, 0.083517201576017053],
[0.31428602962054081, 0.15447008910754168, 0.082746297990036938],
[0.31930918730093549, 0.15741602794789236, 0.081903607342489498],
[0.32429348644694506, 0.16039080695538432, 0.080989934370097966],
[0.32923792394522189, 0.16339546384741710, 0.080006041459889821],
[0.33414149983845959, 0.16643099550814575, 0.078952643742313339],
[0.33900321795691624, 0.16949835725739673, 0.077830404014645166],
[0.34382208653112989, 0.17259846217486052, 0.076639927478309472],
[0.34859711878844057, 0.17573218048414374, 0.075381756268806971],
[0.35332733353586238, 0.17890033900053881, 0.074056363751098003],
[0.35801175573177996, 0.182104, 0.072664148546236318],
[0.36264941704888415, 0.18534306403129477, 0.0712054],
[0.36723935643073713, 0.18861906311445709, 0.069680432766421302],
[0.37178062064430822, 0.19193236692430188, 0.068089297262695331],
[0.376272, 0.19528357936173490, 0.066432054543857949],
[0.38071335305724613, 0.19867325907129063, 0.064708626866826630],
[0.38510295887069712, 0.20210191938459360, 0.062918816996666071],
[0.38944016585815749, 0.20557002833409904, 0.061062298373593581],
[0.39372406821375605, 0.20907800873531529, 0.059138604192876705],
[0.39795377131600018, 0.21262623833527017, 0.057147115153416299],
[0.40212839231729775, 0.21621505002458197, 0.055087045566388403],
[0.40624706074815598, 0.21984473211014027, 0.052957427431272429],
[0.41030891913844503, 0.22351552864510660, 0.050757091975754280],
[0.41431312365816325, 0.22722763981268834, 0.048484648008324492],
[0.41825884478014325, 0.23098122235994584, 0.046138456233329218],
[0.42214526796717489, 0.23477639007773576, 0.043716598406667272],
[0.42597159438605786, 0.238613, 0.041216839834830189],
[0.42973704165108939, 0.24249172457787643, 0.038630110411253915],
[0.43344084459956883, 0.24641190904597182, 0.036044954669519159],
[0.43708225610186319, 0.25037371527439894, 0.033484306717240495],
[0.44066054790865083, 0.25437705080495893, 0.030953692193014568],
[0.44417501153794542, 0.25842178384617637, 0.028458763369723458],
[0.44762495920453743, 0.26250774396391713, 0.026005318607446901],
[0.45100972479447016, 0.26663472278680250, 0.023599322987596431],
[0.45432866488721718, 0.27080247472301849, 0.021246930090199002],
[0.45758115982817588, 0.27501071768535501, 0.018954504874898581],
[0.46076661485412546, 0.27925913382150330, 0.016728647624808829],
[0.46388446127425437, 0.28354737024692350, 0.014576218910767026],
[0.46693415770934960, 0.287875, 0.012504365531788348],
[0.46991519139170851, 0.292242, 0.010520547385515023],
[0.472827, 0.29664696230617016, 0.0086325652201805839],
[0.47566937072946008, 0.30109027599654486, 0.0068485892170128760],
[0.478442, 0.30557114561403259, 0.0051771883490276749],
[0.48114352283640333, 0.31008902334026600, 0.0036273604588036219],
[0.483775, 0.314643, 0.0022085629940401703],
[0.48633472332371846, 0.31923346252605944, 0.00093074433543746692],
[0.48882346690914030, 0.323859, -0.00019562435326908253],
[0.49124065356579821, 0.32851862329946607, -0.0011595168285202138],
[0.49358609772870782, 0.33321229813195380, -0.0019493191044679559],
[0.49585965929557258, 0.33793908789118626, -0.0025527965121272499],
[0.49806124574016858, 0.34269824887560796, -0.0029570605740912655],
[0.50019081430920520, 0.34748901200966859, -0.0031485357958958050],
[0.50224837430326352, 0.35231058347425298, -0.0031129264826776589],
[0.50423398944211617, 0.35716214533257140, -0.0028351836977340010],
[0.50614778031434893, 0.36204285615302179, -0.0022994724878928115],
[0.50798992691080258, 0.36695185163069599, -0.0014891395092150425],
[0.50976067124091373, 0.37188824520933644, -0.00038668119539023046],
[0.51146032003053710, 0.37685112870567694, 0.0010262873798147110],
[0.51308924749927520, 0.38183957293820736, 0.0027690627855936427],
[0.51464789821476498, 0.38685262836248424, 0.0048618824931034319],
[0.51613679002070523, 0.391889, 0.0073259529319097362],
[0.51755651703468697, 0.39694867666918138, 0.010183476156562513],
[0.51890775271112488, 0.40202967450184235, 0.0134577],
[0.52019125296371849, 0.40713129477899984, 0.017172816002756122],
[0.52140785934096734, 0.41225249605675285, 0.021354231428218524],
[0.52255850224724965, 0.41739222060348635, 0.026028337609800983],
[0.52364420420091629, 0.42254939514431405, 0.0312227],
[0.52466608311965435, 0.42772293163017716, 0.036965806762951518],
[0.52562535562216894, 0.432912, 0.043184826047674700],
[0.52652334033385140, 0.43811466917394931, 0.049452956061950486],
[0.52736146118271843, 0.44333062757179048, 0.055748186266650936],
[0.52814125067033846, 0.44855846433808383, 0.062078378001161331],
[0.52886435310090540, 0.45379703009600708, 0.068449986619134068],
[0.52953252774987936, 0.45904516593929529, 0.074868380377553861],
[0.53014765195185420, 0.46430170442770241, 0.081338067767023597],
[0.53071172408545897, 0.46956547062089765, 0.087862862939652286],
[0.53122686643114025, 0.47483528315181239, 0.094446008272951548],
[0.53169532787571339, 0.48010995534024231, 0.10109026662443593],
[0.53211948643549922, 0.48538829634730202, 0.10779799175512919],
[0.53250185156783503, 0.49066911237108540, 0.11457118277006129],
[0.53284506623863215, 0.49595120788365804, 0.12141152668735730],
[0.53315190871162066, 0.50123338690925467, 0.12832043207699281],
[0.533425, 0.50651445434329279, 0.13529905590632199],
[0.53366827510251225, 0.511793, 0.14234832516785473],
[0.53388404350285124, 0.517068, 0.14946895446614514],
[0.53407592969230500, 0.52233907793424150, 0.15666146045375196],
[0.53424740287083172, 0.52760381376653198, 0.163926],
[0.53440207026327369, 0.53286152446957258, 0.171263],
[0.53454367584529883, 0.53811105003403104, 0.17867267387851243],
[0.53467609845654063, 0.54335124160804649, 0.18615427486625474],
[0.53480334925557682, 0.54858096309589777, 0.193708],
[0.53492956847208595, 0.553799, 0.20133255005995243],
[0.53505902141281181, 0.55900452497376829, 0.20902813066189147],
[0.53519609367998944, 0.56419617166974234, 0.21679370990224595],
[0.53534528556373107, 0.569373, 0.22462839601654450],
[0.53551120557351906, 0.57453385508141685, 0.23253116664875090],
[0.53569856307860053, 0.57967781938341589, 0.24050087263609476],
[0.535912, 0.58480385675363211, 0.24853624168015998],
[0.53615688176502096, 0.58991099294787441, 0.25663588195448406],
[0.53643768682740123, 0.59499828154990586, 0.26479828569011926],
[0.53675959589592381, 0.60006480564599007, 0.27302183277327408],
[0.537128, 0.60510967948196404, 0.28130479438296774],
[0.53754704624577509, 0.61013205009762295, 0.28964533669138537],
[0.53802282662085032, 0.61513109893309559, 0.29804152464512213],
[0.53856016066302315, 0.62010604340182651, 0.30649132584160654],
[0.53916418130967392, 0.62505613842473884, 0.31499261451160793],
[0.53983999844123542, 0.62998067792013279, 0.32354317561575169],
[0.54059268205419708, 0.63487899624389832, 0.33214070906031568],
[0.54142724489604666, 0.63975046957466586, 0.34078283403524429],
[0.54234862467238287, 0.64459451723859340, 0.34946709347519839],
[0.54336166594901702, 0.64941060296859021, 0.35819095864256134],
[0.54447110188339221, 0.65419823609294125, 0.36695183382961732],
[0.54568153592989588, 0.65895697264843223, 0.37574706117554785],
[0.54699742367210913, 0.66368641641330806, 0.38457392559250347],
[0.54842305494152055, 0.668386, 0.39342965979372124],
[0.54996253638643799, 0.673056, 0.40231144941550889],
[0.55161977465646428, 0.67769576415802502, 0.41121643822388393],
[0.55339846036679796, 0.68230506067178465, 0.42014173339572353],
[0.55530205300264246, 0.68688382941174642, 0.429084],
[0.55733376691716008, 0.69143197728190719, 0.43804152071163566],
[0.55949655856661207, 0.69594946357613419, 0.44701009261300234],
[0.56179311511379948, 0.700436, 0.45598714129134071],
[0.56422584451585567, 0.70489255199293543, 0.46496967199772005],
[0.56679686719498012, 0.70931833641804420, 0.47395468598660045],
[0.56950800937150225, 0.71371382383785276, 0.48293918597793012],
[0.57236079811773222, 0.718079, 0.49192018159123224],
[0.57535645816920444, 0.72241485156072549, 0.50089469473760950],
[0.57849591050753857, 0.726721, 0.50985976495562890],
[0.58177977270655989, 0.730998, 0.51881245467713666],
[0.58520836101138474, 0.73524642812184482, 0.52774985440926647],
[0.58878169409903181, 0.73946662793134144, 0.53666908781915068],
[0.592499, 0.74365917104328438, 0.54556731670821390],
[0.59636121523808860, 0.74782463408248268, 0.55444174586332828],
[0.60036600864467504, 0.75196364090080048, 0.56328962777261737],
[0.60451277546080873, 0.75607686145643760, 0.57210826719424179],
[0.60880015586628911, 0.76016501060407127, 0.58089502556711237],
[0.613227, 0.76422884680034753, 0.58964732525316044],
[0.61779010684308444, 0.76826917072954826, 0.59836265360151697],
[0.62248878528547413, 0.77228682385458092, 0.60703856682570168],
[0.62732032053403675, 0.77628268689873736, 0.61567269368576893],
[0.63228226241269092, 0.78025767826393777, 0.62426273896816420],
[0.63737198539656503, 0.78421275239139365, 0.63280648675694939],
[0.64258670358393677, 0.78814889807088140, 0.64130180349092314],
[0.64792348571548464, 0.79206713670493867, 0.64974664080211031],
[0.65337927012136665, 0.79596852053451161, 0.65813903813198382],
[0.65895087948641662, 0.79985413083265677, 0.66647712512274537],
[0.66463503533382562, 0.80372507607303467, 0.67475912378190783],
[0.67042837213836792, 0.80758249007998628, 0.68298335041936409],
[0.67632745099106484, 0.81142753016704761, 0.69114821735703780],
[0.68232877274793602, 0.81526137527077258, 0.699252],
[0.68842879060599227, 0.81908522408676088, 0.70729401015585036],
[0.69462392205974421, 0.82290029321477331, 0.715272],
[0.70091056020102038, 0.82670781531980497, 0.72318577176814602],
[0.70728508433372406, 0.83050903731597991, 0.73103347679631569],
[0.71374386988331029, 0.83430521858008799, 0.738814],
[0.72028329758794563, 0.83809762920160469, 0.74652759448840367],
[0.72689976196479700, 0.84188754827601098, 0.75417233616954327],
[0.73358967905030181, 0.84567626224827874, 0.76174792190506180],
[0.74034949341789302, 0.84946506331345106, 0.76925376996876793],
[0.74717568448030025, 0.85325524788136209, 0.77668939934049719],
[0.75406477208624323, 0.85704811511272694, 0.78405442900384337],
[0.76101332142314160, 0.86084496553411760, 0.79134857709228534],
[0.76801794723828709, 0.86464709973971754, 0.79857165989447065],
[0.77507531739077506, 0.86845581718831533, 0.80572359073004285],
[0.78218215574539052, 0.87227241510468723, 0.81280437870807232],
[0.78933524441729341, 0.87609818749554058, 0.81981412738085602],
[0.79653142537300448, 0.87993442429143676, 0.82675303330661976],
[0.80376760138821923, 0.88378241062783591, 0.83362138453550960],
[0.81104073635659468, 0.88764342628060244, 0.84041955903425825],
[0.81834785493511841, 0.89151874527421271, 0.84714802306605397],
[0.82568604150071623, 0.89540963568472087, 0.85380732954355920],
[0.83305243837853638, 0.89931735966454229, 0.860398],
[0.84044424328402367, 0.90324317372271534, 0.86692110482339257],
[0.84785870589671042, 0.90718832930315474, 0.873377],
[0.85529312345196817, 0.911154, 0.87976697887241029],
[0.86274483519433109, 0.91514165148704052, 0.88609170974566020],
[0.87021121547834246, 0.91915230623400246, 0.89235233005499903],
[0.87768966522320935, 0.92318728316570031, 0.89854995571402119],
[0.88517760131592982, 0.92724783239777420, 0.90468577815900941],
[0.892672, 0.93133521329759872, 0.91076106380184640],
[0.900172, 0.935451, 0.91677715389500403],
[0.90767243353921290, 0.93959558983819269, 0.92273546493398340],
[0.91517226051894651, 0.94377121149276710, 0.92863748976718497],
[0.92266828770819709, 0.94797894029870433, 0.93448479964985942],
[0.93015757710602342, 0.95222021581152838, 0.940279],
[0.937637, 0.95649656795912030, 0.94602197342752870],
[0.945103, 0.96080965458702183, 0.95171541160077899],
[0.95255178028525911, 0.96516131773805791, 0.95736130253511209],
[0.95997866074069649, 0.96955367194799724, 0.96296171005461029],
[0.96737799930524326, 0.973989, 0.96851884842689329],
[0.97474241116679383, 0.97847127295100800, 0.974035],
[0.98206144291206787, 0.98300416909489485, 0.97951322600671620],
[0.98931839300953117, 0.98759484258827623, 0.98495625608429582],
[0.99648020273391580, 0.992257, 0.99036814101730941],
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
