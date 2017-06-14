from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.0000208612309326197836, 0.0000200048714121613121, 0.0000198463295491030259],
[0.000319508834810190408, 0.000357979457435837929, 0.000401326321662535826],
[0.000877122562749259880, 0.00103504791302306935, 0.00119880399555405089],
[0.00164111989408177662, 0.00201816744868143485, 0.00239038389515220957],
[0.00257879208746440020, 0.00329268032728375487, 0.00397040936718969124],
[0.00366504572325960501, 0.00485064095352544244, 0.00593809604563589385],
[0.00487877630041887687, 0.00668763620318043889, 0.00829473911627872165],
[0.00620128772800176194, 0.00880144447575751873, 0.0110425974297366052],
[0.00761546549691144523, 0.0111913463678014954, 0.0141843398607160113],
[0.00910529423452676422, 0.0138577247538695970, 0.0177227302164455584],
[0.0106555552111620051, 0.0168018125411493746, 0.0216604290967047294],
[0.0122516271011065946, 0.0200255233336328019, 0.0259998591799242250],
[0.0138793502803785628, 0.0235313320264691865, 0.0307431076465321702],
[0.0155249324242505687, 0.0273221871234917389, 0.0358918517460796102],
[0.0171748821746570933, 0.0314014440733770966, 0.0414235638349432847],
[0.0188159626121671419, 0.0357728130042306441, 0.0469779084203756567],
[0.0204351591564101535, 0.0404403165881978416, 0.0524781354037632611],
[0.0220196582772328384, 0.0451611383255774504, 0.0579269758611704391],
[0.0235568345098853618, 0.0498525994699354422, 0.0633265405381899238],
[0.0250342439922218996, 0.0545188045620980180, 0.0686784303159541642],
[0.0264396232275826912, 0.0591632495299170627, 0.0739838222270731705],
[0.0277608921102628289, 0.0637890268465511612, 0.0792435374596734132],
[0.0289861604837365165, 0.0683988837007208084, 0.0844580958762972678],
[0.0301037376679840832, 0.0729952689749654993, 0.0896277602901611181],
[0.0311021445123859652, 0.0775803715649148740, 0.0947525728603399176],
[0.0319701276185930874, 0.0821561519206755464, 0.0998323853518244819],
[0.0326966754428535747, 0.0867243682265746441, 0.104866884568858204],
[0.0332710360357801674, 0.0912865982989352342, 0.109855613954184639],
[0.0336827362139897612, 0.0958442580344713024, 0.114797992115721836],
[0.0339216019854985118, 0.100398617058157752, 0.119693328870828258],
[0.0339777800714937683, 0.104950812081197969, 0.124540839269765058],
[0.0338417603827943850, 0.109501858374569910, 0.129339655962450367],
[0.0335043993211109614, 0.114052659682841034, 0.134088840197860854],
[0.0329569437840802268, 0.118604016840290594, 0.138787391687630657],
[0.0321910557596567851, 0.123156635302340001, 0.143434257520263592],
[0.0311988374002883269, 0.127711131766614000, 0.148028340276862930],
[0.0299728564708650960, 0.132268040027184258, 0.152568505471111698],
[0.0285061720669665605, 0.136827816180906586, 0.157053588413732154],
[0.0267923605016946037, 0.141390843284882273, 0.161482400583550567],
[0.0248255412607024974, 0.145957435547916403, 0.165853735572641159],
[0.0226004029258489170, 0.150527842125654426, 0.170166374661094438],
[0.0201122289686185493, 0.155102250578215001, 0.174419092067191528],
[0.0173569233149533098, 0.159680790040152593, 0.178610659910728886],
[0.0143310355836834165, 0.164263534145109913, 0.182739852920611373],
[0.0110317859013060234, 0.168850503741261759, 0.186805452912317899],
[0.00745708919654903667, 0.173441669428389289, 0.190806253056274799],
[0.00360557887907410725, 0.178036953942971088, 0.194741061954346595],
[0., 0.182636234413894705, 0.198608707538467322],
[0., 0.187239344508161876, 0.202408040802763312],
[0., 0.191846076483183081, 0.206137939378290280],
[0., 0.196456183159872511, 0.209797310957639593],
[0., 0.201069379828682893, 0.213385096575118005],
[0., 0.205685346098921473, 0.216900273746916616],
[0., 0.210303727700124732, 0.220341859474623425],
[0., 0.214924138242892582, 0.223708913114565866],
[0., 0.219546160945384206, 0.227000539114772137],
[0., 0.224169350330619466, 0.230215889620789982],
[0., 0.228793233898793968, 0.233354166951172060],
[0., 0.233417313777995183, 0.236414625943125067],
[0., 0.238041068355985541, 0.239396576168603992],
[0., 0.242663953895064899, 0.242299384020995046],
[0., 0.247285406131473762, 0.245122474672480273],
[0., 0.251904841860289941, 0.247865333902176799],
[0., 0.256521660506333682, 0.250527509795209990],
[0., 0.261135245681220318, 0.253108614312999691],
[0., 0.265744966726359277, 0.255608324735178527],
[0., 0.270350180241405613, 0.258026384973773004],
[0., 0.274950231597437311, 0.260362606760487281],
[0., 0.279544456433902855, 0.262616870708184624],
[0., 0.284132182138226053, 0.264789127247929856],
[0., 0.288712729306795035, 0.266879397443244126],
[0., 0.293285413185967458, 0.268887773683517017],
[0., 0.297849545091620260, 0.270814420258837729],
[0., 0.302404433805720074, 0.272659573818800294],
[0., 0.306949386948355718, 0.274423543718173957],
[0., 0.311483712323646744, 0.276106712252615682],
[0., 0.316006719237954203, 0.277709534787922541],
[0., 0.320517719788838973, 0.279232539786607170],
[0., 0.325016030123240596, 0.280676328735874725],
[0., 0.329500971663422071, 0.282041575981333004],
[0., 0.333971872299264838, 0.283329028471043576],
[0., 0.338428067545594402, 0.284539505414737270],
[0., 0.342868901663301306, 0.285673897863244597],
[0., 0.347293728743102548, 0.286733168213376299],
[0., 0.351701913750920026, 0.287718349643661275],
[0., 0.356092833533933839, 0.288630545486481316],
[0., 0.360465877786507072, 0.289470928542263584],
[0., 0.364820449975280958, 0.290240740341461245],
[0., 0.369155968222875275, 0.290941290360109628],
[0., 0.373471866149744147, 0.291573955194761536],
[0., 0.377767593673866031, 0.292140177702576664],
[0., 0.382042617768075521, 0.292641466112300019],
[0., 0.386296423174961323, 0.293079393111756903],
[0., 0.390528513079382300, 0.293455594917369611],
[0., 0.394738409738775664, 0.293771770331027304],
[0., 0.398925655071542429, 0.294029679789426346],
[0., 0.403089811203909965, 0.294231144410742496],
[0., 0.407230460975784858, 0.294378045043198700],
[0., 0.411347208406202591, 0.294472321319749875],
[0., 0.415439679119089855, 0.294515970722708798],
[0., 0.419507520730136252, 0.294511047661704994],
[0., 0.423550403195665504, 0.294459662567891689],
[0., 0.427568019124472509, 0.294363981006758812],
[0., 0.431560084053663473, 0.294226222811353300],
[0., 0.435526336689604443, 0.294048661237061193],
[0., 0.439466539115139832, 0.293833622138420070],
[0., 0.443380476964292836, 0.293583483167715376],
[0., 0.447267959565707585, 0.293300672994313616],
[0., 0.451128820056124258, 0.292987670542875611],
[0., 0.454962915465211892, 0.292647004247707065],
[0., 0.458770126773102194, 0.292281251319596869],
[0., 0.462550358941993644, 0.291893037020537427],
[0., 0.466303540923183546, 0.291485033940730054],
[0., 0.470029625640915050, 0.291059961271266321],
[0., 0.473728589954399315, 0.290620584064837040],
[0., 0.477400434599373258, 0.290169712475772612],
[0., 0.481045184110542812, 0.289710200969667819],
[0., 0.484662886726224984, 0.289244947491802851],
[0., 0.488253614276491110, 0.288776892582559674],
[0., 0.491817462056073851, 0.288309018427057473],
[0., 0.495354548683264617, 0.287844347825321978],
[0., 0.498865015945992918, 0.287385943068459937],
[0.0163628535154387647, 0.502349028636228656, 0.286936904705589302],
[0.0465355441901433228, 0.505806774373803392, 0.286500370185664099],
[0.0711686411674427310, 0.509238463420693899, 0.286079512357880872],
[0.0912788184041140038, 0.512644328486762557, 0.285677537814091165],
[0.108848947155703507, 0.516024624527880116, 0.285297685056563555],
[0.124765631239398100, 0.519379628537310789, 0.284943222474634605],
[0.139511417062664261, 0.522709639331167430, 0.284617446114209638],
[0.153381071969768606, 0.526014977328687960, 0.284323677224821603],
[0.166569018271266217, 0.529295984328015834, 0.284065259569997286],
[0.179210728143080728, 0.532553023278103388, 0.283845556488083295],
[0.191404570666585810, 0.535786478047291626, 0.283667947692427425],
[0.203224301462149592, 0.538996753189048383, 0.283535825801937702],
[0.214726655935205568, 0.542184273705282438, 0.283452592595538899],
[0.225956197265774983, 0.545349484807588825, 0.283421654986924065],
[0.236948537737446119, 0.548492851676699700, 0.283446420719215497],
[0.247732551506896714, 0.551614859220366460, 0.283530293782748022],
[0.258331937888575614, 0.554716011829815225, 0.283676669563033834],
[0.268766352705087030, 0.557796833134867942, 0.283888929730124195],
[0.279052244316140896, 0.560857865757747653, 0.284170436884899735],
[0.289203482807088130, 0.563899671065532182, 0.284524528982284863],
[0.299231841210940264, 0.566922828921149757, 0.284954513555890410],
[0.309147368879113038, 0.569927937432764153, 0.285463661773022237],
[0.318958684916627100, 0.572915612701331733, 0.286055202353318716],
[0.328673211477530480, 0.575886488566060062, 0.286732315388314618],
[0.338297361197892554, 0.578841216347452225, 0.287498126102891272],
[0.347836689222881135, 0.581780464587557056, 0.288355698602784205],
[0.357296017593206061, 0.584704918787023020, 0.289308029654912091],
[0.366679537831719804, 0.587615281138486933, 0.290358042549206219],
[0.375990896174682066, 0.590512270255798000, 0.291508581091771413],
[0.385233264866339131, 0.593396620898548943, 0.292762403779498304],
[0.394409402172468948, 0.596269083691339130, 0.294122178205658891],
[0.403521703194959391, 0.599130424837172382, 0.295590475744484160],
[0.412572243133650429, 0.601981425824362870, 0.297169766560287207],
[0.421562814307569478, 0.604822883126306388, 0.298862414983345592],
[0.430494957989097926, 0.607655607893449079, 0.300670675290542311],
[0.439369991902973600, 0.610480425636770296, 0.302596687923807783],
[0.448189034083419535, 0.613298175902091902, 0.304642476173747179],
[0.456953023657113933, 0.616109711934526461, 0.306809943349637404],
[0.465662739019688632, 0.618915900332344338, 0.309100870450375931],
[0.474318813792942884, 0.621717620689585804, 0.311516914344094620],
[0.482921750885234091, 0.624515765226715480, 0.314059606457183782],
[0.491471934924748666, 0.627311238408636673, 0.316730351966575341],
[0.499969643292338006, 0.630104956549411677, 0.319530429482460021],
[0.508415055945361294, 0.632897847403032565, 0.322460991202290159],
[0.516808264194818956, 0.635690849739618868, 0.325523063511130140],
[0.525149278573946776, 0.638484912906447266, 0.328717547998225779],
[0.533438035916385611, 0.641280996373246759, 0.332045222855194944],
[0.541674405745217746, 0.644080069261225074, 0.335506744617555752],
[0.549858196060149074, 0.646883109855331484, 0.339102650208472356],
[0.557989158598156010, 0.649691105099303501, 0.342833359241571711],
[0.566066993632999838, 0.652505050073082904, 0.346699176538580900],
[0.574091354370373619, 0.655325947452250368, 0.350700294817174407],
[0.582061850988330076, 0.658154806949149629, 0.354836797504916590],
[0.589978054366316451, 0.660992644735457935, 0.359108661636351079],
[0.597839499540950836, 0.663840482845981628, 0.363515760792135212],
[0.605645688922015202, 0.666699348563539962, 0.368057868041500591],
[0.613396095298302635, 0.669570273784836800, 0.372734658852207856],
[0.621090164659450328, 0.672454294367290428, 0.377545713935396488],
[0.628727318857037032, 0.675352449456849802, 0.382490521996276256],
[0.636306958125620770, 0.678265780796877160, 0.387568482365335698],
[0.643828463482129410, 0.681195332018246891, 0.392778907488578799],
[0.651291199020115230, 0.684142147910876242, 0.398121025259185468],
[0.658694514113666085, 0.687107273676928365, 0.403593981176810945],
[0.666037745544216686, 0.690091754166036631, 0.409196840324480060],
[0.673320219562246636, 0.693096633092908254, 0.414928589156606631],
[0.680541253894644149, 0.696122952237753445, 0.420788137095051418],
[0.687700159707510750, 0.699171750630011357, 0.426774317933286407],
[0.694796243533206792, 0.702244063715916966, 0.432885891051617067],
[0.701828809169761314, 0.705340922510484747, 0.439121542449063429],
[0.708797159559871659, 0.708463352734520213, 0.445479885599809389],
[0.715700598656220932, 0.711612373937344222, 0.451959462144217172],
[0.722538433279205306, 0.714788998605898840, 0.458558742426159294],
[0.729309974972651487, 0.717994231260982607, 0.465276125889915904],
[0.736014541862661353, 0.721229067541365287, 0.472109941351127216],
[0.742651460524307749, 0.724494493276551244, 0.479058447157240386],
[0.749220067860552508, 0.727791483548997142, 0.486119831253644941],
[0.755719712997405368, 0.731121001746585897, 0.493292211172179307],
[0.762149759199067245, 0.734483998606177968, 0.500573633958993569],
[0.768509585806574025, 0.737881411249055041, 0.507962076058857792],
[0.774798590203176207, 0.741314162209079419, 0.515455443172923688],
[0.781016189809557448, 0.744783158454372929, 0.523051570106714547],
[0.787161824111778374, 0.748289290403323482, 0.530748220624722822],
[0.793234956724733764, 0.751833430935693880, 0.538543087327484349],
[0.799235077493797852, 0.755416434399586056, 0.546433791566327764],
[0.805161704637239017, 0.759039135614995808, 0.554417883410249113],
[0.811014386931970588, 0.762702348874641500, 0.562492841678486455],
[0.816792705945185715, 0.766406866942709319, 0.570656074051380746],
[0.822496278314448159, 0.770153460052116823, 0.578904917271058417],
[0.828124758078906509, 0.773942874900805822, 0.587236637442281939],
[0.833677839064417281, 0.777775833647537551, 0.595648430442571986],
[0.839155257325528203, 0.781653032907545842, 0.604137422449331218],
[0.844556793647559090, 0.785575142748319410, 0.612700670590246355],
[0.849882276112320034, 0.789542805685647053, 0.621335163721677963],
[0.855131582731427642, 0.793556635679938616, 0.630037823338048364],
[0.860304644151743458, 0.797617217132626788, 0.638805504613415898],
[0.865401446438075594, 0.801725103882289902, 0.647634997574454418],
[0.870422033939171280, 0.805880818199846138, 0.656523028401876818],
[0.875366512243983874, 0.810084849781902205, 0.665466260854983394],
[0.880235051236531896, 0.814337654740953987, 0.674461297811375648],
[0.885027888259143691, 0.818639654590705312, 0.683504682910946904],
[0.889745331395850103, 0.822991235224228457, 0.692592902289927648],
[0.894387762890018978, 0.827392745882019498, 0.701722386386991248],
[0.898955642713208602, 0.831844498106208197, 0.710889511799044471],
[0.903449512305899427, 0.836346764676137333, 0.720090603159232345],
[0.907869998515127730, 0.840899778519331176, 0.729321935003636290],
[0.912217817759746419, 0.845503731590263818, 0.738579733585953413],
[0.916493780460989504, 0.850158773707422544, 0.747860178590663782],
[0.920698795784868573, 0.854865011336712666, 0.757159404684484172],
[0.924833876754216577, 0.859622506306102929, 0.766473502832558551],
[0.928900145802490029, 0.864431274432494234, 0.775798521289055354],
[0.932898840860040823, 0.869291284036643241, 0.785130466150480100],
[0.936831322087574026, 0.874202454315382127, 0.794465301332403118],
[0.940699079403185423, 0.879164653531693263, 0.803798947794269414],
[0.944503740991277096, 0.884177696971704896, 0.813127281789137957],
[0.948247083037960459, 0.889241344602315964, 0.822446131851015450],
[0.951931041014153823, 0.894355298342281668, 0.831751274144861052],
[0.955557722933180753, 0.899519198830866951, 0.841038425683046875],
[0.959129425157798310, 0.904732621538000936, 0.850303234741110248],
[0.962648651542769795, 0.909995072002653838, 0.859541267560302691],
[0.966118137006508948, 0.915305979903065170, 0.868747990065014575],
[0.969540877082600727, 0.920664691539044622, 0.877918742784624784],
[0.972920165699665218, 0.926070460118584737, 0.887048706341578397],
[0.976259644533161830, 0.931522432946412127, 0.896132853558054388],
[0.979563369049570087, 0.937019634134795165, 0.905165882092528684],
[0.982835899358208587, 0.942560940653589308, 0.914142117879786609],
[0.986082429266641136, 0.948145048122050471, 0.923055373182046446],
[0.989308976762404257, 0.953770420116618944, 0.931898730928691910],
[0.992522678673151693, 0.959435209553202273, 0.940664202716677278],
[0.995732274402314377, 0.965137129464281762, 0.949342154955812645],
[0.998948964830594810, 0.970873223551239284, 0.957920269581724271],
[1.00000000000000000, 0.976639412226374071, 0.966381447125356785],
[1.00000000000000000, 0.982429433690877540, 0.974698815977057431],
[1.00000000000000000, 0.988231534670260259, 0.982819794172733352],
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
