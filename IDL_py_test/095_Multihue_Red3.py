from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.0000208612309326197836, 0.0000200048714121613121, 0.0000198463295491030259],
[0.000341189588910333519, 0.000363349802569965408, 0.000268974221116803039],
[0.000964717188578996087, 0.00105173906371254467, 0.000711985399957085945],
[0.00185447383113248178, 0.00204919121172640259, 0.00129674031372783104],
[0.00299414726293088752, 0.00333741328770951248, 0.00199107990494984703],
[0.00437575805925987955, 0.00490418098452247500, 0.00277120415932249941],
[0.00599607107542441190, 0.00674023289414132920, 0.00361803642008188880],
[0.00785502332414254878, 0.00883797996042106140, 0.00451559856684120506],
[0.00995488917051907257, 0.0111908524850026173, 0.00545014344791329690],
[0.0122997810183917578, 0.0137929282517230915, 0.00640963791956814400],
[0.0148953246755175756, 0.0166387032843847218, 0.00738343043107311716],
[0.0177484345021792153, 0.0197229423820877645, 0.00836202472088747907],
[0.0208671495615159221, 0.0230405776324620615, 0.00933691859805457248],
[0.0242605090407406708, 0.0265866374585379019, 0.0103004846550708417],
[0.0279384539974848779, 0.0303561960064511922, 0.0112458790523156868],
[0.0319117473323319231, 0.0343443366074497047, 0.0121669696794287751],
[0.0361919067144846479, 0.0385461252959211770, 0.0130582780284287866],
[0.0407845678358952288, 0.0428713327444620387, 0.0139149309709430420],
[0.0454492170594387804, 0.0471216792041443192, 0.0147326198144401548],
[0.0501259991774289995, 0.0513058522797550445, 0.0155075647896302342],
[0.0548191863364607332, 0.0554265307442313934, 0.0162364836464018412],
[0.0595325187945624015, 0.0594860385482654727, 0.0169165633991767428],
[0.0642692726876416265, 0.0634864027367383343, 0.0175454345194856372],
[0.0690323159051321467, 0.0674294003157854816, 0.0181211470585181736],
[0.0738241547260437003, 0.0713165965701088589, 0.0186421483176729234],
[0.0786469731810927330, 0.0751493766847808886, 0.0191072617854408343],
[0.0835026666177223209, 0.0789289720659687999, 0.0195156671342157743],
[0.0883928705910379808, 0.0826564824223975647, 0.0198668811276213331],
[0.0933189859443369074, 0.0863328944254035668, 0.0201607393324522606],
[0.0982822007504687845, 0.0899590975841970120, 0.0203973785627041722],
[0.103283509640931220, 0.0935358978367331340, 0.0205772200088570542],
[0.108323730940238228, 0.0970640292531068927, 0.0207009530253547680],
[0.113403521939487550, 0.100544164168951344, 0.0207695195644131449],
[0.118523392578544301, 0.103976922004812566, 0.0207840992558812367],
[0.123683717756113837, 0.107362876979390814, 0.0207460951416254674],
[0.128884748447662401, 0.110702564886686922, 0.0206571200793929759],
[0.134126621780135957, 0.113996489077023172, 0.0205189838357881966],
[0.139409370187735720, 0.117245125757892671, 0.0203336808912181338],
[0.144732929753282696, 0.120448928711240799, 0.0201033789817240405],
[0.150097147823760518, 0.123608333508118784, 0.0198304084037345084],
[0.155501789975710292, 0.126723761288879244, 0.0195172521081490684],
[0.160946546395588308, 0.129795622166614749, 0.0191665366099328278],
[0.166431037731504777, 0.132824318302900951, 0.0187810237387075890],
[0.171954820465558572, 0.135810246697760539, 0.0183636032547641881],
[0.177517391849988021, 0.138753801729788850, 0.0179172863535807456],
[0.183118194445302446, 0.141655377477393540, 0.0174452000803935470],
[0.188756620294308147, 0.144515369847889014, 0.0169505826746833010],
[0.194432014762307204, 0.147334178537626342, 0.0164367798626671620],
[0.200143680070644314, 0.150112208843310418, 0.0159072421140684754],
[0.205890878548096234, 0.152849873342066622, 0.0153655228776043221],
[0.211672835622277233, 0.155547593455590133, 0.0148152778078109240],
[0.217488742571209370, 0.158205800911789540, 0.0142602649940514557],
[0.223337759053421847, 0.160824939115665283, 0.0137043462008150114],
[0.229219015433389017, 0.163405464439698250, 0.0131514891267568209],
[0.235131614917710896, 0.165947847442746294, 0.0126057706883259471],
[0.241074635516219993, 0.168452574025305612, 0.0120713813322990103],
[0.247047131841085454, 0.170920146527985844, 0.0115526303800742580],
[0.253048136755983699, 0.173351084779147097, 0.0110539524051731508],
[0.259076662886542464, 0.175745927096820909, 0.0105799146440371510],
[0.265131704002409596, 0.178105231249316404, 0.0101352254388770643],
[0.271212236280619579, 0.180429575378216661, 0.00972474371002084170],
[0.277317219459218722, 0.182719558886867139, 0.00935348945388099137],
[0.283445597889546264, 0.184975803296873215, 0.00902665526131240549],
[0.289596301494974229, 0.187198953074597413, 0.00874961884972533938],
[0.295768246643441979, 0.189389676429141313, 0.00852795660082132472],
[0.301960336940630736, 0.191548666082832914, 0.00836745809421560530],
[0.308171463950206614, 0.193676640014789875, 0.00827414162546625392],
[0.314400507847174660, 0.195774342177713834, 0.00825427069509529140],
[0.320646338010013909, 0.197842543187664532, 0.00831437145306024306],
[0.326907813556946702, 0.199882040986178344, 0.00846125108076449181],
[0.333183783831363545, 0.201893661473737940, 0.00870201709004790082],
[0.339473088841171999, 0.203878259113232430, 0.00904409751565954899],
[0.345774559656547631, 0.205836717501728661, 0.00949526197443461249],
[0.352087018770329885, 0.207769949908539864, 0.0100636435607756921],
[0.358409280425093180, 0.209678899777271444, 0.0107577615440133650],
[0.364740150910682237, 0.211564541189244559, 0.0115865448288052109],
[0.371078428835833085, 0.213427879285405464, 0.0125593561348887502],
[0.377422905377309714, 0.215269950643573460, 0.0136860168472192796],
[0.383772364509797903, 0.217091823607653556, 0.0149768324817810116],
[0.390125583219671779, 0.218894598565194276, 0.0164426187061780839],
[0.396481331705571982, 0.220679408169490054, 0.0180947278474399668],
[0.402838373568604025, 0.222447417502239342, 0.0199450758123789970],
[0.409195465994841079, 0.224199824172625017, 0.0220061693382636904],
[0.415551359932681774, 0.225937858348554454, 0.0242911334835834297],
[0.421904800267507207, 0.227662782715705059, 0.0268137392602646463],
[0.428254525995969415, 0.229375892359960865, 0.0295884312999060151],
[0.434599270402141968, 0.231078514568800075, 0.0326303554374511515],
[0.440937761237663373, 0.232772008547209197, 0.0359553860862538641],
[0.447268720907926631, 0.234457765043746602, 0.0395801532687743915],
[0.453590866666257308, 0.236137205882488765, 0.0434061071189366723],
[0.459902910817969357, 0.237811783396725651, 0.0473259040128705052],
[0.466203560936090111, 0.239482979760473336, 0.0513461278964654419],
[0.472491520090480510, 0.241152306214109324, 0.0554646426759579855],
[0.478765487091995790, 0.242821302180747267, 0.0596796840717804602],
[0.485024156753288416, 0.244491534270297406, 0.0639898075411881318],
[0.491266220167752732, 0.246164595168588518, 0.0683938417608256632],
[0.497490365008086355, 0.247842102409376708, 0.0728908472528370099],
[0.503695275845854606, 0.249525697027580262, 0.0774800796745472586],
[0.509879634493399347, 0.251217042092665710, 0.0821609572778877750],
[0.516042120369370583, 0.252917821121717012, 0.0869330320608725504],
[0.522181410889105857, 0.254629736372402160, 0.0917959641662875747],
[0.528296181881028892, 0.256354507016769817, 0.0967494991237158597],
[0.534385108030180245, 0.258093867197553339, 0.101793447574688084],
[0.540446863349939077, 0.259849563969480390, 0.106927667163782325],
[0.546480121682953457, 0.261623355128877133, 0.112152046319059007],
[0.552483557232223088, 0.263417006935726283, 0.117466489682325287],
[0.558455845123249195, 0.265232291733176195, 0.122870904983030493],
[0.564395661998094544, 0.267070985470362621, 0.128365191179046628],
[0.570301686642155081, 0.268934865135260270, 0.133949227713398206],
[0.576172600644385580, 0.270825706105104480, 0.139622864758423337],
[0.582007089091666763, 0.272745279422737241, 0.145385914338263034],
[0.587803841297957930, 0.274695349007983258, 0.151238142237265033],
[0.593561551568803636, 0.276677668813882338, 0.157179260616230831],
[0.599278920001722781, 0.278693979938245406, 0.163208921270729723],
[0.604954653322942404, 0.280746007701574651, 0.169326709476194298],
[0.610587465760882742, 0.282835458702869080, 0.175532138373496044],
[0.616176079956734846, 0.284964017865240726, 0.181824643856338647],
[0.621719227912405748, 0.287133345483541968, 0.188203579928322567],
[0.627215651976055555, 0.289345074286393722, 0.194668214503073062],
[0.632664105865361703, 0.291600806525062484, 0.201217725625520483],
[0.638063355728591186, 0.293902111101586872, 0.207851198096401790],
[0.643412181243483983, 0.296250520748369162, 0.214567620485394461],
[0.648709376753869194, 0.298647529271168777, 0.221365882521121937],
[0.653953752443860337, 0.301094588867018009, 0.228244772848595567],
[0.659144135549398991, 0.303593107528049577, 0.235202977146612147],
[0.664279371606805946, 0.306144446541625648, 0.242239076599192804],
[0.669358325737941962, 0.308749918096403397, 0.249351546716412742],
[0.674379883971444327, 0.311410783003192804, 0.256538756500966525],
[0.679342954599441384, 0.314128248538562915, 0.263798967957546371],
[0.684246469569008031, 0.316903466418228308, 0.271130335942626921],
[0.689089385907542651, 0.319737530906241740, 0.278530908352580875],
[0.693870687181096568, 0.322631477065035643, 0.285998626648186316],
[0.698589384984600437, 0.325586279150291424, 0.293531326713575347],
[0.703244520462762868, 0.328602849153618537, 0.301126740047508168],
[0.707835165860316806, 0.331682035494994698, 0.308782495284568748],
[0.712360426100113186, 0.334824621865968786, 0.316496120043464280],
[0.716819440387439277, 0.338031326223658335, 0.324265043099092765],
[0.721211383838773812, 0.341302799934733780, 0.332086596874432816],
[0.725535469133013033, 0.344639627067769017, 0.339958020247599635],
[0.729790948183067556, 0.348042323831598832, 0.347876461668648995],
[0.733977113825518557, 0.351511338156700215, 0.355838982579856911],
[0.738093301525866718, 0.355047049416051364, 0.363842561132313502],
[0.742138891096714715, 0.358649768281478265, 0.371884096190720048],
[0.746113308426022304, 0.362319736711117724, 0.379960411617304594],
[0.750016027212399905, 0.366057128063379866, 0.388068260824755040],
[0.753846570704190699, 0.369862047332587818, 0.396204331587058200],
[0.757604513438889460, 0.373734531501406730, 0.404365251096089950],
[0.761289482979266019, 0.377674550005132115, 0.412547591250784384],
[0.764901161642327465, 0.381682005302991678, 0.420747874164696056],
[0.768439288217070304, 0.385756733551715136, 0.428962577876770834],
[0.771903659666769881, 0.389898505376813531, 0.437188142249195499],
[0.775294132811352621, 0.394107026737217814, 0.445420975035273059],
[0.778610625985198368, 0.398381939879191183, 0.453657458099414879],
[0.781853120665556234, 0.402722824375675137, 0.461893953770529608],
[0.785021663066532427, 0.407129198247551949, 0.470126811309368786],
[0.788116365693498189, 0.411600519163553780, 0.478352373469724312],
[0.791137408852543689, 0.416136185715856422, 0.486566983132812048],
[0.794085042109506367, 0.420735538768644279, 0.494766989993683681],
[0.796959585692933237, 0.425397862877175126, 0.502948757278151026],
[0.799761431835242842, 0.430122387775093817, 0.511108668468406302],
[0.802491046046240553, 0.434908289927890823, 0.519243134015371810],
[0.805148968313047608, 0.439754694150581826, 0.527348598015741743],
[0.807735814220471027, 0.444660675287729845, 0.535421544831742313],
[0.810252275985780757, 0.449625259954002321, 0.543458505631799538],
[0.812699123401823487, 0.454647428333481984, 0.551456064830599946],
[0.815077204682473244, 0.459726116035846844, 0.559410866407418106],
[0.817387447204361628, 0.464860216007532523, 0.567319620082116116],
[0.819630858138963747, 0.470048580495795620, 0.575179107328825712],
[0.821808524969161791, 0.475290023063482503, 0.582986187208078710],
[0.823921615884520286, 0.480583320652098245, 0.590737801998972301],
[0.825971380049654314, 0.485927215690561687, 0.598430982613895268],
[0.827959147740240153, 0.491320418246768809, 0.606062853779367083],
[0.829886330341402689, 0.496761608218859119, 0.613630638967649356],
[0.831754420203451805, 0.502249437562788392, 0.621131665064978744],
[0.833564990350178836, 0.507782532552540022, 0.628563366763515652],
[0.835319694035215332, 0.513359496069037191, 0.635923290665428187],
[0.837020264142258608, 0.518978909913547892, 0.643209099088883240],
[0.838668512425305601, 0.524639337141120876, 0.650418573567126401],
[0.840266328585423938, 0.530339324409337065, 0.657549618033263172],
[0.841815679180926812, 0.536077404337462648, 0.664600261684806681],
[0.843318606368310131, 0.541852097870878402, 0.671568661523523458],
[0.844777226471676301, 0.547661916645513336, 0.678453104567576126],
[0.846193728378913268, 0.553505365346842360, 0.685252009734403589],
[0.847570371763327501, 0.559380944057969010, 0.691963929394240340],
[0.848909485129990982, 0.565287150591182064, 0.698587550595560325],
[0.850213463686579018, 0.571222482797407172, 0.705121695965116424],
[0.851484767039049961, 0.577185440847956532, 0.711565324286577705],
[0.852725916713093279, 0.583174529483043602, 0.717917530763030110],
[0.853939493502882563, 0.589188260221615745, 0.724177546969845043],
[0.855128134649283389, 0.595225153527177642, 0.730344740505544543],
[0.856294530850330471, 0.601283740924463128, 0.736418614349414025],
[0.857441423107398126, 0.607362567061969449, 0.742398805935580497],
[0.858571599411210862, 0.613460191715631154, 0.748285085954245699],
[0.859687891272481242, 0.619575191729149988, 0.754077356891584727],
[0.860793170102700178, 0.625706162886759842, 0.759775651320605538],
[0.861890343451255481, 0.631851721714551395, 0.765380129955947175],
[0.862982351105797241, 0.638010507206757227, 0.770891079486185959],
[0.864072161063482946, 0.644181182473767544, 0.776308910197745505],
[0.865162765381427556, 0.650362436308983827, 0.781634153404936694],
[0.866257175915389199, 0.656552984671978868, 0.786867458701004718],
[0.867358419956445248, 0.662751572085808594, 0.792009591045337302],
[0.868469535776065338, 0.668956972946671668, 0.797061427702192016],
[0.869593568090699986, 0.675167992744490686, 0.802023955046426096],
[0.870733563457597226, 0.681383469193362234, 0.806898265251783653],
[0.871892565614231119, 0.687602273271156528, 0.811685552877295935],
[0.873073610774296238, 0.693823310167915208, 0.816387111367301022],
[0.874279722893744671, 0.700045520143020905, 0.821004329480498507],
[0.875513908920886430, 0.706267879291440637, 0.825538687663315729],
[0.876779154045005726, 0.712489400219627811, 0.829991754382694236],
[0.878078416958342434, 0.718709132631987102, 0.834365182433206898],
[0.879414625146626716, 0.724926163829019532, 0.838660705233230774],
[0.880790670223608463, 0.731139619118556960, 0.842880133124665698],
[0.882209403325233898, 0.737348662141660838, 0.847025349690510576],
[0.883673630579213332, 0.743552495114979006, 0.851098308104411894],
[0.885186108665755311, 0.749750358991498334, 0.855101027526168234],
[0.886749540485219700, 0.755941533541748201, 0.859035589557065715],
[0.888366570948227463, 0.762125337357625665, 0.862904134768906150],
[0.890039782903611632, 0.768301127781052084, 0.866708859320644898],
[0.891771693219231887, 0.774468300759690309, 0.870452011676747683],
[0.893564749030239747, 0.780626290631938446, 0.874135889441687741],
[0.895421324168984567, 0.786774569843340932, 0.877762836325529872],
[0.897343715790087759, 0.792912648596425074, 0.881335239256273439],
[0.899334141203657067, 0.799040074435812930, 0.884855525655643072],
[0.901394734928904651, 0.805156431770179037, 0.888326160896388717],
[0.903527545979753821, 0.811261341332308761, 0.891749645960949744],
[0.905734535393263207, 0.817354459578078618, 0.895128515323688867],
[0.908017574011030115, 0.823435478024618028, 0.898465335081940042],
[0.910378440523078480, 0.829504122527227161, 0.901762701365006025],
[0.912818819783181579, 0.835560152493718955, 0.905023239055276818],
[0.915340301404238055, 0.841603360033745918, 0.908249600862082729],
[0.917944378642131187, 0.847633569039211832, 0.911444466797210473],
[0.920632447576798629, 0.853650634190029067, 0.914610544111791102],
[0.923405806599944645, 0.859654439877093779, 0.917750567768253700],
[0.926265656220269906, 0.865644899031203896, 0.920867301539422201],
[0.929213099199623693, 0.871621951842531217, 0.923963539851085591],
[0.932249141037307161, 0.877585564349693592, 0.927042110516764217],
[0.935374690825716670, 0.883535726870025240, 0.930105878557083598],
[0.938590562509363013, 0.889472452232312638, 0.933157751355878307],
[0.941897476592507554, 0.895395773758921432, 0.936200685487871942],
[0.945296062360195699, 0.901305742923869002, 0.939237695669214112],
[0.948786860706888890, 0.907202426583959887, 0.942271866448931572],
[0.952370327711505538, 0.913085903636677632, 0.945306367503011669],
[0.956046839166505458, 0.918956260893049937, 0.948344473756767337],
[0.959816696377366108, 0.924813587852335694, 0.951389592118530802],
[0.963680133724855836, 0.930657969903921911, 0.954445297486270605],
[0.967637328776702943, 0.936489479215996234, 0.957515382119716540],
[0.971688416245772291, 0.942308162115637837, 0.960603924892405314],
[0.975833508017508566, 0.948114020950668102, 0.963715391225763995],
[0.980072723240198562, 0.953906986884912711, 0.966854782519078859],
[0.984406236088839814, 0.959686876972909553, 0.970027869878035687],
[0.988834356835471051, 0.965453322052746921, 0.973241581594613714],
[0.993357681656196090, 0.971205635389277622, 0.976504697386795795],
[0.997977403120007156, 0.976942545137774121, 0.979829235416136091],
[1.00000000000000000, 0.982661549855001870, 0.983233722751823192],
[1.00000000000000000, 0.988356830194641156, 0.986753542240176640],
[1.00000000000000000, 0.994000868618791888, 0.990528868543822605]]

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
