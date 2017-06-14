from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.0000208612309326197836, 0.0000200048714121613121, 0.0000198463295491030259],
[0.000329732983032901886, 0.000355235180310873027, 0.000388911410982505329],
[0.000918775406588910148, 0.00102323430198466019, 0.00115405162394373187],
[0.00174368070660850375, 0.00198770266358338707, 0.00229306748798694272],
[0.00278067343093749142, 0.00323034189004337046, 0.00380119695094466607],
[0.00401417519247438282, 0.00473922407970798348, 0.00567963469784484032],
[0.00543317204376583471, 0.00650562801309073797, 0.00793261012334524340],
[0.00702962385510816270, 0.00852271014021447476, 0.0105661955013635050],
[0.00879762502186139279, 0.0107848250433358814, 0.0135877063222019437],
[0.0107329085562938749, 0.0132871339455447896, 0.0170053572874215471],
[0.0128325296678132878, 0.0160253600311404641, 0.0208280454503838447],
[0.0150946522821663702, 0.0189956261655418977, 0.0250652029866779563],
[0.0175183987677833761, 0.0221943422937620066, 0.0297266908429331261],
[0.0201037405559185145, 0.0256181245059907033, 0.0348227176571584557],
[0.0228514163288265661, 0.0292637352174838356, 0.0403637749180660241],
[0.0257628694137682669, 0.0331280379628716357, 0.0460311078783999031],
[0.0288401989164425512, 0.0372079626336716332, 0.0516775247282575609],
[0.0320861208952326685, 0.0414750928428656226, 0.0573086569264572229],
[0.0355039369988242384, 0.0457052923000242431, 0.0629281081799430708],
[0.0390975087243544683, 0.0498785035804000035, 0.0685389325689035322],
[0.0427902554608530702, 0.0539976578340349497, 0.0741437220966918165],
[0.0464561304671903749, 0.0580653127175978292, 0.0797446756495651943],
[0.0501091856896255170, 0.0620837110496457664, 0.0853436539989965159],
[0.0537536563756343885, 0.0660548283425705374, 0.0909422241719952673],
[0.0573934780144496268, 0.0699804117307193940, 0.0965416956168641816],
[0.0610323186497856926, 0.0738620121642118432, 0.102143149963402707],
[0.0646736054097632740, 0.0777010112746268633, 0.107747465729355812],
[0.0683205464346897939, 0.0814986439833756959, 0.113355339001745020],
[0.0719761491172948298, 0.0852560176774419254, 0.118967300884915028],
[0.0756432353712715166, 0.0889741285942285409, 0.124583732331372099],
[0.0793244544937395102, 0.0926538759196480766, 0.130204876839481426],
[0.0830222940722931957, 0.0962960739989882353, 0.135830851401870789],
[0.0867390892984486739, 0.0999014629797347897, 0.141461656011503151],
[0.0904770309798534900, 0.103470718143264501, 0.147097181972861646],
[0.0942381724888582406, 0.107004458133612285, 0.152737219219182929],
[0.0980244358414727734, 0.110503252253120826, 0.158381462800048778],
[0.101837617065714897, 0.113967626964278618, 0.164029518674565250],
[0.105679390990067457, 0.117398071712635471, 0.169680908922094725],
[0.109551315559682949, 0.120795044166024934, 0.175335076463777495],
[0.113454835769057377, 0.124158974949368922, 0.180991389372875344],
[0.117391287284295293, 0.127490271941337163, 0.186649144839574038],
[0.121361899815149277, 0.130789324188460759, 0.192307572845688390],
[0.125367800286261960, 0.134056505483490518, 0.197965839596292159],
[0.129410015848052812, 0.137292177647499902, 0.203623050748292456],
[0.133489476760167203, 0.140496693549147483, 0.209278254470112723],
[0.137607019174125628, 0.143670399889425593, 0.214930444361717599],
[0.141763387836515792, 0.146813639775949800, 0.220578562260043243],
[0.145959238729669039, 0.149926755107232940, 0.226221500951347743],
[0.150195141663060500, 0.153010088784334475, 0.231858106808956632],
[0.154471582825596587, 0.156063986764687329, 0.237487182372258354],
[0.158788967306396217, 0.159088799970686895, 0.243107488880544398],
[0.163147621589578740, 0.162084886063748851, 0.248717748773306990],
[0.167547796026819601, 0.165052611092924323, 0.254316648166882875],
[0.171989667290041004, 0.167992351025786413, 0.259902839315804102],
[0.176473340805481965, 0.170904493168110377, 0.265474943065869717],
[0.180998853169479917, 0.173789437477862074, 0.271031551304747098],
[0.185566174545610058, 0.176647597778140847, 0.276571229414835973],
[0.190175211042292375, 0.179479402872978311, 0.282092518732163788],
[0.194825807069572754, 0.182285297569271865, 0.287593939014199940],
[0.199517747673533141, 0.185065743607587735, 0.293073990918690852],
[0.204250760846568624, 0.187821220504130054, 0.298531158494891979],
[0.209024519811701059, 0.190552226305791439, 0.303963911687914368],
[0.213838645279021688, 0.193259278259902606, 0.309370708856306353],
[0.218692707672397457, 0.195942913400042773, 0.314749999302432193],
[0.223586229324585051, 0.198603689049093424, 0.320100225814713701],
[0.228518686639013868, 0.201242183240559369, 0.325419827220328472],
[0.233489512216548456, 0.203858995059095272, 0.330707240946540915],
[0.238498096945698734, 0.206454744901104770, 0.335960905588456482],
[0.243543792054824293, 0.209030074656262998, 0.341179263480631989],
[0.248625911125045007, 0.211585647810811572, 0.346360763269660254],
[0.253743732062662375, 0.214122149473522039, 0.351503862484559337],
[0.258896499030044747, 0.216640286325279985, 0.356607030101538047],
[0.264083424334047134, 0.219140786493333184, 0.361668749099487097],
[0.269303690271153362, 0.221624399351350365, 0.366687519002339923],
[0.274556450928646112, 0.224091895246569250, 0.371661858404289558],
[0.279840833941214617, 0.226544065155450780, 0.376590307473693542],
[0.285155942202519386, 0.228981720269413547, 0.381471430431397252],
[0.290500855531311442, 0.231405691512393652, 0.386303817999108956],
[0.295874632291822981, 0.233816828992141956, 0.391086089813410531],
[0.301276310968197403, 0.236216001387368535, 0.395816896800944007],
[0.306704911692829985, 0.238604095273018624, 0.400494923510313239],
[0.312159437728548483, 0.240982014386159626, 0.405118890396253484],
[0.317638876904643208, 0.243350678835153156, 0.409687556051662849],
[0.323142203006812845, 0.245711024254962163, 0.414199719383159637],
[0.328668377121161814, 0.248064000911639049, 0.418654221725910436],
[0.334216348932433904, 0.250410572759208250, 0.423049948893591821],
[0.339785057976734417, 0.252751716452328967, 0.427385833159476425],
[0.345373434849041872, 0.255088420318277609, 0.431660855164788082],
[0.350980402365863309, 0.257421683291937820, 0.435874045750645644],
[0.356604876683432825, 0.259752513817614217, 0.440024487710094669],
[0.362245768371918853, 0.262081928721599300, 0.444111317456951204],
[0.367901983446140724, 0.264410952059519200, 0.448133726608385963],
[0.373572424353339150, 0.266740613942565430, 0.452090963478427199],
[0.379255990918617114, 0.269071949346771810, 0.455982334479805240],
[0.384951581248679564, 0.271405996909534652, 0.459807205431822574],
[0.390658092594579676, 0.273743797717587778, 0.463565002772209855],
[0.396374422174199492, 0.276086394090635234, 0.467255214671200070],
[0.402099467955245649, 0.278434828364815257, 0.470877392046346543],
[0.407832129399593402, 0.280790141680107686, 0.474431149476899183],
[0.413571308169832730, 0.283153372775730661, 0.477916166016847776],
[0.419315908798935655, 0.285525556797454116, 0.481332185906038712],
[0.425064839323974986, 0.287907724120662567, 0.484679019179073578],
[0.430817011884893020, 0.290300899192822370, 0.487956542171981977],
[0.436571343289329006, 0.292706099398870823, 0.491164697926971316],
[0.442326755544552697, 0.295124333952853257, 0.494303496495831551],
[0.448082176357602890, 0.297556602818923932, 0.497373015142860753],
[0.453836539604728084, 0.300003895664626208, 0.500373398448456408],
[0.459588785771273323, 0.302467190849124545, 0.503304858314781556],
[0.465337862363175148, 0.304947454448822763, 0.506167673875172253],
[0.471082724291258581, 0.307445639322545761, 0.508962191309204615],
[0.476822334229517864, 0.309962684218209272, 0.511688823565566553],
[0.482555662948626562, 0.312499512922624456, 0.514348049995109302],
[0.488281689625885862, 0.315057033455822144, 0.516940415896658401],
[0.493999402132871135, 0.317636137311002820, 0.519466531978352464],
[0.499707797302019474, 0.320237698740953813, 0.521927073737464608],
[0.505405881173408678, 0.322862574091504151, 0.524322780761812601],
[0.511092669222999452, 0.325511601182325527, 0.526654455956019452],
[0.516767186573581672, 0.328185598735129869, 0.528922964696000086],
[0.522428468189684581, 0.330885365849077184, 0.531129233915176413],
[0.528075559057704091, 0.333611681522958114, 0.533274251125995247],
[0.533707514352477430, 0.336365304223506856, 0.535359063380422717],
[0.539323399591541075, 0.339146971498981598, 0.537384776173121637],
[0.544922290778283802, 0.341957399636963089, 0.539352552291070153],
[0.550503274535211196, 0.344797283365134655, 0.541263610613408885],
[0.556065448228488912, 0.347667295593660330, 0.543119224865285188],
[0.561607920084956302, 0.350568087197621947, 0.544920722329472196],
[0.567129809302746146, 0.353500286837859112, 0.546669482519505756],
[0.572630246156655920, 0.356464500818440888, 0.548366935818022760],
[0.578108372099367496, 0.359461312978921199, 0.550014562083950609],
[0.583563339859622832, 0.362491284619447574, 0.551613889232087429],
[0.588994313538406367, 0.365554954456744630, 0.553166491788554149],
[0.594400468704196161, 0.368652838608956757, 0.554673989425479186],
[0.599780992488286868, 0.371785430607320333, 0.556138045478154930],
[0.605135083681207053, 0.374953201432613847, 0.557560365447788420],
[0.610461952831189203, 0.378156599574372032, 0.558942695492823827],
[0.615760822345651548, 0.381396051110849676, 0.560286820911660044],
[0.621030926596634059, 0.384671959807768193, 0.561594564619427139],
[0.626271512031079003, 0.387984707233930581, 0.562867785621322891],
[0.631481837286856695, 0.391334652891842549, 0.564108377484824897],
[0.636661173315405837, 0.394722134361540633, 0.565318266812911974],
[0.641808803511817683, 0.398147467455922166, 0.566499411720253421],
[0.646924023853215790, 0.401610946385930590, 0.567653800314101287],
[0.652006143046209741, 0.405112843934060551, 0.568783449181457512],
[0.657054482684237717, 0.408653411634718522, 0.569890401883858422],
[0.662068377415554688, 0.412232879960088394, 0.570976727460934419],
[0.667047175122617242, 0.415851458510243410, 0.572044518943688462],
[0.671990237113625377, 0.419509336206328520, 0.573095891878250163],
[0.676896938326905007, 0.423206681485779779, 0.574132982860628971],
[0.681766667548889704, 0.426943642498586740, 0.575157948082832715],
[0.686598827646332621, 0.430720347303770734, 0.576172961890485058],
[0.691392835813497308, 0.434536904065273066, 0.577180215351895343],
[0.696148123834919308, 0.438393401246624126, 0.578181914838366229],
[0.700864138364459599, 0.442289907803772808, 0.579180280615307796],
[0.705540341221227663, 0.446226473375615773, 0.580177545443581910],
[0.710176209703041628, 0.450203128471796610, 0.581175953190323780],
[0.714771236918011366, 0.454219884657461936, 0.582177757448341660],
[0.719324932134853268, 0.458276734734714031, 0.583185220163025209],
[0.723836821152511245, 0.462373652920588241, 0.584200610265588449],
[0.728306446689650166, 0.466510595021445040, 0.585226202311330157],
[0.732733368794583950, 0.470687498603721444, 0.586264275121491041],
[0.737117165276147679, 0.474904283161070972, 0.587317110427186595],
[0.741457432156053531, 0.479160850277941808, 0.588386991513812574],
[0.745753784143207921, 0.483457083789729791, 0.589476201864257643],
[0.750005855130455035, 0.487792849939663931, 0.590587023799193034],
[0.754213298714218050, 0.492167997532641122, 0.591721737112686941],
[0.758375788737437384, 0.496582358086250453, 0.592882617701357639],
[0.762493019856202547, 0.501035745979291791, 0.594071936185289307],
[0.766564708130438088, 0.505527958598098404, 0.595291956518940402],
[0.770590591638980027, 0.510058776481015497, 0.596544934590306108],
[0.774570431119305014, 0.514627963461421589, 0.597833116806655407],
[0.778504010632186771, 0.519235266809697671, 0.599158738665221180],
[0.782391138251447127, 0.523880417374567364, 0.600524023307303256],
[0.786231646778981719, 0.528563129724266778, 0.601931180054361970],
[0.790025394485133314, 0.533283102288011124, 0.603382402924778072],
[0.793772265874458372, 0.538040017498247702, 0.604879869130105052],
[0.797472172476850760, 0.542833541934202191, 0.606425737549780131],
[0.801125053663939268, 0.547663326467231260, 0.608022147183424955],
[0.804730877490553942, 0.552529006408532641, 0.609671215580047665],
[0.808289641561050098, 0.557430201659740887, 0.611375037243649166],
[0.811801373920098990, 0.562366516866985910, 0.613135682014921635],
[0.815266133967543660, 0.567337541578977311, 0.614955193428962543],
[0.818684013396768662, 0.572342850409695569, 0.616835587049115119],
[0.822055137155926374, 0.577382003206289296, 0.618778848777292056],
[0.825379664431282078, 0.582454545222774622, 0.620786933141354802],
[0.828657789651767174, 0.587560007300147014, 0.622861761560348226],
[0.831889743513757329, 0.592697906053519796, 0.625005220588625732],
[0.835075794024872864, 0.597867744066926776, 0.627219160140124465],
[0.838216247565577777, 0.603069010096389024, 0.629505391694263672],
[0.841311449967047320, 0.608301179281921400, 0.631865686485171274],
[0.844361787603741254, 0.613563713369071007, 0.634301773676134717],
[0.847367688498897098, 0.618856060940668695, 0.636815338521378171],
[0.850329623440946314, 0.624177657659408247, 0.639408020517444164],
[0.853248107108773524, 0.629527926521899150, 0.642081411546638670],
[0.856123699203416466, 0.634906278124844792, 0.644837054015123590],
[0.858957005583735778, 0.640312110943957458, 0.647676438988407210],
[0.861748679403274154, 0.645744811626264625, 0.650601004327062360],
[0.864499422245397220, 0.651203755296397957, 0.653612132825609482],
[0.867209985253533877, 0.656688305877496159, 0.656711150357558782],
[0.869881170253156477, 0.662197816427306241, 0.659899324029642354],
[0.872513830861911366, 0.667731629490055711, 0.663177860348283632],
[0.875108873584082181, 0.673289077464661601, 0.666547903401329078],
[0.877667258885373336, 0.678869482989799544, 0.670010533058023494],
[0.880190002243751324, 0.684472159346345754, 0.673566763190120765],
[0.882678175171918489, 0.690096410877650279, 0.677217539916933786],
[0.885132906206748338, 0.695741533428088088, 0.680963739876950247],
[0.887555381860854808, 0.701406814800268896, 0.684806168528487968],
[0.889946847531283502, 0.707091535231243573, 0.688745558481628328],
[0.892308608360134481, 0.712794967888015330, 0.692782567863411858],
[0.894642030041848169, 0.718516379382548864, 0.696917778717980774],
[0.896948539571730152, 0.724255030306458103, 0.701151695443002598],
[0.899229625930230036, 0.730010175785442250, 0.705484743263310343],
[0.901486840697522274, 0.735781066053453947, 0.709917266742249309],
[0.903721798592852621, 0.741566947046508162, 0.714449528330684758],
[0.905936177933324482, 0.747367061015900558, 0.719081706953062949],
[0.908131721006840031, 0.753180647160511918, 0.723813896629224018],
[0.910310234354204328, 0.759006942277722696, 0.728646105129914900],
[0.912473588955761139, 0.764845181432296628, 0.733578252663071084],
[0.914623720318282984, 0.770694598642454376, 0.738610170586920800],
[0.916762628458536177, 0.776554427582118345, 0.743741600144802728],
[0.918892377780584191, 0.782423902298113205, 0.748972191215228622],
[0.921015096844903458, 0.788302257940835749, 0.754301501069122970],
[0.923132978028491591, 0.794188731506613510, 0.759728993124300422],
[0.925248277076621384, 0.800082562589614521, 0.765254035685009049],
[0.927363312548626473, 0.805982994140769793, 0.770875900651706081],
[0.929480465162262015, 0.811889273230691266, 0.776593762183022451],
[0.931602177043897362, 0.817800651812955026, 0.782406695287998888],
[0.933730950894930190, 0.823716387483477086, 0.788313674321911240],
[0.935869349088971125, 0.829635744230789451, 0.794313571353191916],
[0.938019992719183238, 0.835557993171028857, 0.800405154361686244],
[0.940185560621455752, 0.841482413260103979, 0.806587085219469646],
[0.942368788406770186, 0.847408291973871686, 0.812857917394013807],
[0.944572467545971572, 0.853334925945050449, 0.819216093299021564],
[0.946799444562658521, 0.859261621542897647, 0.825659941199610614],
[0.949052620406097280, 0.865187695378128896, 0.832187671554412200],
[0.951334950097077692, 0.871112474710942442, 0.838797372645517347],
[0.953649442767544708, 0.877035297733740338, 0.845487005305295192],
[0.955999162252142542, 0.882955513691752070, 0.852254396492841293],
[0.958387228440498284, 0.888872482793146679, 0.859097231396288352],
[0.960816819669265354, 0.894785575844048830, 0.866013043631538082],
[0.963291176531399285, 0.900694173520913299, 0.872999202959681697],
[0.965813607621515469, 0.906597665159457611, 0.880052899733509086],
[0.968387497942739484, 0.912495446890373652, 0.887171124974651115],
[0.971016321010112260, 0.918386918878006719, 0.894350644522526883],
[0.973703656161199249, 0.924271481303683307, 0.901587964992457969],
[0.976453213337372339, 0.930148528552835030, 0.908879288172974586],
[0.979268868830558525, 0.936017440764600916, 0.916220448691765110],
[0.982154717584085568, 0.941877571388391566, 0.923606826737530695],
[0.985115151361209418, 0.947728228471621192, 0.931033222248013437],
[0.988154979089757801, 0.953568645664416459, 0.938493666944184235],
[0.991279619721871952, 0.959397935419655679, 0.945981130607293053],
[0.994495428510114521, 0.965215009182105788, 0.953487034763436214],
[0.997810291683775774, 0.971018430624328688, 0.961000382873643422],
[1.00000000000000000, 0.976806115149730148, 0.968506026447674473],
[1.00000000000000000, 0.982574604290608611, 0.975980588066381105],
[1.00000000000000000, 0.988316713794476720, 0.983379606660296335],
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
